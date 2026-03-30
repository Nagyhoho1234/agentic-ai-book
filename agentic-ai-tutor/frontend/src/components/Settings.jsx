import { useState, useEffect } from 'react';
import { testConnection, listModels, getLLMSettings, saveLLMSettings } from '../api/client';

const STRINGS = {
  title: 'LLM Settings',
  provider: 'Provider',
  apiKey: 'API Key',
  baseUrl: 'Server URL',
  model: 'Model',
  save: 'Save',
  test: 'Test Connection',
  close: 'Close',
  saving: 'Saving...',
  testing: 'Testing...',
  saved: 'Saved!',
  connected: 'Connected',
  disconnected: 'Disconnected',
  testOk: 'Connection OK',
  testFail: 'Connection failed',
  noKeyNeeded: 'No API key needed',
  providerHints: {
    openai: 'OpenAI API -- requires OPENAI_API_KEY',
    gemini: 'Google Gemini -- requires GEMINI_API_KEY',
    ollama: 'Local Ollama server (default: localhost:11434)',
    lmstudio: 'Local LM Studio server (default: localhost:1234)',
    groq: 'Groq cloud -- requires GROQ_API_KEY',
    anthropic: 'Anthropic Claude -- requires ANTHROPIC_API_KEY',
  },
};

const PROVIDERS = ['openai', 'gemini', 'anthropic', 'ollama', 'lmstudio', 'groq'];

const PROVIDER_LABELS = {
  openai: 'OpenAI',
  gemini: 'Google Gemini',
  anthropic: 'Anthropic Claude',
  ollama: 'Ollama (local)',
  lmstudio: 'LM Studio (local)',
  groq: 'Groq',
};

