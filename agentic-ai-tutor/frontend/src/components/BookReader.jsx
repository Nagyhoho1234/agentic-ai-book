import { useState, useEffect, useRef, useCallback } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import remarkSupersub from 'remark-supersub';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';
import { getChapter, getChapterList, getChapterSummary } from '../api/client';

const SUMMARY_CACHE_PREFIX = 'agenticai-tutor-summary-';
const LS_LAST_CHAPTER = 'agenticai-tutor-last-chapter';
const LS_LAST_SCROLL = 'agenticai-tutor-last-scroll';

// Process React children to turn chapter references into clickable spans.
// Handles: "1. fejezet", "fejezet 3", "Chapter 6", "Ch. 3"
function processChapterRefs(children, onChapterChange) {
  if (!children) return children;
  if (typeof children === 'string') {
    const clickableRanges = [];

    // Match "N. fejezet" (Hungarian format)
    const fejezetRe = /(\d+)\.\s*fejezet/gi;
    let m;
    while ((m = fejezetRe.exec(children)) !== null) {
      const chapNum = parseInt(m[1], 10);
      if (chapNum >= 1 && chapNum <= 19) {
        clickableRanges.push({ start: m.index, end: m.index + m[0].length, chapNum });
      }
    }

    // Match "Chapter N" or "chapter N" (English fallback)
    const directRe = /[Cc]hapters?\s+(\d+)/g;
    while ((m = directRe.exec(children)) !== null) {
      const chapNum = parseInt(m[1], 10);
      if (chapNum >= 1 && chapNum <= 19) {
        const alreadyCovered = clickableRanges.some((r) => r.start <= m.index && r.end > m.index);
        if (!alreadyCovered) {
          clickableRanges.push({ start: m.index, end: m.index + m[0].length, chapNum });
        }
      }
    }

    // Match "Ch. N" or "Ch N"
    const chRe = /Ch\.?\s*(\d+)/g;
    while ((m = chRe.exec(children)) !== null) {
      const chapNum = parseInt(m[1], 10);
      if (chapNum < 1 || chapNum > 19) continue;
      const alreadyCovered = clickableRanges.some((r) => r.start <= m.index && r.end > m.index);
      if (!alreadyCovered) {
        clickableRanges.push({ start: m.index, end: m.index + m[0].length, chapNum });
      }
    }

    if (clickableRanges.length === 0) return children;

    clickableRanges.sort((a, b) => a.start - b.start);

    const deduped = [clickableRanges[0]];
    for (let i = 1; i < clickableRanges.length; i++) {
      const prev = deduped[deduped.length - 1];
      if (clickableRanges[i].start >= prev.end) {
        deduped.push(clickableRanges[i]);
      }
    }

    const parts = [];
    let lastIdx = 0;
    for (const range of deduped) {
      if (range.start > lastIdx) {
        parts.push(children.slice(lastIdx, range.start));
      }
      const text = children.slice(range.start, range.end);
      parts.push(
        <span
          key={`chref-${range.start}`}
          onClick={(e) => { e.stopPropagation(); onChapterChange(range.chapNum); }}
          style={{ color: 'var(--accent)', cursor: 'pointer', borderBottom: '1px dashed var(--accent)' }}
          onMouseEnter={(e) => { e.target.style.textDecoration = 'underline'; }}
          onMouseLeave={(e) => { e.target.style.textDecoration = 'none'; }}
          title={`Ugrás a ${range.chapNum}. fejezethez`}
        >
          {text}
        </span>
      );
      lastIdx = range.end;
    }
    if (lastIdx < children.length) parts.push(children.slice(lastIdx));
    return parts;
  }
  if (Array.isArray(children)) {
    return children.map((child, i) => {
      if (typeof child === 'string') return <span key={`cr-${i}`}>{processChapterRefs(child, onChapterChange)}</span>;
      return child;
    });
  }
  return children;
}

