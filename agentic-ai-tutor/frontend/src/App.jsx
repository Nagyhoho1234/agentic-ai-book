import { useState, useEffect } from 'react';
import Chat from './components/Chat';
import Sidebar from './components/Sidebar';
import BookReader from './components/BookReader';
import QuizPanel from './components/QuizPanel';
import QuizResults from './components/QuizResults';
import ConceptMap from './components/ConceptMap';
import SearchBar from './components/SearchBar';
import Flashcards from './components/Flashcards';
import Settings from './components/Settings';
import ProgressBar from './components/ProgressBar';
import QuotaBar from './components/QuotaBar';
import ErrorBoundary from './components/ErrorBoundary';
import { useSession } from './hooks/useSession';
import { useChat } from './hooks/useChat';
import { useMobile } from './hooks/useMobile';
import { askAboutSelection } from './api/client';

const STRINGS = {
  hu: {
    title: 'Ágentikus AI Kutatóknak — Interaktív Tutor',
    readBook: 'Könyv',
    quiz: 'Teszt',
    cards: 'Kártyák',
    conceptMap: 'Térkép',
    newSession: 'Új munkamenet',
    askPlaceholder: 'Kérdezz az AI tudományos alkalmazásairól...',
    welcome: 'Üdvözöllek!',
    welcomeText: 'Kérdezz bármit az AI tudományos alkalmazásairól!',
    welcomeSub: 'A válaszok a tankönyvből származnak, mesterséges intelligenciával kiegészítve.',
    settings: 'Beállítások',
  },
  en: {
    title: 'Ágentikus AI Kutatóknak — Interaktív Tutor',
    readBook: 'Könyv',
    quiz: 'Teszt',
    cards: 'Kártyák',
    conceptMap: 'Térkép',
    newSession: 'Új munkamenet',
    askPlaceholder: 'Kérdezz az AI tudományos alkalmazásairól...',
    welcome: 'Ágentikus AI Tutor',
    welcomeText: 'Kérdezz bármit az AI tudományos alkalmazásairól!',
    welcomeSub: 'A válaszok a tankönyvből származnak, mesterséges intelligenciával kiegészítve.',
    settings: 'Beállítások',
  },
};

