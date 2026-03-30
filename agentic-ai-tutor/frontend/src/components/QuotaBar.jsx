import { useState, useEffect } from 'react';
import { getQuotaStatus } from '../api/client';

export default function QuotaBar() {
  const [quota, setQuota] = useState(null);

  useEffect(() => {
    const fetch = () => getQuotaStatus().then(setQuota).catch(() => {});
    fetch();
    const interval = setInterval(fetch, 30000);
    return () => clearInterval(interval);
  }, []);

  if (!quota) return null;

  const models = quota.models || {};
  const totalUsed = Object.values(models).reduce((s, m) => s + m.rpd_used, 0);
  const totalLimit = Object.values(models).reduce((s, m) => s + m.rpd_limit, 0);
  const pct = totalLimit > 0 ? (totalUsed / totalLimit) * 100 : 0;

  const color = pct > 80 ? 'var(--error)' : pct > 50 ? 'var(--warning)' : 'var(--success)';

  return (
    <div className="px-4 py-2 border-b text-xs flex items-center gap-3" style={{ borderColor: 'var(--border)' }}>
      <span style={{ color: 'var(--text-secondary)' }}>API Quota:</span>
      <div className="flex-1 h-1.5 rounded-full" style={{ background: 'var(--border)' }}>
        <div className="h-full rounded-full transition-all" style={{ width: `${pct}%`, background: color }} />
      </div>
      <span style={{ color: 'var(--text-secondary)' }}>{totalUsed}/{totalLimit}</span>
      {quota.all_exhausted && (
        <span className="text-xs font-medium" style={{ color: 'var(--error)' }}>EXHAUSTED</span>
      )}
    </div>
  );
}
