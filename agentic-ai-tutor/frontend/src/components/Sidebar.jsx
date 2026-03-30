import { useState, useEffect, useRef } from 'react';
import { getChapterList, getChapter } from '../api/client';

export default function Sidebar({ onChapterOpen, onScrollToSection, activeChapter, isOpen, onToggle, isMobile, lang = 'en' }) {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedParts, setExpandedParts] = useState({});
  const [expandedChapters, setExpandedChapters] = useState({});
  const tocCache = useRef({});

  useEffect(() => {
    getChapterList(lang)
      .then(setChapters)
      .catch(() => setChapters([]))
      .finally(() => setLoading(false));
  }, [lang]);

  // Clear TOC cache when language changes
  useEffect(() => { tocCache.current = {}; }, [lang]);

  // Fetch TOC when a chapter is expanded
  const toggleChapterWithToc = (chNum) => {
    const wasExpanded = expandedChapters[chNum];
    setExpandedChapters((prev) => ({ ...prev, [chNum]: !prev[chNum] }));
    if (!wasExpanded && !tocCache.current[chNum]) {
      getChapter(chNum, lang).then((data) => {
        tocCache.current[chNum] = data.toc || [];
        setChapters((prev) => prev.map((ch) =>
          ch.chapter_num === chNum ? { ...ch, toc: data.toc || [] } : ch
        ));
      }).catch(() => {});
    }
  };

  // Group chapters by part
  const parts = [];
  const partMap = {};
  for (const ch of chapters) {
    const p = ch.part || 'Other';
    if (!(p in partMap)) {
      partMap[p] = { title: p, chapters: [] };
      parts.push(partMap[p]);
    }
    partMap[p].chapters.push(ch);
  }

  const togglePart = (idx) => setExpandedParts((prev) => ({ ...prev, [idx]: !prev[idx] }));

  return (
    <div
      className={`${isMobile
        ? `fixed inset-y-0 left-0 z-50 w-72 transition-transform duration-300 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`
        : `${isOpen ? 'w-72' : 'w-0'} transition-all duration-300 overflow-hidden`
      } border-r flex-shrink-0 select-none`}
      style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)' }}
    >
      <div className="w-72 h-full flex flex-col">
        <div className="p-4 border-b flex items-center justify-between" style={{ borderColor: 'var(--border)' }}>
          <h2 className="font-semibold text-sm uppercase tracking-wide" style={{ color: 'var(--text-secondary)' }}>
            {lang === 'hu' ? 'Fejezetek' : 'Chapters'}
          </h2>
          <button onClick={onToggle} className="text-lg cursor-pointer" style={{ color: 'var(--text-secondary)' }}>
            &times;
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-2">
          {loading && <p className="p-4 text-sm" style={{ color: 'var(--text-secondary)' }}>Loading...</p>}
          {parts.map((part, i) => (
            <div key={i} className="mb-1">
              {/* Part header */}
              <button
                onClick={() => togglePart(i)}
                className="w-full text-left px-3 py-2 text-xs font-bold uppercase tracking-wide rounded-lg cursor-pointer hover:opacity-80"
                style={{ color: 'var(--text-secondary)' }}
              >
                {expandedParts[i] ? '\u25BC' : '\u25B6'} {part.title}
              </button>

              {expandedParts[i] && (
                <div className="ml-2">
                  {part.chapters.map((ch) => {
                    const isActive = ch.chapter_num === activeChapter;
                    const isExpanded = expandedChapters[ch.chapter_num];
                    const subs = ch.toc || [];

                    // Filter to only level 2 sections
                    const sections = subs.filter((s) => s.level === 2);

                    return (
                      <div key={ch.chapter_num}>
                        {/* Chapter button */}
                        <div className="flex items-center">
                          {ch.chapter_num >= 1 && (
                            <button
                              onClick={() => toggleChapterWithToc(ch.chapter_num)}
                              className="px-1 text-xs cursor-pointer"
                              style={{ color: 'var(--text-secondary)' }}
                            >
                              {isExpanded ? '\u25BC' : '\u25B6'}
                            </button>
                          )}
                          <button
                            onClick={() => onChapterOpen?.(ch.chapter_num)}
                            className="flex-1 text-left px-2 py-1.5 text-sm rounded-lg cursor-pointer transition-colors"
                            style={{
                              color: isActive ? 'var(--accent)' : 'var(--text-primary)',
                              fontWeight: isActive ? '600' : '400',
                              background: isActive ? 'var(--bg-chat)' : 'transparent',
                            }}
                            onMouseOver={(e) => { if (!isActive) e.currentTarget.style.background = 'var(--bg-chat)'; }}
                            onMouseOut={(e) => { if (!isActive) e.currentTarget.style.background = 'transparent'; }}
                          >
                            {ch.chapter_title}
                          </button>
                        </div>

                        {/* Section list */}
                        {isExpanded && sections.length > 0 && (
                          <div className="ml-5 border-l" style={{ borderColor: 'var(--border)' }}>
                            {sections.map((sub, si) => (
                              <button
                                key={si}
                                onClick={() => {
                                  onChapterOpen?.(ch.chapter_num);
                                  setTimeout(() => onScrollToSection?.(sub.id), 200);
                                }}
                                className="block w-full text-left text-xs py-1 pl-2 cursor-pointer truncate hover:underline"
                                style={{ color: 'var(--text-secondary)' }}
                              >
                                {sub.text}
                              </button>
                            ))}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
