'use client';

import { useEffect, useRef } from 'react';
import { useChat } from '@/hooks/useChat';
import { ChatInput } from './ChatInput';
import { MessageBubble } from './MessageBubble';
import { TypingIndicator } from './TypingIndicator';

export function ChatWindow() {
  const { messages, loading, error, sendMessage } = useChat();
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  return (
    <section className="flex h-[min(70vh,720px)] min-h-[480px] flex-col overflow-hidden rounded-2xl border border-slate-800 bg-slate-950">
      <div className="flex-1 space-y-4 overflow-y-auto p-5" aria-live="polite">
        {messages.map((message) => <MessageBubble key={message.id} message={message} />)}
        {loading && <TypingIndicator />}
        {error && <p className="rounded-lg border border-rose-900 bg-rose-950/60 p-3 text-sm text-rose-200" role="alert">{error}</p>}
        <div ref={bottomRef} />
      </div>
      <ChatInput disabled={loading} onSend={sendMessage} />
    </section>
  );
}
