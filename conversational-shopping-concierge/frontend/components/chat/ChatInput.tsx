'use client';

import { useState, type FormEvent } from 'react';

export function ChatInput({ disabled, onSend }: { disabled: boolean; onSend: (message: string) => Promise<void> }) {
  const [message, setMessage] = useState('');

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const content = message.trim();
    if (!content || disabled) return;
    setMessage('');
    await onSend(content);
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-3 border-t border-slate-800 p-4">
      <label htmlFor="chat-message" className="sr-only">Your shopping request</label>
      <input
        id="chat-message"
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        placeholder="e.g. A laptop for coding under ₹80,000"
        className="min-w-0 flex-1 rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-sm text-white outline-none focus:border-cyan-400"
      />
      <button disabled={disabled || !message.trim()} className="rounded-xl bg-cyan-400 px-4 py-3 text-sm font-semibold text-slate-950 disabled:cursor-not-allowed disabled:opacity-50">
        Send
      </button>
    </form>
  );
}