function App() {
  const { sessionId, resetSession } = useSession();
  const { messages, loading, send, clearMessages, addAssistantMessage } = useChat(sessionId);
  const isMobile = useMobile();
  const [sidebarOpen, setSidebarOpen] = useState(!isMobile);
  const [readerOpen, setReaderOpen] = useState(false);
  const [quizOpen, setQuizOpen] = useState(false);
  const [cardsOpen, setCardsOpen] = useState(false);
  const [mapOpen, setMapOpen] = useState(false);
  const [currentChapter, setCurrentChapter] = useState(null);
  const [scrollToSectionId, setScrollToSectionId] = useState(null);
  const [highlightText, setHighlightText] = useState(null);
  const [selectionLoading, setSelectionLoading] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [quizResultsData, setQuizResultsData] = useState(null);
  const [dark, setDark] = useState(() => {
    return localStorage.getItem('agenticai-tutor-dark') === 'true' ||
      window.matchMedia('(prefers-color-scheme: dark)').matches;
  });
  const [lang, setLang] = useState(() => localStorage.getItem('agenticai-tutor-lang') || 'en');
  const toggleLang = () => {
    const n = lang === 'hu' ? 'en' : 'hu';
    setLang(n);
    localStorage.setItem('agenticai-tutor-lang', n);
  };
  const t = STRINGS[lang];

  // Restore last-read chapter from localStorage on mount, default to chapter 1
  useEffect(() => {
    const saved = localStorage.getItem('agenticai-tutor-last-chapter');
    if (!readerOpen && currentChapter == null) {
      const num = saved != null ? parseInt(saved, 10) : 1;
      if (!isNaN(num)) {
        setCurrentChapter(num);
        setReaderOpen(true);
      }
    }
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const toggleDark = () => {
    const n = !dark;
    setDark(n);
    localStorage.setItem('agenticai-tutor-dark', String(n));
  };

  const handleChapterOpen = (chapterNum) => {
    setCurrentChapter(chapterNum);
    setReaderOpen(true);
    setQuizOpen(false);
    setCardsOpen(false);
    setMapOpen(false);
    setScrollToSectionId(null);
    setHighlightText(null);
  };

  const handleScrollToSection = (sectionId) => {
    setScrollToSectionId(sectionId);
    setTimeout(() => setScrollToSectionId(null), 500);
  };

  const handleAskAboutSelection = async (selectedText, question, chapterNum) => {
    const userContent = `> ${selectedText.substring(0, 300)}${selectedText.length > 300 ? '...' : ''}\n\n${question}`;
    addAssistantMessage({ role: 'user', content: userContent, quotedText: selectedText, timestamp: new Date().toISOString() });
    setSelectionLoading(true);
    try {
      const result = await askAboutSelection(selectedText, question, chapterNum, sessionId);
      addAssistantMessage({ role: 'assistant', content: result.answer, agent: 'selection', sources: result.sources || [], model: result.model_used, timestamp: new Date().toISOString() });
    } catch (err) {
      addAssistantMessage({ role: 'assistant', content: `Error: ${err.response?.data?.detail || err.message}`, agent: 'error', timestamp: new Date().toISOString() });
    } finally {
      setSelectionLoading(false);
    }
  };

  // Quiz results callback
  const handleQuizResults = (questions, results) => {
    setQuizResultsData({ questions, results });
  };

  // Jump to answer in book from quiz results
  const handleJumpToAnswer = (question) => {
    const chNum = question.chapter_num;
    if (!chNum) return;

    const needsChapterChange = currentChapter !== chNum || !readerOpen;
    setCurrentChapter(chNum);
    setReaderOpen(true);
    setQuizOpen(false);
    setCardsOpen(false);

    const searchText = question.question;
    const delay = needsChapterChange ? 800 : 100;
    setHighlightText(null);
    setTimeout(() => setHighlightText(searchText), delay);
  };

  const handleNewSession = async () => {
    clearMessages();
    await resetSession();
  };

  const handleChapterOpenMobile = (chapterNum) => {
    handleChapterOpen(chapterNum);
    if (isMobile) setSidebarOpen(false);
  };

  // Search result click -- open chapter in reader and highlight the match
  const handleSearchResultClick = (chapterNum, section, excerpt) => {
    const needsChapterChange = currentChapter !== chapterNum || !readerOpen;
    setCurrentChapter(chapterNum);
    setReaderOpen(true);
    setQuizOpen(false);
    setCardsOpen(false);

    const plainExcerpt = excerpt.replace(/<\/?mark>/g, '');
    const delay = needsChapterChange ? 800 : 100;
    setHighlightText(null);
    setTimeout(() => setHighlightText(plainExcerpt), delay);
  };

  const leftPanelOpen = readerOpen || quizOpen || cardsOpen || mapOpen;

  return (
    <div className={`${dark ? 'dark' : ''} h-screen overflow-hidden`}>
      <div className="flex h-full" style={{ background: 'var(--bg-primary)', color: 'var(--text-primary)' }}>
        {isMobile && sidebarOpen && (
          <div
            className="fixed inset-0 z-40 bg-black/40"
            onClick={() => setSidebarOpen(false)}
          />
        )}
        <Sidebar
          onChapterOpen={handleChapterOpenMobile}
          onScrollToSection={(id) => { handleScrollToSection(id); if (isMobile) setSidebarOpen(false); }}
          activeChapter={currentChapter}
          isOpen={sidebarOpen}
          onToggle={() => setSidebarOpen(!sidebarOpen)}
          isMobile={isMobile}
          lang={lang}
        />

        <div className="flex-1 flex flex-col min-w-0">
          {/* QuotaBar -- shows API usage across the top */}
          <QuotaBar />

          <header className="flex items-center gap-1.5 md:gap-3 px-2 md:px-4 py-2 border-b flex-wrap" style={{ borderColor: 'var(--border)' }}>
            {!sidebarOpen && (
              <button onClick={() => setSidebarOpen(true)} className="text-xl cursor-pointer" style={{ color: 'var(--text-secondary)' }}>&#9776;</button>
            )}
            <h1 className="text-sm md:text-base font-bold flex-1 truncate" style={{ color: 'var(--text-primary)' }}>
              {t.title}
            </h1>
            <SearchBar onResultClick={handleSearchResultClick} lang={lang} />
            <button
              onClick={() => { setReaderOpen(!readerOpen); if (!readerOpen) { setQuizOpen(false); setCardsOpen(false); setMapOpen(false); } }}
              className={`px-2 md:px-3 py-1 text-xs rounded-lg border cursor-pointer ${readerOpen ? 'font-bold' : ''}`}
              style={{ borderColor: readerOpen ? 'var(--accent)' : 'var(--border)', color: readerOpen ? 'var(--accent)' : 'var(--text-secondary)', background: readerOpen ? 'var(--bg-chat)' : 'transparent' }}
            >{t.readBook}</button>
            <button
              onClick={() => { setQuizOpen(!quizOpen); if (!quizOpen) { setReaderOpen(false); setCardsOpen(false); setMapOpen(false); } }}
              className={`px-2 md:px-3 py-1 text-xs rounded-lg border cursor-pointer ${quizOpen ? 'font-bold' : ''}`}
              style={{ borderColor: quizOpen ? 'var(--accent)' : 'var(--border)', color: quizOpen ? 'var(--accent)' : 'var(--text-secondary)', background: quizOpen ? 'var(--bg-chat)' : 'transparent' }}
            >{t.quiz}</button>
            <button
              onClick={() => { setCardsOpen(!cardsOpen); if (!cardsOpen) { setReaderOpen(false); setQuizOpen(false); setMapOpen(false); } }}
              className={`px-2 md:px-3 py-1 text-xs rounded-lg border cursor-pointer ${cardsOpen ? 'font-bold' : ''}`}
              style={{ borderColor: cardsOpen ? 'var(--accent)' : 'var(--border)', color: cardsOpen ? 'var(--accent)' : 'var(--text-secondary)', background: cardsOpen ? 'var(--bg-chat)' : 'transparent' }}
            >{t.cards}</button>
            <button
              onClick={() => { setMapOpen(!mapOpen); if (!mapOpen) { setReaderOpen(false); setQuizOpen(false); setCardsOpen(false); } }}
              className={`px-2 md:px-3 py-1 text-xs rounded-lg border cursor-pointer ${mapOpen ? 'font-bold' : ''}`}
              style={{ borderColor: mapOpen ? 'var(--accent)' : 'var(--border)', color: mapOpen ? 'var(--accent)' : 'var(--text-secondary)', background: mapOpen ? 'var(--bg-chat)' : 'transparent' }}
            >{t.conceptMap}</button>
            <button onClick={handleNewSession} className="px-2 md:px-3 py-1 text-xs rounded-lg border cursor-pointer hidden md:inline-block" style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}>{t.newSession}</button>
            <button onClick={toggleLang} className="px-2 py-1 text-xs font-medium cursor-pointer rounded-lg border" style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}>{lang === 'hu' ? 'EN' : 'HU'}</button>
            <button onClick={toggleDark} className="px-2 py-1 text-sm cursor-pointer rounded-lg" style={{ color: 'var(--text-secondary)' }}>{dark ? '\u2600' : '\u263E'}</button>
            <button onClick={() => setSettingsOpen(true)} className="px-2 py-1 text-sm cursor-pointer rounded-lg" style={{ color: 'var(--text-secondary)' }} title={t.settings}>&#9881;</button>
          </header>

          {/* ProgressBar -- shows mastery under the header */}
          <ProgressBar sessionId={sessionId} />

          <div className={`flex-1 min-h-0 flex ${isMobile ? 'flex-col' : 'flex-row'}`}>
            {/* Book Reader with quiz results at bottom */}
            {readerOpen && (
              <div className={`${isMobile ? 'flex-1 min-h-0' : 'flex-1 min-w-0 border-r'} flex flex-col`} style={{ borderColor: 'var(--border)' }}>
                <div className="flex-1 min-h-0">
                  <ErrorBoundary>
                    <BookReader
                      chapterNum={currentChapter}
                      onChapterChange={setCurrentChapter}
                      onAskAboutSelection={handleAskAboutSelection}
                      scrollToSectionId={scrollToSectionId}
                      highlightText={highlightText}
                      lang={lang}
                    />
                  </ErrorBoundary>
                </div>
                {quizResultsData && quizResultsData.questions?.length > 0 && (
                  <QuizResults
                    questions={quizResultsData.questions}
                    results={quizResultsData.results}
                    lang={lang}
                    onJumpToAnswer={handleJumpToAnswer}
                    onClose={() => { setQuizResultsData(null); setHighlightText(null); }}
                  />
                )}
              </div>
            )}

            {/* Quiz panel */}
            {quizOpen && (
              <div className={`${isMobile ? 'flex-1 min-h-0' : 'flex-1 min-w-0 border-r'}`} style={{ borderColor: 'var(--border)' }}>
                <ErrorBoundary>
                  <QuizPanel
                    sessionId={sessionId}
                    lang={lang}
                    onQuizResults={handleQuizResults}
                    onShowResults={() => {
                      if (quizResultsData?.questions?.length > 0) {
                        const firstCh = quizResultsData.questions.find((q) => q.chapter_num)?.chapter_num;
                        if (firstCh) setCurrentChapter(firstCh);
                      }
                      setReaderOpen(true);
                      setQuizOpen(false);
                    }}
                  />
                </ErrorBoundary>
              </div>
            )}

            {/* Flashcards panel */}
            {cardsOpen && (
              <div className={`${isMobile ? 'flex-1 min-h-0' : 'flex-1 min-w-0 border-r'}`} style={{ borderColor: 'var(--border)' }}>
                <ErrorBoundary>
                  <Flashcards
                    sessionId={sessionId}
                    lang={lang}
                  />
                </ErrorBoundary>
              </div>
            )}

            {/* Concept Map panel */}
            {mapOpen && (
              <div className={`${isMobile ? 'flex-1 min-h-0' : 'flex-1 min-w-0 border-r'}`} style={{ borderColor: 'var(--border)' }}>
                <ErrorBoundary>
                  <ConceptMap onChapterOpen={handleChapterOpen} lang={lang} />
                </ErrorBoundary>
              </div>
            )}

            {/* Chat -- hidden on mobile when a panel is open */}
            {(!isMobile || !leftPanelOpen) && (
              <div className={`${(!isMobile && leftPanelOpen) ? 'w-[420px] flex-shrink-0' : 'flex-1'} min-w-0`}>
                <ErrorBoundary>
                  <Chat
                    messages={messages}
                    loading={loading || selectionLoading}
                    onSend={send}
                    placeholder={t.askPlaceholder}
                    welcomeTitle={t.welcome}
                    welcomeText={t.welcomeText}
                    welcomeSub={t.welcomeSub}
                  />
                </ErrorBoundary>
              </div>
            )}
          </div>
        </div>
      </div>
      <Settings isOpen={settingsOpen} onClose={() => setSettingsOpen(false)} lang={lang} />
    </div>
  );
}

export default App;
