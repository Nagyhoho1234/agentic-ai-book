import { useState, useEffect, useRef } from 'react';
import { generateQuiz, evaluateQuiz, getChapterList } from '../api/client';

function LoadingScreen({ label }) {
  const [elapsed, setElapsed] = useState(0);
  const startRef = useRef(Date.now());

  useEffect(() => {
    startRef.current = Date.now();
    setElapsed(0);
    const interval = setInterval(() => {
      setElapsed(Math.floor((Date.now() - startRef.current) / 1000));
    }, 1000);
    return () => clearInterval(interval);
  }, [label]);

  const dots = '.'.repeat((elapsed % 3) + 1);

  return (
    <div className="h-full flex flex-col items-center justify-center gap-4" style={{ color: 'var(--text-secondary)' }}>
      <div className="w-8 h-8 border-3 border-t-transparent rounded-full animate-spin" style={{ borderColor: 'var(--accent)', borderTopColor: 'transparent' }} />
      <p className="text-sm font-medium">{label}{dots}</p>
      <p className="text-xs">{elapsed}s</p>
    </div>
  );
}

const Q_TYPES = [
  { key: 'mcq', hu: 'Feleletválasztós', en: 'Multiple choice' },
  { key: 'true_false', hu: 'Igaz/hamis', en: 'True/false' },
  { key: 'fill_blank', hu: 'Kiegészítős', en: 'Fill in the blank' },
  { key: 'essay', hu: 'Esszé', en: 'Essay' },
];

