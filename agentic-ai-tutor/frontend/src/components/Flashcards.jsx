import { useState, useEffect, useCallback, useMemo } from 'react';
import { generateQuiz, getChapterList } from '../api/client';

const SRS_KEY = 'agenticai-tutor-srs';

// --- SM-2 Spaced Repetition helpers ---

function loadSrs() {
  try { return JSON.parse(localStorage.getItem(SRS_KEY) || '{}'); } catch { return {}; }
}

function saveSrs(data) {
  localStorage.setItem(SRS_KEY, JSON.stringify(data));
}

function cardKey(card) {
  return (card.question || '').substring(0, 80);
}

function todayStr() {
  return new Date().toISOString().slice(0, 10);
}

function addDays(dateStr, days) {
  const d = new Date(dateStr);
  d.setDate(d.getDate() + days);
  return d.toISOString().slice(0, 10);
}

function defaultSrsEntry() {
  return { easeFactor: 2.5, interval: 0, repetitions: 0, nextReview: null, lastQuality: null };
}

function sm2(entry, quality) {
  let { easeFactor, interval, repetitions } = entry;

  easeFactor = easeFactor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02));
  if (easeFactor < 1.3) easeFactor = 1.3;

  if (quality >= 3) {
    repetitions += 1;
    if (repetitions === 1) {
      interval = 1;
    } else if (repetitions === 2) {
      interval = 6;
    } else {
      interval = Math.round(interval * easeFactor);
    }
  } else {
    repetitions = 0;
    interval = 1;
  }

  const nextReview = addDays(todayStr(), interval);

  return { easeFactor, interval, repetitions, nextReview, lastQuality: quality };
}

function predictIntervals(entry) {
  const predictions = {};
  for (const [label, q] of [['again', 0], ['hard', 1], ['good', 3], ['easy', 5]]) {
    const result = sm2(entry || defaultSrsEntry(), q);
    predictions[label] = result.interval;
  }
  return predictions;
}

function formatInterval(days, lang) {
  if (days < 1) return lang === 'hu' ? '<1p' : '<1m';
  if (days === 1) return lang === 'hu' ? '1n' : '1d';
  if (days < 30) return `${days}${lang === 'hu' ? 'n' : 'd'}`;
  if (days < 365) {
    const months = Math.round(days / 30);
    return `${months}${lang === 'hu' ? 'ho' : 'mo'}`;
  }
  const years = (days / 365).toFixed(1);
  return `${years}${lang === 'hu' ? 'e' : 'y'}`;
}

function buildSrsDeck(cards, srsData) {
  const today = todayStr();
  const due = [];
  const newCards = [];

  for (const c of cards) {
    const key = cardKey(c);
    const entry = srsData[key];
    if (!entry || !entry.nextReview) {
      newCards.push(c);
    } else if (entry.nextReview <= today) {
      due.push(c);
    }
  }

  due.sort((a, b) => {
    const ea = srsData[cardKey(a)];
    const eb = srsData[cardKey(b)];
    return (ea.nextReview || '').localeCompare(eb.nextReview || '');
  });

  return { deck: [...due, ...newCards], dueCount: due.length, newCount: newCards.length };
}

