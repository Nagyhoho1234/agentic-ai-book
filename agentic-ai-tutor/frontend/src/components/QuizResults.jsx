import { useState } from 'react';

export default function QuizResults({ questions, results, lang, onJumpToAnswer, onClose }) {
  const [expanded, setExpanded] = useState(true);

  const t = lang === 'hu' ? {
    title: 'Teszt eredmenyek',
    close: 'Bezárás',
    correct: 'Helyes',
    incorrect: 'Helytelen',
    feedback: 'Visszajelzes',
    modelAnswer: 'Helyes valasz',
    score: 'Pontszam',
    jumpHint: 'Kattints egy kerdesre a valasz megkeresesehez a konyvben',
  } : {
    title: 'Quiz Results',
    close: 'Close',
    correct: 'Correct',
    incorrect: 'Incorrect',
    feedback: 'Feedback',
    modelAnswer: 'Correct answer',
    score: 'Score',
    jumpHint: 'Click a question to find the answer in the book',
  };

  if (!questions || questions.length === 0) return null;

  const total = questions.length;
  const mcqResults = questions.filter((q) => q.type !== 'essay').map((q) => results[q.id]);
  const essayResults = questions.filter((q) => q.type === 'essay').map((q) => results[q.id]);
  const correctCount = mcqResults.filter((r) => r?.correct).length;
  const essayScores = essayResults.filter((r) => r?.score != null).map((r) => r.score);
  const essayAvg = essayScores.length > 0 ? Math.round(essayScores.reduce((a, b) => a + b, 0) / essayScores.length) : null;
  const pct = total > 0 ? Math.round(((correctCount + (essayAvg || 0) / 100 * essayResults.length) / total) * 100) : 0;
  const pctColor = pct >= 70 ? 'var(--success)' : pct >= 40 ? 'var(--warning)' : 'var(--error)';

  return (
    <div className="border-t flex-shrink-0" style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', maxHeight: '40vh', overflow: 'hidden' }}>
      {/* Header bar */}
      <div
        className="flex items-center gap-3 px-4 py-2 cursor-pointer"
        onClick={() => setExpanded(!expanded)}
      >
        <span className="text-xs font-bold" style={{ color: pctColor }}>{pct}%</span>
        <span className="text-xs font-medium flex-1" style={{ color: 'var(--text-primary)' }}>
          {t.title} -- {correctCount}/{mcqResults.length}
          {essayAvg != null && ` | Essay: ${essayAvg}%`}
        </span>
        <span className="text-xs" style={{ color: 'var(--text-secondary)' }}>{expanded ? '\u25BC' : '\u25B2'}</span>
        <button
          onClick={(e) => { e.stopPropagation(); onClose(); }}
          className="text-xs px-2 py-0.5 rounded border cursor-pointer"
          style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}
        >{t.close}</button>
      </div>

      {/* Expandable results list */}
      {expanded && (
        <div className="px-4 pb-3 max-h-60 overflow-y-auto space-y-2">
          <p className="text-xs italic mb-2" style={{ color: 'var(--text-secondary)' }}>{t.jumpHint}</p>
          {questions.map((q) => {
            const r = results[q.id] || {};
            const isEssay = q.type === 'essay';
            return (
              <div
                key={q.id}
                className="rounded-lg border p-2 cursor-pointer transition-colors text-xs"
                style={{ borderColor: 'var(--border)' }}
                onClick={() => onJumpToAnswer(q)}
                onMouseOver={(e) => e.currentTarget.style.background = 'var(--bg-chat)'}
                onMouseOut={(e) => e.currentTarget.style.background = 'transparent'}
              >
                <div className="flex items-start gap-2">
                  <span className="font-bold flex-shrink-0" style={{ color: r.correct ? 'var(--success)' : 'var(--error)' }}>
                    {isEssay ? `${r.score || 0}%` : (r.correct ? '\u2714' : '\u2718')}
                  </span>
                  <p className="flex-1" style={{ color: 'var(--text-primary)' }}>{q.question}</p>
                  {q.chapter_num && (
                    <span className="px-1.5 py-0.5 rounded-full flex-shrink-0" style={{ color: 'var(--accent)', background: 'var(--bg-primary)' }}>
                      Ch{q.chapter_num} &#8599;
                    </span>
                  )}
                </div>
                {r.feedback && <p className="mt-1 pl-5" style={{ color: 'var(--text-secondary)' }}>{r.feedback}</p>}
                {!isEssay && !r.correct && r.correct_answer && (
                  <p className="mt-1 pl-5" style={{ color: 'var(--text-secondary)' }}>{t.modelAnswer}: {r.correct_answer}</p>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
