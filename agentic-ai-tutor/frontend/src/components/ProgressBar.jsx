import { useState, useEffect } from 'react';
import { getMastery } from '../api/client';

export default function ProgressBar({ sessionId }) {
  const [mastery, setMastery] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (!sessionId) return;
    getMastery(sessionId).then(setMastery).catch(() => {});
  }, [sessionId]);

  if (!mastery) return null;

  const overall = mastery.overall_mastery || 0;
  const topics = mastery.topics || [];
  const activeTopic = topics.filter((t) => t.attempts > 0);

  if (activeTopic.length === 0) return null;

  return (
    <div className="border-b" style={{ borderColor: 'var(--border)' }}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-4 py-2 text-xs flex items-center gap-3 cursor-pointer"
        style={{ color: 'var(--text-secondary)' }}
      >
        <span>Progress: {(overall * 100).toFixed(0)}%</span>
        <div className="flex-1 h-1.5 rounded-full" style={{ background: 'var(--border)' }}>
          <div
            className="h-full rounded-full transition-all"
            style={{ width: `${overall * 100}%`, background: 'var(--success)' }}
          />
        </div>
        <span>{isOpen ? '\u25B2' : '\u25BC'}</span>
      </button>

      {isOpen && (
        <div className="px-4 pb-3 space-y-1.5">
          {activeTopic.map((t) => (
            <div key={t.chapter_num} className="flex items-center gap-2 text-xs">
              <span className="w-6 text-right" style={{ color: 'var(--text-secondary)' }}>
                Ch{t.chapter_num}
              </span>
              <div className="flex-1 h-1.5 rounded-full" style={{ background: 'var(--border)' }}>
                <div
                  className="h-full rounded-full"
                  style={{
                    width: `${t.mastery * 100}%`,
                    background: t.mastery >= 0.7 ? 'var(--success)' : t.mastery >= 0.4 ? 'var(--warning)' : 'var(--error)',
                  }}
                />
              </div>
              <span className="w-16 truncate" style={{ color: 'var(--text-secondary)' }}>{t.name.split(':').pop()?.trim().substring(0, 15)}</span>
              <span style={{ color: 'var(--text-secondary)' }}>{t.correct}/{t.attempts}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
