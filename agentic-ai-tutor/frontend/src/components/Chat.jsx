import { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';

const AGENT_LABELS = {
  rag: 'Textbook',
  quiz: 'Quiz',
  socratic: 'Socratic',
  code_lab: 'Code Lab',
  navigate: 'Navigation',
  explain: 'Textbook',
  selection: 'About Selection',
  error: 'Error',
};

const AGENT_COLORS = {
  rag: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
  quiz: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200',
  socratic: 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200',
  code_lab: 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200',
  navigate: 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200',
  selection: 'bg-teal-100 text-teal-800 dark:bg-teal-900 dark:text-teal-200',
  explain: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
  error: 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200',
};

export default function Chat({ messages, loading, onSend, placeholder, welcomeTitle, welcomeText, welcomeSub }) {
  const [input, setInput] = useState('');
  const chatContainerRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    const el = chatContainerRef.current;
    if (el) el.scrollTop = el.scrollHeight;
  }, [messages, loading]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;
    onSend(input.trim());
    setInput('');
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages */}
      <div ref={chatContainerRef} className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="text-center py-16" style={{ color: 'var(--text-secondary)' }}>
            <div className="text-4xl mb-4">&#127806;</div>
            <h2 className="text-xl font-semibold mb-2" style={{ color: 'var(--text-primary)' }}>
              {welcomeTitle || 'PrecAgri-Tutor'}
            </h2>
            <p className="mb-2">{welcomeText || 'Ask me anything about precision agriculture!'}</p>
            <p className="text-sm mb-6">{welcomeSub || ''}</p>
            <div className="flex flex-wrap gap-2 justify-center max-w-lg mx-auto">
              {[
                'What is variable rate application?',
                'Test me on remote sensing',
                'Explain NDVI and crop health',
                'What topics does the book cover?',
              ].map((q) => (
                <button
                  key={q}
                  onClick={() => { setInput(q); inputRef.current?.focus(); }}
                  className="px-3 py-1.5 text-sm rounded-full border transition-colors cursor-pointer"
                  style={{
                    borderColor: 'var(--border)',
                    color: 'var(--text-secondary)',
                    background: 'var(--bg-secondary)',
                  }}
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                msg.role === 'user'
                  ? 'text-white'
                  : ''
              }`}
              style={{
                background: msg.role === 'user' ? 'var(--accent)' : 'var(--bg-chat)',
                color: msg.role === 'user' ? '#fff' : 'var(--text-primary)',
              }}
            >
              {msg.role === 'assistant' && msg.agent && (
                <span className={`inline-block text-xs px-2 py-0.5 rounded-full mb-2 ${AGENT_COLORS[msg.agent] || AGENT_COLORS.rag}`}>
                  {AGENT_LABELS[msg.agent] || msg.agent}
                </span>
              )}
              <div className="chat-markdown">
                <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>{msg.content}</ReactMarkdown>
              </div>
              {msg.sources && msg.sources.length > 0 && (
                <details className="mt-2 text-xs" style={{ color: 'var(--text-secondary)' }}>
                  <summary className="cursor-pointer">Sources ({msg.sources.length})</summary>
                  <ul className="mt-1 space-y-0.5">
                    {msg.sources.map((s, j) => (
                      <li key={j}>{s.chapter} (pp. {s.pages}) -- {(s.score * 100).toFixed(0)}%</li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start">
            <div className="rounded-2xl px-4 py-3" style={{ background: 'var(--bg-chat)' }}>
              <div className="flex space-x-1.5">
                <div className="w-2 h-2 rounded-full animate-bounce" style={{ background: 'var(--accent)', animationDelay: '0ms' }} />
                <div className="w-2 h-2 rounded-full animate-bounce" style={{ background: 'var(--accent)', animationDelay: '150ms' }} />
                <div className="w-2 h-2 rounded-full animate-bounce" style={{ background: 'var(--accent)', animationDelay: '300ms' }} />
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Input */}
      <form onSubmit={handleSubmit} className="p-4 border-t" style={{ borderColor: 'var(--border)' }}>
        <div className="flex gap-2">
          <input
            ref={inputRef}
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={placeholder || "Ask a question about precision agriculture..."}
            disabled={loading}
            className="flex-1 px-4 py-2.5 rounded-xl border outline-none transition-colors"
            style={{
              borderColor: 'var(--border)',
              background: 'var(--bg-secondary)',
              color: 'var(--text-primary)',
            }}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="px-6 py-2.5 rounded-xl text-white font-medium transition-colors disabled:opacity-50 cursor-pointer"
            style={{ background: 'var(--accent)' }}
          >
            Send
          </button>
        </div>
      </form>
    </div>
  );
}
