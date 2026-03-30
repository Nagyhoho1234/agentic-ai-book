import axios from 'axios';

const LLM_STORAGE_KEY = 'agenticai-tutor-llm';

const api = axios.create({
  baseURL: '/api',
  timeout: 120000,
});

// Inject per-user LLM settings as headers on every request
api.interceptors.request.use((config) => {
  try {
    const raw = localStorage.getItem(LLM_STORAGE_KEY);
    if (raw) {
      const s = JSON.parse(raw);
      if (s.provider) config.headers['X-LLM-Provider'] = s.provider;
      if (s.apiKey) config.headers['X-LLM-Key'] = s.apiKey;
      if (s.model) config.headers['X-LLM-Model'] = s.model;
      if (s.baseUrl) config.headers['X-LLM-BaseUrl'] = s.baseUrl;
    }
  } catch {}
  return config;
});

// Save/load LLM settings to/from localStorage (never server)
export function getLLMSettings() {
  try {
    return JSON.parse(localStorage.getItem(LLM_STORAGE_KEY)) || {};
  } catch { return {}; }
}

export function saveLLMSettings(settings) {
  localStorage.setItem(LLM_STORAGE_KEY, JSON.stringify(settings));
}

// --- Session management ---

export async function createSession() {
  const { data } = await api.post('/session');
  return data.session_id;
}

// --- Chat ---

export async function sendChat(message, sessionId) {
  const { data } = await api.post('/chat', {
    message,
    session_id: sessionId,
  });
  return data;
}

export async function sendMessage(message, studentId = 'default', chapterFilter = null) {
  const { data } = await api.post('/chat', {
    message,
    student_id: studentId,
    chapter_filter: chapterFilter,
  });
  return data;
}

export async function askAboutSelection(selectedText, question, chapterNum, sessionId) {
  const { data } = await api.post('/ask-about-selection', {
    selected_text: selectedText,
    question: question || 'Explain this',
    chapter_num: chapterNum,
    session_id: sessionId,
  });
  return data;
}

// --- Book content ---

export async function getChapterList(lang = 'en') {
  const { data } = await api.get(`/book/chapters?lang=${lang}`);
  return data;
}

export async function getChapter(chapterNum, lang = 'en') {
  const { data } = await api.get(`/book/chapter/${chapterNum}?lang=${lang}`);
  return data;
}

export async function searchBook(query) {
  const { data } = await api.get('/book/search', { params: { q: query } });
  return data;
}

export async function getChapterSummary(chapterNum) {
  const { data } = await api.post('/book/summary', { chapter_num: chapterNum });
  return data;
}

export async function getToc() {
  const { data } = await api.get('/toc');
  return data;
}

// --- Quiz ---

export async function generateQuiz(chapterNums, numQuestions = 5, sessionId = null, lang = 'en', questionTypes = null) {
  const { data } = await api.post('/quiz/generate', {
    chapter_nums: chapterNums,
    num_questions: numQuestions,
    session_id: sessionId,
    lang,
    question_types: questionTypes,
  });
  return data;
}

export async function evaluateQuiz(question, answer, sessionId) {
  const { data } = await api.post('/quiz/evaluate', {
    question,
    answer,
    session_id: sessionId,
  });
  return data;
}

export async function submitQuizAnswer(concept, correct, studentId = 'default') {
  const { data } = await api.post('/quiz/answer', {
    student_id: studentId,
    concept,
    correct,
  });
  return data;
}

// --- Concept graph ---

export async function getConceptGraph() {
  const { data } = await api.get('/concept-graph');
  return data;
}

export async function getConcepts() {
  const { data } = await api.get('/concepts');
  return data;
}

// --- Student progress ---

export async function getMastery(sessionId) {
  const { data } = await api.get(`/mastery/${sessionId}`);
  return data;
}

export async function getQuotaStatus() {
  const { data } = await api.get('/quota-status');
  return data;
}

export async function getCacheStats() {
  const { data } = await api.get('/cache-stats');
  return data;
}

// --- Settings ---

export async function getSettings() {
  const { data } = await api.get('/settings');
  return data;
}

export async function saveSettings(settingsData) {
  const { data } = await api.post('/settings', settingsData);
  return data;
}

export async function testConnection() {
  const { data } = await api.get('/settings/test');
  return data;
}

export async function listModels(provider = '', apiKey = '', baseUrl = '') {
  const headers = {};
  if (provider) headers['X-LLM-Provider'] = provider;
  if (apiKey) headers['X-LLM-Key'] = apiKey;
  if (baseUrl) headers['X-LLM-BaseUrl'] = baseUrl;
  const { data } = await api.get(`/settings/models?provider=${encodeURIComponent(provider)}`, { headers });
  return data;
}

// --- Health ---

export async function getHealth() {
  const { data } = await api.get('/health');
  return data;
}

export default api;