export default function QuizPanel({ sessionId, lang, onQuizResults, onShowResults }) {
  const [chapters, setChapters] = useState([]);
  const [selectedChapters, setSelectedChapters] = useState({});
  const [numInput, setNumInput] = useState('5');
  const [numError, setNumError] = useState('');
  const [selectedTypes, setSelectedTypes] = useState({ mcq: true, true_false: true, fill_blank: true, essay: true });
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [results, setResults] = useState({});
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [done, setDone] = useState(false);
  const [currentQ, setCurrentQ] = useState(0);

  const t = lang === 'hu' ? {
    title: 'Tudásfelmérés',
    chapter: 'Fejezet',
    allChapters: 'Teljes könyv',
    numQ: 'Kérdések száma',
    types: 'Kérdéstípusok',
    start: 'Teszt indítása',
    submit: 'Beküldés',
    next: 'Következő',
    prev: 'Előző',
    loading: 'Kérdések generálása...',
    submitting: 'Értékelés...',
    yourAnswer: 'Válaszod...',
    essayPlaceholder: 'Írd le a válaszod részletesen...',
    of: '/',
    numErr: 'Adj meg egy számot (1-20)',
    noTypes: 'Válassz legalább egy típust',
    all: 'Mind',
    none: 'Egyik sem',
  } : {
    title: 'Self-Test',
    chapter: 'Chapter',
    allChapters: 'Whole book',
    numQ: 'Number of questions',
    types: 'Question types',
    start: 'Start Test',
    submit: 'Submit',
    next: 'Next',
    prev: 'Previous',
    loading: 'Generating questions...',
    submitting: 'Grading...',
    yourAnswer: 'Your answer...',
    essayPlaceholder: 'Write your answer in detail...',
    of: '/',
    numErr: 'Enter a number (1-20)',
    noTypes: 'Select at least one type',
    all: 'All',
    none: 'None',
  };

  useEffect(() => {
    getChapterList().then((chs) => {
      setChapters(chs);
      const sel = {};
      chs.forEach((ch) => { sel[ch.chapter_num] = true; });
      setSelectedChapters(sel);
    }).catch(() => {});
  }, []);

  const toggleType = (key) => {
    setSelectedTypes((prev) => ({ ...prev, [key]: !prev[key] }));
  };

  const startQuiz = async () => {
    const num = parseInt(numInput);
    if (isNaN(num) || num < 1 || num > 20) {
      setNumError(t.numErr);
      return;
    }
    const activeTypes = Object.entries(selectedTypes).filter(([, v]) => v).map(([k]) => k);
    if (activeTypes.length === 0) {
      setNumError(t.noTypes);
      return;
    }
    const activeChapters = Object.entries(selectedChapters).filter(([, v]) => v).map(([k]) => Number(k));
    if (activeChapters.length === 0) {
      setNumError(lang === 'hu' ? 'Valassz legalabb egy fejezetet' : 'Select at least one chapter');
      return;
    }
    setNumError('');
    setLoading(true);
    setQuestions([]);
    setAnswers({});
    setResults({});
    setDone(false);
    setCurrentQ(0);
    try {
      const allSelected = activeChapters.length === chapters.length;
      const chNums = allSelected ? null : activeChapters;
      const data = await generateQuiz(chNums, num, sessionId, lang, activeTypes);
      if (data.error) {
        setNumError(data.error);
        setQuestions([]);
      } else if (!data.questions || data.questions.length === 0) {
        setNumError(lang === 'hu' ? 'Nem sikerult kerdeseket generalni. Probald ujra.' : 'Failed to generate questions. Try again.');
        setQuestions([]);
      } else {
        setQuestions(data.questions);
      }
    } catch (e) {
      setNumError(lang === 'hu' ? `Hiba: ${e.message}. Probald ujra.` : `Error: ${e.message}. Try again.`);
      setQuestions([]);
    } finally {
      setLoading(false);
    }
  };

  const handleAnswer = (qId, value, autoAdvance = false) => {
    setAnswers((prev) => ({ ...prev, [qId]: value }));
    if (autoAdvance && currentQ < questions.length - 1) {
      setTimeout(() => setCurrentQ((c) => c + 1), 300);
    }
  };

  const submitAll = async () => {
    setSubmitting(true);
    const newResults = {};
    for (const q of questions) {
      const answer = answers[q.id] || '';
      if (!answer) { newResults[q.id] = { correct: false, skipped: true }; continue; }
      try {
        newResults[q.id] = await evaluateQuiz(q, answer, sessionId);
      } catch {
        newResults[q.id] = { correct: false, error: true };
      }
    }
    setResults(newResults);
    setSubmitting(false);
    setDone(true);
    onQuizResults?.(questions, newResults);
  };

  // Export quiz results via window.print()
  const handleExportPDF = (qs, res, pct, correctCount, mcqTotal, essayAvg, lng) => {
    const dateStr = new Date().toLocaleDateString(lng === 'hu' ? 'hu-HU' : 'en-US', {
      year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit',
    });
    const title = lng === 'hu' ? 'Precíziós Mezőgazdaság Teszt Eredmények' : 'Precision Agriculture Test Results';
    const rows = qs.map((q, i) => {
      const r = res[q.id] || {};
      const isEssay = q.type === 'essay';
      const mark = isEssay ? `${r.score || 0}%` : (r.correct ? '\u2714' : '\u2718');
      const markColor = (isEssay ? (r.score >= 50) : r.correct) ? '#16a34a' : '#dc2626';
      const userAns = answers[q.id] || (lng === 'hu' ? '(nem válaszolt)' : '(skipped)');
      const correctAns = !isEssay && r.correct_answer ? r.correct_answer : '';
      const chRef = q.chapter_num ? `Ch. ${q.chapter_num}` : '';
      return `<tr>
        <td style="padding:6px;border:1px solid #ddd;text-align:center;width:28px;color:${markColor};font-weight:bold">${mark}</td>
        <td style="padding:6px;border:1px solid #ddd">
          <strong>${i + 1}. ${q.question}</strong>
          <br/><span style="color:#555">${lng === 'hu' ? 'Válaszod' : 'Your answer'}: ${userAns}</span>
          ${correctAns && !r.correct ? `<br/><span style="color:#555">${lng === 'hu' ? 'Helyes válasz' : 'Correct answer'}: ${correctAns}</span>` : ''}
          ${r.explanation ? `<br/><em style="color:#666">${r.explanation}</em>` : ''}
          ${r.feedback ? `<br/><em style="color:#666">${r.feedback}</em>` : ''}
          ${chRef ? `<br/><span style="color:#888;font-size:11px">${chRef}</span>` : ''}
        </td>
      </tr>`;
    }).join('');

    const html = `<!DOCTYPE html><html><head><meta charset="utf-8"/>
      <title>${title}</title>
      <style>
        body{font-family:system-ui,sans-serif;max-width:700px;margin:0 auto;padding:24px;color:#1a1a2e}
        h1{font-size:20px;margin-bottom:4px}
        .meta{color:#555;font-size:13px;margin-bottom:16px}
        .score{font-size:32px;font-weight:bold;text-align:center;margin:16px 0}
        table{width:100%;border-collapse:collapse;font-size:13px}
        td{vertical-align:top}
      </style>
    </head><body>
      <h1>${title}</h1>
      <p class="meta">${dateStr}</p>
      <div class="score" style="color:${pct >= 70 ? '#16a34a' : pct >= 40 ? '#d97706' : '#dc2626'}">${pct}%</div>
      <p style="text-align:center;color:#555;font-size:13px;margin-bottom:20px">
        ${mcqTotal > 0 ? `${lng === 'hu' ? 'Helyes' : 'Correct'}: ${correctCount}/${mcqTotal}` : ''}
        ${essayAvg != null ? ` | ${lng === 'hu' ? 'Essze atlag' : 'Essay avg'}: ${essayAvg}%` : ''}
      </p>
      <table>${rows}</table>
    </body></html>`;

    const printWin = window.open('', '_blank', 'width=800,height=600');
    if (printWin) {
      printWin.document.write(html);
      printWin.document.close();
      setTimeout(() => printWin.print(), 300);
    }
  };

  // Setup screen
  if (questions.length === 0 && !loading) {
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

          <div>
            <label className="block text-sm mb-1" style={{ color: 'var(--text-secondary)' }}>{t.numQ}</label>
            <input
              type="text"
              value={numInput}
              onChange={(e) => { setNumInput(e.target.value); setNumError(''); }}
              className="w-full px-3 py-2 rounded-lg border text-sm outline-none"
              style={{ borderColor: numError ? 'var(--error)' : 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
            {numError && <p className="text-xs mt-1" style={{ color: 'var(--error)' }}>{numError}</p>}
          </div>

          <div>
            <label className="block text-sm mb-1" style={{ color: 'var(--text-secondary)' }}>{t.types}</label>
            <div className="flex flex-wrap gap-2">
              {Q_TYPES.map((qt) => (
                <button
                  key={qt.key}
                  onClick={() => toggleType(qt.key)}
                  className="px-3 py-1.5 text-xs rounded-lg border cursor-pointer"
                  style={{
                    borderColor: selectedTypes[qt.key] ? 'var(--accent)' : 'var(--border)',
                    background: selectedTypes[qt.key] ? 'var(--bg-chat)' : 'transparent',
                    color: selectedTypes[qt.key] ? 'var(--accent)' : 'var(--text-secondary)',
                  }}
                >{lang === 'hu' ? qt.hu : qt.en}</button>
              ))}
            </div>
          </div>

          <button
            onClick={startQuiz}
            className="w-full py-2.5 rounded-lg text-white font-medium cursor-pointer"
            style={{ background: 'var(--accent)' }}
          >{t.start}</button>
        </div>
      </div>
    );
  }

  if (loading || submitting) {
    const label = loading ? t.loading : t.submitting;
    return <LoadingScreen label={label} />;
  }

  if (done) {
    const mcqQs = questions.filter((q) => q.type !== 'essay');
    const essayQs = questions.filter((q) => q.type === 'essay');
    const correctCount = mcqQs.filter((q) => results[q.id]?.correct).length;
    const essayScores = essayQs.map((q) => results[q.id]?.score).filter((s) => s != null);
    const essayAvg = essayScores.length > 0 ? Math.round(essayScores.reduce((a, b) => a + b, 0) / essayScores.length) : null;
    const pct = questions.length > 0
      ? Math.round(((correctCount + (essayAvg || 0) / 100 * essayQs.length) / questions.length) * 100)
      : 0;
    const pctColor = pct >= 70 ? 'var(--success)' : pct >= 40 ? 'var(--warning)' : 'var(--error)';

    return (
      <div className="h-full flex flex-col overflow-y-auto p-6">
        {/* Score */}
        <div className="flex justify-center mb-4">
          <div className="w-24 h-24 rounded-full flex items-center justify-center border-4" style={{ borderColor: pctColor }}>
            <span className="text-2xl font-bold" style={{ color: pctColor }}>{pct}%</span>
          </div>
        </div>
        <div className="text-center text-sm mb-4" style={{ color: 'var(--text-secondary)' }}>
          {mcqQs.length > 0 && <p>{lang === 'hu' ? 'Helyes' : 'Correct'}: {correctCount}/{mcqQs.length}</p>}
          {essayAvg != null && <p>{lang === 'hu' ? 'Essze atlag' : 'Essay avg'}: {essayAvg}%</p>}
        </div>

        {/* Per-question results */}
        <div className="space-y-3 mb-6">
          {questions.map((q) => {
            const r = results[q.id] || {};
            const isEssay = q.type === 'essay';
            return (
              <div key={q.id} className="rounded-lg border p-3 text-xs" style={{ borderColor: 'var(--border)' }}>
                <div className="flex items-start gap-2 mb-1">
                  <span className="font-bold" style={{ color: r.correct ? 'var(--success)' : 'var(--error)' }}>
                    {isEssay ? `${r.score || 0}%` : (r.correct ? '\u2714' : '\u2718')}
                  </span>
                  <p className="flex-1" style={{ color: 'var(--text-primary)' }}>{q.question}</p>
                </div>
                {r.feedback && <p className="pl-5 mt-1" style={{ color: 'var(--text-secondary)' }}>{r.feedback}</p>}
                {!isEssay && !r.correct && r.correct_answer && (
                  <p className="pl-5 mt-1" style={{ color: 'var(--text-secondary)' }}>
                    {lang === 'hu' ? 'Helyes válasz' : 'Correct answer'}: {r.correct_answer}
                  </p>
                )}
                {r.explanation && <p className="pl-5 mt-1 italic" style={{ color: 'var(--text-secondary)' }}>{r.explanation}</p>}
              </div>
            );
          })}
        </div>

        {/* Buttons */}
        <div className="flex gap-3 flex-wrap">
          <button
            onClick={() => onShowResults?.()}
            className="flex-1 py-2 rounded-lg text-white cursor-pointer text-sm font-medium min-w-[120px]"
            style={{ background: 'var(--accent)' }}
          >{lang === 'hu' ? 'Válaszok a könyvben' : 'Answers in Book'}</button>
          <button
            onClick={() => handleExportPDF(questions, results, pct, correctCount, mcqQs.length, essayAvg, lang)}
            className="flex-1 py-2 rounded-lg border cursor-pointer text-sm font-medium min-w-[120px]"
            style={{ borderColor: 'var(--accent)', color: 'var(--accent)' }}
          >{lang === 'hu' ? 'Exportálás' : 'Export'}</button>
          <button
            onClick={() => { setQuestions([]); setResults({}); setDone(false); }}
            className="flex-1 py-2 rounded-lg border cursor-pointer text-sm min-w-[120px]"
            style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}
          >{lang === 'hu' ? 'Uj teszt' : 'New Test'}</button>
        </div>
      </div>
    );
  }

  // Quiz in progress
  const q = questions[currentQ];
  if (!q) return null;

  return (
    <div className="h-full flex flex-col">
      {/* Progress */}
      <div className="px-4 py-2 border-b flex items-center gap-3" style={{ borderColor: 'var(--border)' }}>
        <span className="text-xs font-medium" style={{ color: 'var(--text-secondary)' }}>
          {currentQ + 1}{t.of}{questions.length}
        </span>
        <div className="flex-1 h-1.5 rounded-full" style={{ background: 'var(--border)' }}>
          <div className="h-full rounded-full transition-all" style={{ width: `${((currentQ + 1) / questions.length) * 100}%`, background: 'var(--accent)' }} />
        </div>
        <span className={`text-xs px-1.5 py-0.5 rounded-full ${
          q.type === 'essay' ? 'bg-purple-100 text-purple-800' : q.type === 'mcq' ? 'bg-green-100 text-green-800' : 'bg-emerald-100 text-emerald-800'
        }`}>{q.type}</span>
      </div>

      {/* Question */}
      <div className="flex-1 overflow-y-auto p-5">
        <p className="text-sm font-medium mb-4" style={{ color: 'var(--text-primary)' }}>{q.question}</p>

        {q.type === 'mcq' && q.options && (
          <div className="space-y-2">
            {q.options.map((opt, i) => {
              const letter = opt.charAt(0);
              const selected = answers[q.id] === letter;
              return (
                <button key={i} onClick={() => handleAnswer(q.id, letter, true)}
                  className="w-full text-left px-4 py-2.5 rounded-lg border text-sm cursor-pointer"
                  style={{ borderColor: selected ? 'var(--accent)' : 'var(--border)', background: selected ? 'var(--bg-chat)' : 'transparent', color: 'var(--text-primary)' }}
                >{opt}</button>
              );
            })}
          </div>
        )}

        {q.type === 'true_false' && (
          <div className="flex gap-3">
            {['true', 'false'].map((val) => (
              <button key={val} onClick={() => handleAnswer(q.id, val, true)}
                className="flex-1 px-4 py-2.5 rounded-lg border text-sm cursor-pointer"
                style={{ borderColor: answers[q.id] === val ? 'var(--accent)' : 'var(--border)', background: answers[q.id] === val ? 'var(--bg-chat)' : 'transparent', color: 'var(--text-primary)' }}
              >{val === 'true' ? (lang === 'hu' ? 'Igaz' : 'True') : (lang === 'hu' ? 'Hamis' : 'False')}</button>
            ))}
          </div>
        )}

        {q.type === 'fill_blank' && (
          <input type="text" value={answers[q.id] || ''} onChange={(e) => handleAnswer(q.id, e.target.value)}
            placeholder={t.yourAnswer}
            className="w-full px-4 py-2.5 rounded-lg border text-sm outline-none"
            style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
          />
        )}

        {q.type === 'essay' && (
          <textarea value={answers[q.id] || ''} onChange={(e) => handleAnswer(q.id, e.target.value)}
            placeholder={t.essayPlaceholder} rows={6}
            className="w-full px-4 py-2.5 rounded-lg border text-sm outline-none resize-y"
            style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
          />
        )}
      </div>

      {/* Navigation */}
      <div className="px-4 py-3 border-t flex gap-2" style={{ borderColor: 'var(--border)' }}>
        <button onClick={() => setCurrentQ(Math.max(0, currentQ - 1))} disabled={currentQ === 0}
          className="px-4 py-2 rounded-lg border text-sm cursor-pointer disabled:opacity-30"
          style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}
        >{t.prev}</button>
        <div className="flex-1" />
        {currentQ < questions.length - 1 ? (
          <button onClick={() => setCurrentQ(currentQ + 1)}
            className="px-4 py-2 rounded-lg text-white text-sm cursor-pointer" style={{ background: 'var(--accent)' }}
          >{t.next}</button>
        ) : (
          <button onClick={submitAll}
            className="px-6 py-2 rounded-lg text-white text-sm font-medium cursor-pointer" style={{ background: 'var(--success)' }}
          >{t.submit}</button>
        )}
      </div>
    </div>
  );
}