export default function Flashcards({ sessionId, lang }) {
  const [chapters, setChapters] = useState([]);
  const [selectedChapters, setSelectedChapters] = useState({});
  const [allCards, setAllCards] = useState([]);
  const [deck, setDeck] = useState([]);
  const [dueCount, setDueCount] = useState(0);
  const [newCount, setNewCount] = useState(0);
  const [idx, setIdx] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [srsData, setSrsData] = useState(loadSrs);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [sessionDone, setSessionDone] = useState(false);

  const t = lang === 'hu' ? {
    title: 'Tanulókártyák',
    chapter: 'Fejezet',
    all: 'Mind',
    none: 'Egyik sem',
    start: 'Kártyák betöltése',
    flip: 'Kattints a megfordításhoz',
    again: 'Újra',
    hard: 'Nehéz',
    good: 'Jó',
    easy: 'Könnyű',
    loading: 'Kártyák betöltése...',
    noCards: 'Nincs elérhető kártya. Válassz fejezeteket és próbáld újra.',
    question: 'Kérdés',
    answer: 'Válasz',
    correct: 'Helyes válasz',
    explanation: 'Magyarázat',
    restart: 'Újrakezdés',
    done: 'Gratulálok! Minden esedékes kártyát átnéztél.',
    dueToday: 'Esedékes ma',
    newLabel: 'Új',
    learned: 'Tanult',
    sessionComplete: 'A mai adag kész!',
    backToSetup: 'Vissza',
  } : {
    title: 'Flashcards',
    chapter: 'Chapter',
    all: 'All',
    none: 'None',
    start: 'Load Cards',
    flip: 'Click to flip',
    again: 'Again',
    hard: 'Hard',
    good: 'Good',
    easy: 'Easy',
    loading: 'Loading cards...',
    noCards: 'No cards available. Select chapters and try again.',
    question: 'Question',
    answer: 'Answer',
    correct: 'Correct answer',
    explanation: 'Explanation',
    restart: 'Restart',
    done: 'Congratulations! All due cards reviewed.',
    dueToday: 'Due today',
    newLabel: 'New',
    learned: 'Learned',
    sessionComplete: 'Session complete!',
    backToSetup: 'Back',
  };

  useEffect(() => {
    getChapterList().then((chs) => {
      setChapters(chs);
      const sel = {};
      chs.forEach((ch) => { sel[ch.chapter_num] = true; });
      setSelectedChapters(sel);
    }).catch(() => {});
  }, []);

  const learnedCount = useMemo(() => {
    let count = 0;
    for (const c of allCards) {
      const entry = srsData[cardKey(c)];
      if (entry && entry.repetitions > 0) count++;
    }
    return count;
  }, [allCards, srsData]);

  const rebuildDeck = useCallback((cards, data) => {
    const { deck: d, dueCount: dc, newCount: nc } = buildSrsDeck(cards, data);
    setDeck(d);
    setDueCount(dc);
    setNewCount(nc);
    setIdx(0);
    setFlipped(false);
    setSessionDone(d.length === 0);
    return d;
  }, []);

  const loadCards = async () => {
    const activeChapters = Object.entries(selectedChapters).filter(([, v]) => v).map(([k]) => Number(k));
    if (activeChapters.length === 0) {
      setError(lang === 'hu' ? 'Válassz legalább egy fejezetet' : 'Select at least one chapter');
      return;
    }
    setError('');
    setLoading(true);
    try {
      const allSelected = activeChapters.length === chapters.length;
      const chNums = allSelected ? null : activeChapters;
      const data = await generateQuiz(chNums, 20, sessionId, lang, ['mcq', 'true_false', 'fill_blank']);
      const cards = data.questions || [];
      if (cards.length === 0) {
        setError(t.noCards);
        setAllCards([]);
        setDeck([]);
      } else {
        setAllCards(cards);
        rebuildDeck(cards, srsData);
      }
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const flip = useCallback(() => setFlipped((f) => !f), []);

  const rate = useCallback((quality) => {
    if (deck.length === 0 || sessionDone) return;
    const card = deck[idx];
    const key = cardKey(card);
    const entry = srsData[key] || defaultSrsEntry();
    const updated = sm2(entry, quality);
    const newSrsData = { ...srsData, [key]: updated };
    setSrsData(newSrsData);
    saveSrs(newSrsData);

    setFlipped(false);
    if (idx < deck.length - 1) {
      if (quality < 3) {
        const newDeck = [...deck];
        newDeck.push(card);
        setDeck(newDeck);
      }
      setIdx(idx + 1);
    } else {
      if (quality < 3) {
        const newDeck = [...deck, card];
        setDeck(newDeck);
        setIdx(idx + 1);
      } else {
        setSessionDone(true);
      }
    }
  }, [deck, idx, srsData, sessionDone]);

  // Keyboard support
  useEffect(() => {
    const handler = (e) => {
      if (deck.length === 0 || sessionDone) return;
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); }
      if (e.key === '1') rate(0);
      if (e.key === '2') rate(1);
      if (e.key === '3') rate(3);
      if (e.key === '4') rate(5);
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [deck, sessionDone, flip, rate]);

  // Setup screen
  if (allCards.length === 0 && !loading) {
    return (
      <div className="h-full flex flex-col items-center justify-center p-8">
        <h2 className="text-xl font-bold mb-6" style={{ color: 'var(--text-primary)' }}>{t.title}</h2>
        <div className="w-full max-w-sm space-y-4">
          <div>
            <div className="flex items-center justify-between mb-1">
              <label className="text-sm" style={{ color: 'var(--text-secondary)' }}>{t.chapter}</label>
              <div className="flex gap-2">
                <button onClick={() => { const s = {}; chapters.forEach((ch) => { s[ch.chapter_num] = true; }); setSelectedChapters(s); }}
                  className="text-xs cursor-pointer underline" style={{ color: 'var(--accent)' }}>{t.all}</button>
                <button onClick={() => { const s = {}; chapters.forEach((ch) => { s[ch.chapter_num] = false; }); setSelectedChapters(s); }}
                  className="text-xs cursor-pointer underline" style={{ color: 'var(--accent)' }}>{t.none}</button>
              </div>
            </div>
            <div className="max-h-40 overflow-y-auto rounded-lg border p-2 space-y-0.5" style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)' }}>
              {chapters.map((ch) => (
                <label key={ch.chapter_num} className="flex items-center gap-2 cursor-pointer text-xs py-0.5"
                  style={{ color: selectedChapters[ch.chapter_num] ? 'var(--text-primary)' : 'var(--text-secondary)' }}>
                  <input type="checkbox" checked={!!selectedChapters[ch.chapter_num]}
                    onChange={() => setSelectedChapters((prev) => ({ ...prev, [ch.chapter_num]: !prev[ch.chapter_num] }))}
                    className="cursor-pointer" />
                  {ch.chapter_title}
                </label>
              ))}
            </div>
          </div>

          {error && <p className="text-xs" style={{ color: 'var(--error)' }}>{error}</p>}

          <button
            onClick={loadCards}
            className="w-full py-2.5 rounded-lg text-white font-medium cursor-pointer"
            style={{ background: 'var(--accent)' }}
          >{t.start}</button>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="h-full flex flex-col items-center justify-center gap-4" style={{ color: 'var(--text-secondary)' }}>
        <div className="w-8 h-8 border-3 border-t-transparent rounded-full animate-spin" style={{ borderColor: 'var(--accent)', borderTopColor: 'transparent' }} />
        <p className="text-sm font-medium">{t.loading}</p>
      </div>
    );
  }

  // Session complete screen
  if (sessionDone) {
    return (
      <div className="h-full flex flex-col items-center justify-center gap-4 p-8">
        <div className="text-4xl mb-2">&#10003;</div>
        <h2 className="text-lg font-bold" style={{ color: 'var(--text-primary)' }}>{t.sessionComplete}</h2>
        <p className="text-sm" style={{ color: 'var(--text-secondary)' }}>{t.done}</p>
        <div className="flex gap-6 mt-2 text-sm" style={{ color: 'var(--text-secondary)' }}>
          <span>{t.learned}: {learnedCount}</span>
        </div>
        <div className="flex gap-3 mt-4">
          <button
            onClick={() => { setAllCards([]); setDeck([]); setIdx(0); setFlipped(false); setSessionDone(false); }}
            className="px-4 py-2 rounded-lg text-sm font-medium cursor-pointer"
            style={{ background: 'var(--accent)', color: 'white' }}
          >{t.backToSetup}</button>
          <button
            onClick={() => rebuildDeck(allCards, srsData)}
            className="px-4 py-2 rounded-lg text-sm font-medium cursor-pointer border"
            style={{ borderColor: 'var(--border)', color: 'var(--text-primary)' }}
          >{t.restart}</button>
        </div>
      </div>
    );
  }

  const card = deck[idx];
  if (!card) return null;

  const currentEntry = srsData[cardKey(card)] || defaultSrsEntry();
  const intervals = predictIntervals(currentEntry);

  const renderAnswer = () => {
    const parts = [];
    const correctVal = card.correct_answer ?? card.correct;
    if (card.type === 'mcq') {
      const correctOpt = card.options?.find((o) => o.charAt(0) === String(correctVal));
      parts.push(
        <p key="correct" className="text-sm font-semibold mb-2" style={{ color: 'var(--success)' }}>
          {t.correct}: {correctOpt || correctVal}
        </p>
      );
    } else if (card.type === 'true_false') {
      const val = String(correctVal).toLowerCase();
      const display = val === 'true' || val === 'igaz'
        ? (lang === 'hu' ? 'Igaz' : 'True')
        : (lang === 'hu' ? 'Hamis' : 'False');
      parts.push(
        <p key="correct" className="text-sm font-semibold mb-2" style={{ color: 'var(--success)' }}>
          {t.correct}: {display}
        </p>
      );
    } else if (card.type === 'fill_blank') {
      parts.push(
        <p key="correct" className="text-sm font-semibold mb-2" style={{ color: 'var(--success)' }}>
          {t.correct}: {correctVal}
        </p>
      );
    }
    if (card.explanation) {
      parts.push(
        <p key="expl" className="text-xs mt-2" style={{ color: 'var(--text-secondary)' }}>
          {t.explanation}: {card.explanation}
        </p>
      );
    }
    return parts;
  };

  return (
    <div className="h-full flex flex-col">
      {/* Header bar */}
      <div className="px-4 py-2 border-b flex items-center gap-3" style={{ borderColor: 'var(--border)' }}>
        <span className="text-xs font-medium" style={{ color: 'var(--text-secondary)' }}>
          {idx + 1}/{deck.length}
        </span>
        <div className="flex-1 h-1.5 rounded-full" style={{ background: 'var(--border)' }}>
          <div className="h-full rounded-full transition-all" style={{ width: `${((idx + 1) / deck.length) * 100}%`, background: 'var(--accent)' }} />
        </div>
        <div className="flex gap-2 text-xs" style={{ color: 'var(--text-secondary)' }}>
          <span style={{ color: 'var(--warning)' }}>{t.dueToday}: {dueCount}</span>
          <span style={{ color: 'var(--accent)' }}>{t.newLabel}: {newCount}</span>
          <span style={{ color: 'var(--success)' }}>{t.learned}: {learnedCount}</span>
        </div>
        <span className={`text-xs px-1.5 py-0.5 rounded-full ${
          card.type === 'mcq' ? 'bg-green-100 text-green-800' :
          card.type === 'true_false' ? 'bg-emerald-100 text-emerald-800' : 'bg-purple-100 text-purple-800'
        }`}>{card.type}</span>
        <button
          onClick={() => { setAllCards([]); setDeck([]); setIdx(0); setFlipped(false); setSessionDone(false); }}
          className="text-xs cursor-pointer underline"
          style={{ color: 'var(--text-secondary)' }}
        >{t.backToSetup}</button>
      </div>

      {/* Card */}
      <div className="flex-1 flex items-center justify-center p-6">
        <div
          onClick={flip}
          className="w-full max-w-md min-h-48 rounded-2xl border-2 p-6 cursor-pointer select-none transition-all"
          style={{
            borderColor: flipped ? 'var(--success)' : 'var(--accent)',
            background: flipped ? 'var(--bg-secondary)' : 'var(--bg-primary)',
            boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
          }}
        >
          <div className="text-xs font-medium uppercase tracking-wide mb-3" style={{ color: 'var(--text-secondary)' }}>
            {flipped ? t.answer : t.question}
          </div>
          {!flipped ? (
            <div>
              <p className="text-sm leading-relaxed" style={{ color: 'var(--text-primary)' }}>{card.question}</p>
              {card.type === 'mcq' && card.options && (
                <div className="mt-3 space-y-1">
                  {card.options.map((opt, i) => (
                    <p key={i} className="text-xs" style={{ color: 'var(--text-secondary)' }}>{opt}</p>
                  ))}
                </div>
              )}
              <p className="text-xs mt-4 italic" style={{ color: 'var(--text-secondary)' }}>{t.flip}</p>
            </div>
          ) : (
            <div>{renderAnswer()}</div>
          )}
        </div>
      </div>

      {/* SM-2 Rating buttons */}
      <div className="px-4 py-3 border-t flex gap-2 justify-center" style={{ borderColor: 'var(--border)' }}>
        <button
          onClick={() => rate(0)}
          className="px-4 py-2 rounded-lg text-xs font-medium cursor-pointer flex flex-col items-center gap-0.5"
          style={{ background: 'var(--error)', color: 'white', minWidth: '5rem' }}
        >
          <span>{t.again} (1)</span>
          <span className="opacity-75 text-[10px]">{formatInterval(intervals.again, lang)}</span>
        </button>
        <button
          onClick={() => rate(1)}
          className="px-4 py-2 rounded-lg text-xs font-medium cursor-pointer flex flex-col items-center gap-0.5"
          style={{ background: 'var(--warning)', color: 'white', minWidth: '5rem' }}
        >
          <span>{t.hard} (2)</span>
          <span className="opacity-75 text-[10px]">{formatInterval(intervals.hard, lang)}</span>
        </button>
        <button
          onClick={() => rate(3)}
          className="px-4 py-2 rounded-lg text-xs font-medium cursor-pointer flex flex-col items-center gap-0.5"
          style={{ background: 'var(--success)', color: 'white', minWidth: '5rem' }}
        >
          <span>{t.good} (3)</span>
          <span className="opacity-75 text-[10px]">{formatInterval(intervals.good, lang)}</span>
        </button>
        <button
          onClick={() => rate(5)}
          className="px-4 py-2 rounded-lg text-xs font-medium cursor-pointer flex flex-col items-center gap-0.5"
          style={{ background: '#22c55e', color: 'white', minWidth: '5rem' }}
        >
          <span>{t.easy} (4)</span>
          <span className="opacity-75 text-[10px]">{formatInterval(intervals.easy, lang)}</span>
        </button>
      </div>
    </div>
  );
}