export default function BookReader({ chapterNum, onChapterChange, onAskAboutSelection, scrollToSectionId, highlightText, lang = 'en' }) {
  const [chapter, setChapter] = useState(null);
  const [chapterList, setChapterList] = useState([]);
  const [loading, setLoading] = useState(false);
  const [popup, setPopup] = useState(null);
  const [question, setQuestion] = useState('');
  const [tocOpen, setTocOpen] = useState(true);
  const [summaryOpen, setSummaryOpen] = useState(false);
  const [summaryText, setSummaryText] = useState(null);
  const [summaryLoading, setSummaryLoading] = useState(false);
  const contentRef = useRef(null);
  const popupRef = useRef(null);
  const chapterCache = useRef({});
  const restoredScroll = useRef(false);

  useEffect(() => {
    getChapterList(lang).then(setChapterList).catch(() => {});
  }, [lang]);

  // Clear cache when language changes
  const prevLangRef = useRef(lang);
  const restoreSectionRef = useRef(null);

  useEffect(() => {
    chapterCache.current = {};
  }, [lang]);

  useEffect(() => {
    if (chapterNum == null) return;

    // If only language changed (not chapter), capture current visible heading
    if (prevLangRef.current !== lang && contentRef.current) {
      const headings = contentRef.current.querySelectorAll('h2[id], h3[id]');
      const containerTop = contentRef.current.getBoundingClientRect().top;
      let closest = null;
      let closestDist = Infinity;
      headings.forEach((h) => {
        const dist = Math.abs(h.getBoundingClientRect().top - containerTop - 60);
        if (dist < closestDist) { closestDist = dist; closest = h.id; }
      });
      restoreSectionRef.current = closest;
    }
    prevLangRef.current = lang;

    const cacheKey = `${lang}-${chapterNum}`;
    if (chapterCache.current[cacheKey]) {
      setChapter(chapterCache.current[cacheKey]);
      return;
    }
    setLoading(true);
    getChapter(chapterNum, lang)
      .then((data) => {
        chapterCache.current[cacheKey] = data;
        setChapter(data);
      })
      .catch(() => setChapter(null))
      .finally(() => setLoading(false));
  }, [chapterNum, lang]);

  // After content loads from a language switch, scroll to the same section
  useEffect(() => {
    if (!restoreSectionRef.current || !chapter || !contentRef.current) return;
    const sectionId = restoreSectionRef.current;
    restoreSectionRef.current = null;
    requestAnimationFrame(() => {
      const container = contentRef.current;
      if (!container) return;
      const el = container.querySelector(`#${CSS.escape(sectionId)}`);
      if (el) {
        const elRect = el.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        const elTopInContainer = elRect.top - containerRect.top + container.scrollTop;
        const centered = elTopInContainer - container.clientHeight / 3;
        container.scrollTo({ top: Math.max(0, centered), behavior: 'auto' });
      }
    });
  }, [chapter]);

  // Restore scroll position once on initial load from localStorage
  useEffect(() => {
    if (restoredScroll.current || !chapter || !contentRef.current) return;
    restoredScroll.current = true;
    const savedPct = parseFloat(localStorage.getItem(LS_LAST_SCROLL));
    if (!isNaN(savedPct) && savedPct > 0) {
      requestAnimationFrame(() => {
        const container = contentRef.current;
        if (container) {
          const target = savedPct * (container.scrollHeight - container.clientHeight);
          container.scrollTo({ top: Math.max(0, target), behavior: 'auto' });
        }
      });
    }
  }, [chapter]);

  // Save last chapter to localStorage whenever it changes
  useEffect(() => {
    if (chapterNum != null) {
      localStorage.setItem(LS_LAST_CHAPTER, String(chapterNum));
    }
  }, [chapterNum]);

  // Save scroll position periodically
  useEffect(() => {
    const container = contentRef.current;
    if (!container || chapterNum == null) return;
    let ticking = false;
    const handleScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const pct = container.scrollHeight > container.clientHeight
          ? container.scrollTop / (container.scrollHeight - container.clientHeight)
          : 0;
        localStorage.setItem(LS_LAST_SCROLL, String(pct));
        ticking = false;
      });
    };
    container.addEventListener('scroll', handleScroll, { passive: true });
    return () => container.removeEventListener('scroll', handleScroll);
  }, [chapterNum, chapter]);

  // Reset summary when chapter changes
  useEffect(() => {
    contentRef.current?.scrollTo(0, 0);
    setPopup(null);
    setSummaryOpen(false);
    setSummaryText(null);
  }, [chapterNum]);

  // Scroll helper -- NEVER use scrollIntoView (it scrolls the whole page).
  const scrollToEl = useCallback((el) => {
    const container = contentRef.current;
    if (!container || !el) return;
    const elRect = el.getBoundingClientRect();
    const containerRect = container.getBoundingClientRect();
    const elTopInContainer = elRect.top - containerRect.top + container.scrollTop;
    const centered = elTopInContainer - container.clientHeight / 3;
    container.scrollTo({ top: Math.max(0, centered), behavior: 'smooth' });
  }, []);

  // Scroll to section when requested from sidebar
  useEffect(() => {
    if (!scrollToSectionId || !contentRef.current) return;
    const el = contentRef.current.querySelector(`#${CSS.escape(scrollToSectionId)}`);
    if (el) scrollToEl(el);
  }, [scrollToSectionId, scrollToEl]);

  // Highlight text and scroll to it (for quiz results)
  useEffect(() => {
    if (!contentRef.current) return;

    // Remove previous highlights
    contentRef.current.querySelectorAll('.quiz-highlight').forEach((el) => {
      el.classList.remove('quiz-highlight');
      el.style.background = '';
      el.style.borderLeft = '';
      el.style.paddingLeft = '';
      el.style.borderRadius = '';
    });

    if (!highlightText) return;

    // Extract meaningful keywords from the search text
    const stopWords = new Set(['the', 'and', 'of', 'in', 'to', 'for', 'is', 'on', 'with', 'which', 'that', 'this', 'are', 'was', 'from', 'have', 'been']);
    const keywords = highlightText
      .replace(/[?.,!;:()\u201c\u201d\u201e\u201d]/g, '')
      .split(/\s+/)
      .filter((w) => w.length > 3 && !stopWords.has(w.toLowerCase()))
      .slice(0, 8);

    if (keywords.length === 0) return;

    // Score each element by how many keywords it contains
    const paragraphs = contentRef.current.querySelectorAll('p, li, td');
    let bestEl = null;
    let bestScore = 0;

    paragraphs.forEach((el) => {
      const text = el.textContent.toLowerCase();
      let score = 0;
      for (const kw of keywords) {
        if (text.includes(kw.toLowerCase())) score++;
      }
      if (score > bestScore) {
        bestScore = score;
        bestEl = el;
      }
    });

    if (bestEl && bestScore >= 2) {
      bestEl.style.cssText += '; background: #fbbf2440; border-left: 3px solid #f59e0b; padding-left: 8px; border-radius: 4px;';
      bestEl.classList.add('quiz-highlight');
      scrollToEl(bestEl);
    } else if (keywords.length > 0) {
      const walker = document.createTreeWalker(contentRef.current, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) {
        const node = walker.currentNode;
        const text = node.textContent.toLowerCase();
        for (const kw of keywords) {
          if (text.includes(kw.toLowerCase())) {
            scrollToEl(node.parentElement);
            return;
          }
        }
      }
    }
  }, [highlightText, chapter]);

  // Summary handler -- check localStorage first, then fetch from API
  const handleSummaryToggle = useCallback(async () => {
    if (summaryOpen) {
      setSummaryOpen(false);
      return;
    }
    setSummaryOpen(true);

    const cacheKey = SUMMARY_CACHE_PREFIX + chapterNum;
    const cached = localStorage.getItem(cacheKey);
    if (cached) {
      setSummaryText(cached);
      return;
    }

    if (summaryText) return;

    setSummaryLoading(true);
    try {
      const result = await getChapterSummary(chapterNum);
      setSummaryText(result.summary);
      localStorage.setItem(cacheKey, result.summary);
    } catch (err) {
      setSummaryText('Failed to load summary.');
    } finally {
      setSummaryLoading(false);
    }
  }, [summaryOpen, chapterNum, summaryText]);

  // Use a portal-style fixed popup to avoid scroll/positioning issues
  const handleMouseUp = useCallback(() => {
    const sel = window.getSelection();
    const text = sel?.toString().trim();
    if (!text || text.length < 5) return;

    const range = sel.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    setPopup({
      left: Math.max(16, Math.min(rect.left + rect.width / 2 - 144, window.innerWidth - 304)),
      top: Math.min(rect.bottom + 8, window.innerHeight - 180),
      text,
    });
    setQuestion('');
  }, []);

  const handleAsk = () => {
    if (!popup) return;
    onAskAboutSelection(popup.text, question || 'Explain this', chapterNum);
    setPopup(null);
    window.getSelection()?.removeAllRanges();
  };

  const dismissPopup = useCallback(() => {
    setPopup(null);
    window.getSelection()?.removeAllRanges();
  }, []);

  // Dismiss popup on outside click
  useEffect(() => {
    if (!popup) return;
    const handler = (e) => {
      if (popupRef.current && !popupRef.current.contains(e.target)) {
        dismissPopup();
      }
    };
    const t = setTimeout(() => document.addEventListener('mousedown', handler), 100);
    return () => { clearTimeout(t); document.removeEventListener('mousedown', handler); };
  }, [popup, dismissPopup]);

  const scrollToHeading = (id) => {
    const el = contentRef.current?.querySelector(`#${CSS.escape(id)}`);
    if (el) scrollToEl(el);
  };

  const currentIdx = chapterList.findIndex((c) => c.chapter_num === chapterNum);
  const prevChapter = currentIdx > 0 ? chapterList[currentIdx - 1].chapter_num : null;
  const nextChapter = currentIdx < chapterList.length - 1 ? chapterList[currentIdx + 1].chapter_num : null;

  const toc = chapter?.toc || [];

  // Slugify matching the backend's _slugify exactly
  const slugify = (text) => {
    let s = text.toLowerCase();
    s = s.replace(/[^\p{L}\p{N}\s-]/gu, '');
    s = s.replace(/\s+/g, '-');
    return s.replace(/^-+|-+$/g, '').slice(0, 60);
  };

  const headingRenderer = ({ node, children, ...props }) => {
    const text = String(children);
    const id = slugify(text);
    const level = parseInt(node.tagName?.[1] || props.level || '2');
    const Tag = `h${level}`;
    const styles = {
      2: 'text-lg font-bold mt-8 mb-3',
      3: 'text-base font-semibold mt-6 mb-2',
      4: 'text-sm font-semibold mt-4 mb-1',
    };
    return <Tag id={id} className={styles[level] || styles[3]} style={{ color: 'var(--text-primary)' }}>{children}</Tag>;
  };

  if (chapterNum == null) {
    return (
      <div className="h-full flex flex-col items-center justify-center p-8" style={{ color: 'var(--text-secondary)' }}>
        <div className="text-4xl mb-4">&#128214;</div>
        <h2 className="text-lg font-semibold mb-2" style={{ color: 'var(--text-primary)' }}>Book Reader</h2>
        <p className="text-center mb-4">Click a chapter in the sidebar to start reading.</p>
        <p className="text-sm text-center">Select any text to ask questions about it.</p>
      </div>
    );
  }

  const summaryLabel = lang === 'hu' ? 'Összefoglaló' : 'Summary';

  return (
    <div className="h-full flex flex-col">
      {/* Chapter nav */}
      <div className="flex items-center gap-2 px-4 py-2 border-b" style={{ borderColor: 'var(--border)' }}>
        <button
          onClick={() => prevChapter != null && onChapterChange(prevChapter)}
          disabled={prevChapter == null}
          className="px-2 py-1 text-sm rounded cursor-pointer disabled:opacity-30"
          style={{ color: 'var(--text-secondary)' }}
        >&#9664;</button>
        <select
          value={chapterNum}
          onChange={(e) => onChapterChange(Number(e.target.value))}
          className="flex-1 text-sm px-2 py-1 rounded border cursor-pointer"
          style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
        >
          {chapterList.map((ch) => (
            <option key={ch.chapter_num} value={ch.chapter_num}>
              {ch.chapter_title || `Chapter ${ch.chapter_num}`}
            </option>
          ))}
        </select>
        <button
          onClick={handleSummaryToggle}
          className={`px-2 py-1 text-xs rounded-lg border cursor-pointer ${summaryOpen ? 'font-bold' : ''}`}
          style={{
            borderColor: summaryOpen ? 'var(--accent)' : 'var(--border)',
            color: summaryOpen ? 'var(--accent)' : 'var(--text-secondary)',
            background: summaryOpen ? 'var(--bg-chat)' : 'transparent',
          }}
        >{summaryLabel}</button>
        <button
          onClick={() => nextChapter != null && onChapterChange(nextChapter)}
          disabled={nextChapter == null}
          className="px-2 py-1 text-sm rounded cursor-pointer disabled:opacity-30"
          style={{ color: 'var(--text-secondary)' }}
        >&#9654;</button>
      </div>

      {/* Summary panel -- collapsible */}
      {summaryOpen && (
        <div
          className="border-b px-4 py-3 text-sm overflow-y-auto"
          style={{
            borderColor: 'var(--border)',
            background: 'var(--bg-secondary)',
            maxHeight: '220px',
          }}
        >
          {summaryLoading && (
            <div className="flex items-center gap-2" style={{ color: 'var(--text-secondary)' }}>
              <span className="inline-block w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
              {lang === 'hu' ? 'Osszefoglalo generalasa...' : 'Generating summary...'}
            </div>
          )}
          {!summaryLoading && summaryText && (
            <div className="chat-markdown" style={{ color: 'var(--text-primary)' }}>
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {summaryText}
              </ReactMarkdown>
            </div>
          )}
        </div>
      )}

      {/* Chapter content -- rendered markdown */}
      <div
        ref={contentRef}
        className="flex-1 overflow-y-auto p-6"
        onMouseUp={handleMouseUp}
        style={{ lineHeight: '1.8' }}
      >
        {loading && (
          <div className="flex items-center justify-center py-16" style={{ color: 'var(--text-secondary)' }}>
            Loading chapter...
          </div>
        )}

        {!loading && chapter && (
          <>
            <h1 className="text-xl font-bold mb-1" style={{ color: 'var(--text-primary)' }}>
              {chapter.chapter_title}
            </h1>
            <p className="text-xs mb-8" style={{ color: 'var(--text-secondary)' }}>
              {chapter.part}
            </p>
            <div className="chat-markdown text-sm" style={{ color: 'var(--text-primary)' }}>
              <ReactMarkdown
                remarkPlugins={[remarkGfm, remarkMath, remarkSupersub]}
                rehypePlugins={[rehypeRaw, rehypeKatex]}
                components={{
                  h2: headingRenderer,
                  h3: headingRenderer,
                  h4: headingRenderer,
                  table: ({ children }) => (
                    <div style={{ overflowX: 'auto', margin: '0.75em 0', maxWidth: '100%' }}>
                      <table style={{ minWidth: '400px' }}>{children}</table>
                    </div>
                  ),
                  p: ({ children }) => <p>{processChapterRefs(children, onChapterChange)}</p>,
                  li: ({ children, ordered, ...rest }) => <li>{processChapterRefs(children, onChapterChange)}</li>,
                  td: ({ children }) => <td>{processChapterRefs(children, onChapterChange)}</td>,
                  img: ({ src, alt }) => (
                    <figure className="my-4">
                      <img src={src} alt={alt || ''} className="max-w-full rounded" loading="lazy"
                        onError={(e) => { e.target.style.display = 'none'; }} />
                      {alt && <figcaption className="text-xs mt-1 italic" style={{ color: 'var(--text-secondary)' }}>{alt}</figcaption>}
                    </figure>
                  ),
                }}
              >
                {chapter.markdown}
              </ReactMarkdown>
            </div>
          </>
        )}
      </div>

      {/* Selection popup -- fixed position on viewport */}
      {popup && (
        <div
          ref={popupRef}
          className="fixed z-[9999] rounded-xl shadow-xl border p-3 w-72"
          style={{
            left: popup.left,
            top: popup.top,
            background: 'var(--bg-primary, #ffffff)',
            borderColor: 'var(--border)',
            boxShadow: '0 8px 32px rgba(0,0,0,0.25)',
            opacity: 1,
            backdropFilter: 'none',
          }}
        >
          <p className="text-xs mb-2 italic" style={{ color: 'var(--text-secondary)' }}>
            &ldquo;{popup.text.substring(0, 100)}{popup.text.length > 100 ? '...' : ''}&rdquo;
          </p>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter') handleAsk(); if (e.key === 'Escape') dismissPopup(); }}
            placeholder={lang === 'hu' ? 'Kerdezz errol... (Enter a kuldeshez)' : 'Ask about this... (Enter to send)'}
            autoFocus
            className="w-full px-2 py-1.5 text-sm rounded border mb-2 outline-none"
            style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
          />
          <div className="flex gap-2">
            <button onClick={handleAsk} className="flex-1 px-3 py-1.5 text-xs rounded-lg text-white cursor-pointer" style={{ background: 'var(--accent)' }}>
              {lang === 'hu' ? 'Kérdés' : 'Ask'}
            </button>
            <button onClick={dismissPopup} className="px-3 py-1.5 text-xs rounded-lg border cursor-pointer" style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}>
              {lang === 'hu' ? 'Mégse' : 'Cancel'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
