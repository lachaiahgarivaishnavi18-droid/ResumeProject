import type { ChatMessage } from '@/types/chat';

export function MessageBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === 'user';
  return (
    <article className={`max-w-[90%] rounded-2xl px-4 py-3 ${isUser ? 'ml-auto bg-cyan-500 text-slate-950' : 'border border-slate-800 bg-slate-900 text-slate-100'}`}>
      <p className="whitespace-pre-wrap leading-6">{message.content}</p>
      {message.recommendations && message.recommendations.length > 0 && (
        <ul className="mt-3 space-y-1 border-t border-slate-700/70 pt-3 text-sm">
          {message.recommendations.map((recommendation) => <li key={recommendation}>{recommendation}</li>)}
        </ul>
      )}
    </article>
  );
}
