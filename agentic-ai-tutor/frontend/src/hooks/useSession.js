import { useState, useEffect, useCallback } from 'react';
import { createSession } from '../api/client';

export function useSession() {
  const [sessionId, setSessionId] = useState(() => {
    return localStorage.getItem('agenticai-tutor-session');
  });

  useEffect(() => {
    if (!sessionId) {
      createSession().then((id) => {
        setSessionId(id);
        localStorage.setItem('agenticai-tutor-session', id);
      });
    }
  }, [sessionId]);

  const resetSession = useCallback(async () => {
    const id = await createSession();
    setSessionId(id);
    localStorage.setItem('agenticai-tutor-session', id);
    return id;
  }, []);

  return { sessionId, resetSession };
}
