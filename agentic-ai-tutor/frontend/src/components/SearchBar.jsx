import { useState, useRef, useEffect, useCallback } from 'react';
import { searchBook } from '../api/client';

export default function SearchBar({ onResultClick, lang }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const timerRef = useRef(null);
  const inputRef = useRef(null);
  const wrapperRef = useRef(null);

  const t = lang === 'hu'
    ? { placeholder: 'Kereses a konyvben...', noResults: 'Nincs találat', searching: 'Keresés...' }
    : { placeholder: 'Search the book...', noResults: 'No results', searching: 'Searching...' };

  const doSearch = useCallback(async (q) => {
    if (!q || q.trim().length < 2) { setResults([]); return; }
    setLoading(true);
    try {
      const data = await searchBook(q.trim());
      setResults(data.results || []);
    } catch {
      setResults([]);
    } finally {
      setLoading(false);
    }
  }, []);

  // Debounced search
  useEffect(() => {
    if (timerRef.current) clearTimeout(timerRef.current);
    timerRef.current = setTimeout(() => doSearch(query), 300);
    return () => clearTimeout(timerRef.current);
  }, [query, doSearch]);

  // Focus input when opened
  useEffect(() => {
    if (open) setTimeout(() => inputRef.current?.focus(), 50);
  }, [open]);

  // Close on outside click
  useEffect(() => {
    if (!open) return;
    const handler = (e) => {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target)) {
        setOpen(false);
      }
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [open]);

  const handleKeyDown = (e) => {
    if (e.key === 'Escape') { setOpen(false); setQuery(''); setResults([]); }
  };

  const handleResultClick = (r) => {
    onResultClick?.(r.chapter_num, r.section, r.excerpt);
    setOpen(false);
    setQuery('');
    setResults([]);
  };

  return (
    <div ref={wrapperRef} className="relative">
      {!open && (
        <button
          onClick={() => setOpen(true)}
          className="px-2 py-1 text-sm cursor-pointer rounded-lg"
          style={{ color: 'var(--text-secondary)' }}
          title={t.placeholder}
        >
          &#128269;
        </button>
      )}

      {open && (
        <div className="flex items-center gap-2">
          <div className="relative">
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={t.placeholder}
              className="w-56 px-3 py-1 text-xs rounded-lg border outline-none"
              style={{ borderColor: 'var(--border)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
            <button
              onClick={() => { setOpen(false); setQuery(''); setResults([]); }}
              className="absolute right-1 top-1/2 -translate-y-1/2 text-xs cursor-pointer px-1"
              style={{ color: 'var(--text-secondary)' }}
            >&times;</button>
          </div>
        </div>
      )}

      {open && query.trim().length >= 2 && (
        <div
          className="absolute top-full right-0 mt-1 w-96 max-h-80 overflow-y-auto rounded-xl border shadow-xl z-[100]"
          style={{ background: 'var(--bg-primary)', borderColor: 'var(--border)', boxShadow: '0 8px 32px rgba(0,0,0,0.15)' }}
        >
          {loading && (
            <div className="p-3 text-xs text-center" style={{ color: 'var(--text-secondary)' }}>{t.searching}</div>
          )}
          {!loading && results.length === 0 && (
            <div className="p-3 text-xs text-center" style={{ color: 'var(--text-secondary)' }}>{t.noResults}</div>
          )}
          {!loading && results.map((r, i) => (
            <button
              key={i}
              onClick={() => handleResultClick(r)}
              className="w-full text-left px-3 py-2 border-b last:border-b-0 cursor-pointer hover:opacity-80 transition-opacity"
              style={{ borderColor: 'var(--border)', background: 'transparent' }}
              onMouseOver={(e) => { e.currentTarget.style.background = 'var(--bg-chat)'; }}
              onMouseOut={(e) => { e.currentTarget.style.background = 'transparent'; }}
            >
              <div className="flex items-center gap-2 mb-0.5">
                <span className="text-xs font-semibold" style={{ color: 'var(--accent)' }}>
                  {r.chapter_title}
                </span>
                {r.section && (
                  <span className="text-xs" style={{ color: 'var(--text-secondary)' }}>
                    &rsaquo; {r.section}
                  </span>
                )}
              </div>
              <p
                className="text-xs leading-relaxed"
                style={{ color: 'var(--text-primary)' }}
                dangerouslySetInnerHTML={{ __html: r.excerpt }}
              />
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
