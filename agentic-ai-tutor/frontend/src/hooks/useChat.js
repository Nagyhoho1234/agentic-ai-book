import { useState, useCallback } from 'react';
import { sendChat } from '../api/client';

export function useChat(sessionId) {
  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem('precagri-tutor-messages');
    return saved ? JSON.parse(saved) : [];
  });
  const [loading, setLoading] = useState(false);

  const saveMessages = (msgs) => {
    setMessages(msgs);
    localStorage.setItem('precagri-tutor-messages', JSON.stringify(msgs));
  };

  const send = useCallback(async (text) => {
    if (!sessionId || !text.trim()) return;

    const userMsg = { role: 'user', content: text, timestamp: new Date().toISOString() };
    const updated = [...messages, userMsg];
    saveMessages(updated);
    setLoading(true);

    try {
      const result = await sendChat(text, sessionId);
      const assistantMsg = {
        role: 'assistant',
        content: result.response || result.answer || '',
        agent: result.agent || result.intent || 'rag',
        sources: result.sources || [],
        quizData: result.quiz_data || null,
        exerciseData: result.exercise_data || null,
        model: result.model_used || '',
        timestamp: new Date().toISOString(),
      };
      saveMessages([...updated, assistantMsg]);
    } catch (err) {
      const errorMsg = {
        role: 'assistant',
        content: `Error: ${err.response?.data?.detail || err.message}`,
        agent: 'error',
        timestamp: new Date().toISOString(),
      };
      saveMessages([...updated, errorMsg]);
    } finally {
      setLoading(false);
    }
  }, [sessionId, messages]);

  const clearMessages = useCallback(() => {
    saveMessages([]);
  }, []);

  const addAssistantMessage = useCallback((msg) => {
    setMessages((prev) => {
      const updated = [...prev, msg];
      localStorage.setItem('precagri-tutor-messages', JSON.stringify(updated));
      return updated;
    });
  }, []);

  return { messages, loading, send, clearMessages, addAssistantMessage };
}