const PROVIDER_FIELDS = {
  openai: { hasKey: true, keyField: 'openai_api_key', hasUrl: false, hasModel: true, modelField: 'openai_model_medium', defaultModels: ['gpt-4-turbo', 'gpt-4o', 'gpt-4o-mini', 'gpt-3.5-turbo'] },
  gemini: { hasKey: true, keyField: 'gemini_api_key', hasUrl: false, hasModel: true, modelField: 'gemini_model', defaultModels: ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.5-flash-lite'] },
  anthropic: { hasKey: true, keyField: 'anthropic_api_key', hasUrl: false, hasModel: true, modelField: 'anthropic_model', defaultModels: ['claude-sonnet-4-20250514', 'claude-haiku-4-5-20251001', 'claude-opus-4-20250514'] },
  ollama: { hasKey: false, hasUrl: true, urlField: 'ollama_base_url', hasModel: true, modelField: 'ollama_model', defaultModels: ['llama3.1', 'qwen2.5', 'mistral', 'codellama', 'gemma2'] },
  lmstudio: { hasKey: false, hasUrl: true, urlField: 'lmstudio_base_url', hasModel: true, modelField: 'lmstudio_model', defaultModels: ['default'] },
  groq: { hasKey: true, keyField: 'groq_api_key', hasUrl: false, hasModel: true, modelField: 'groq_model', defaultModels: ['llama-3.3-70b-versatile', 'mixtral-8x7b-32768', 'llama-3.1-8b-instant'] },
};

export default function Settings({ isOpen, onClose }) {
  const t = STRINGS;
  const [config, setConfig] = useState(null);
  const [form, setForm] = useState({});
  const [saving, setSaving] = useState(false);
  const [testing, setTesting] = useState(false);
  const [message, setMessage] = useState(null);
  const [availableModels, setAvailableModels] = useState([]);
  const [loadingModels, setLoadingModels] = useState(false);

  const fetchModels = (prov, key = '', url = '') => {
    setLoadingModels(true);
    setAvailableModels([]);
    const saved = getLLMSettings();
    const effectiveKey = key || (saved.provider === prov ? saved.apiKey : '') || '';
    const effectiveUrl = url || (saved.provider === prov ? saved.baseUrl : '') || '';
    listModels(prov, effectiveKey, effectiveUrl).then((res) => {
      setAvailableModels(res.models || []);
    }).catch(() => setAvailableModels([])).finally(() => setLoadingModels(false));
  };

  useEffect(() => {
    if (isOpen) {
      const saved = getLLMSettings();
      const prov = saved.provider || 'openai';
      setForm({
        llm_provider: prov,
        openai_api_key: prov === 'openai' ? (saved.apiKey || '') : '',
        gemini_api_key: prov === 'gemini' ? (saved.apiKey || '') : '',
        anthropic_api_key: prov === 'anthropic' ? (saved.apiKey || '') : '',
        groq_api_key: prov === 'groq' ? (saved.apiKey || '') : '',
        ollama_base_url: saved.baseUrl || 'http://localhost:11434/v1',
        ollama_model: prov === 'ollama' ? (saved.model || 'llama3.1') : 'llama3.1',
        lmstudio_base_url: saved.baseUrl || 'http://localhost:1234/v1',
        lmstudio_model: prov === 'lmstudio' ? (saved.model || 'default') : 'default',
        groq_model: prov === 'groq' ? (saved.model || 'llama-3.3-70b-versatile') : 'llama-3.3-70b-versatile',
        anthropic_model: prov === 'anthropic' ? (saved.model || 'claude-sonnet-4-20250514') : 'claude-sonnet-4-20250514',
        openai_model_medium: prov === 'openai' ? (saved.model || 'gpt-4-turbo') : 'gpt-4-turbo',
        gemini_model: prov === 'gemini' ? (saved.model || 'gemini-2.5-flash') : 'gemini-2.5-flash',
      });
      setConfig(saved);
      setMessage(null);
      fetchModels(prov);
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const provider = form.llm_provider || 'openai';
  const fields = PROVIDER_FIELDS[provider] || PROVIDER_FIELDS.openai;

  const handleChange = (key, value) => {
    setForm((prev) => ({ ...prev, [key]: value }));
    setMessage(null);
  };

  const handleSave = async () => {
    setSaving(true);
    setMessage(null);
    try {
      const prov = form.llm_provider;
      const apiKey = fields.hasKey ? (form[fields.keyField] || '') : '';
      const model = fields.hasModel ? (form[fields.modelField] || '') : '';
      const baseUrl = fields.hasUrl ? (form[fields.urlField] || '') : '';

      saveLLMSettings({ provider: prov, apiKey, model, baseUrl });
      setMessage({ type: 'ok', text: t.saved });
    } catch (err) {
      const detail = err.response?.data?.detail || err.message;
      setMessage({ type: 'error', text: detail });
    } finally {
      setSaving(false);
    }
  };

  const handleTest = async () => {
    setTesting(true);
    setMessage(null);
    try {
      const prov = form.llm_provider;
      const apiKey = fields.hasKey ? (form[fields.keyField] || '') : '';
      const model = fields.hasModel ? (form[fields.modelField] || '') : '';
      const baseUrl = fields.hasUrl ? (form[fields.urlField] || '') : '';
      saveLLMSettings({ provider: prov, apiKey, model, baseUrl });

      const result = await testConnection();
      if (result.status === 'ok') {
        setMessage({ type: 'ok', text: `${t.testOk}: ${result.model} -- "${result.response}"` });
      } else {
        setMessage({ type: 'error', text: `${t.testFail}: ${result.error}` });
      }
    } catch (err) {
      setMessage({ type: 'error', text: `${t.testFail}: ${err.message}` });
    } finally {
      setTesting(false);
    }
  };

  const inputStyle = {
    background: 'var(--bg-chat)',
    color: 'var(--text-primary)',
    borderColor: 'var(--border)',
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ background: 'rgba(0,0,0,0.5)' }}>
      <div className="w-full max-w-lg rounded-xl shadow-2xl p-6 mx-4" style={{ background: 'var(--bg-primary)', color: 'var(--text-primary)' }}>
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <h2 className="text-lg font-bold">{t.title}</h2>
          <button onClick={onClose} className="text-xl cursor-pointer px-2" style={{ color: 'var(--text-secondary)' }}>&times;</button>
        </div>

        {/* Status indicator */}
        {(() => {
          const saved = getLLMSettings();
          const hasKey = saved.apiKey || ['ollama', 'lmstudio'].includes(saved.provider);
          return (
            <div className="flex items-center gap-2 mb-4 text-xs" style={{ color: 'var(--text-secondary)' }}>
              <span className={`inline-block w-2 h-2 rounded-full ${hasKey ? 'bg-green-500' : 'bg-yellow-500'}`}></span>
              <span>{hasKey ? t.connected : 'No API key set'}</span>
              <span className="ml-auto font-mono">{saved.provider || 'none'}</span>
            </div>
          );
        })()}

        {/* Provider selector */}
        <div className="mb-4">
          <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-secondary)' }}>{t.provider}</label>
          <select
            value={provider}
            onChange={(e) => {
              const newProv = e.target.value;
              handleChange('llm_provider', newProv);
              const pf = PROVIDER_FIELDS[newProv] || {};
              const key = pf.hasKey ? (form[pf.keyField] || '') : '';
              const url = pf.hasUrl ? (form[pf.urlField] || '') : '';
              fetchModels(newProv, key, url);
            }}
            className="w-full px-3 py-2 rounded-lg border text-sm"
            style={inputStyle}
          >
            {PROVIDERS.map((p) => (
              <option key={p} value={p}>{PROVIDER_LABELS[p]}</option>
            ))}
          </select>
          <p className="text-xs mt-1" style={{ color: 'var(--text-secondary)' }}>{t.providerHints[provider]}</p>
        </div>

        {/* API Key */}
        {fields.hasKey && (
          <div className="mb-4">
            <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-secondary)' }}>{t.apiKey}</label>
            <input
              type="password"
              value={form[fields.keyField] || ''}
              onChange={(e) => handleChange(fields.keyField, e.target.value)}
              placeholder={config?.[fields.keyField] || 'sk-...'}
              className="w-full px-3 py-2 rounded-lg border text-sm font-mono"
              style={inputStyle}
            />
          </div>
        )}

        {!fields.hasKey && (
          <div className="mb-4 text-xs px-3 py-2 rounded-lg" style={{ background: 'var(--bg-chat)', color: 'var(--text-secondary)' }}>
            {t.noKeyNeeded}
          </div>
        )}

        {/* Base URL */}
        {fields.hasUrl && (
          <div className="mb-4">
            <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-secondary)' }}>{t.baseUrl}</label>
            <input
              type="text"
              value={form[fields.urlField] || ''}
              onChange={(e) => handleChange(fields.urlField, e.target.value)}
              onBlur={() => fetchModels(provider, '', form[fields.urlField])}
              className="w-full px-3 py-2 rounded-lg border text-sm font-mono"
              style={inputStyle}
            />
          </div>
        )}

        {/* Model selector */}
        {fields.hasModel && (
          <div className="mb-4">
            <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-secondary)' }}>
              {t.model}
              {loadingModels && <span className="ml-2 inline-block w-3 h-3 border-2 border-current border-t-transparent rounded-full animate-spin" />}
            </label>
            <select
              value={form[fields.modelField] || ''}
              onChange={(e) => handleChange(fields.modelField, e.target.value)}
              className="w-full px-3 py-2 rounded-lg border text-sm font-mono"
              style={inputStyle}
            >
              {form[fields.modelField] && !availableModels.includes(form[fields.modelField]) && (
                <option value={form[fields.modelField]}>{form[fields.modelField]}</option>
              )}
              {availableModels.map((m) => (
                <option key={m} value={m}>{m}</option>
              ))}
              {availableModels.length === 0 && !loadingModels && (
                <option value="" disabled>Could not load models</option>
              )}
            </select>
          </div>
        )}

        {/* Message */}
        {message && (
          <div className={`mb-4 text-xs px-3 py-2 rounded-lg ${message.type === 'ok' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' : 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'}`}>
            {message.text}
          </div>
        )}

        {/* Buttons */}
        <div className="flex gap-3">
          <button
            onClick={handleTest}
            disabled={testing}
            className="flex-1 px-4 py-2 text-sm rounded-lg border cursor-pointer disabled:opacity-50"
            style={{ borderColor: 'var(--border)', color: 'var(--text-secondary)' }}
          >
            {testing ? t.testing : t.test}
          </button>
          <button
            onClick={handleSave}
            disabled={saving}
            className="flex-1 px-4 py-2 text-sm rounded-lg font-medium cursor-pointer disabled:opacity-50"
            style={{ background: 'var(--accent)', color: '#fff' }}
          >
            {saving ? t.saving : t.save}
          </button>
        </div>
      </div>
    </div>
  );
}
