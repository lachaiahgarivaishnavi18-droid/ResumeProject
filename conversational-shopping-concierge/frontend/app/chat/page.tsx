import { ChatWindow } from '@/components/chat/ChatWindow';

export default function ChatPage() {
  return (
    <main className="mx-auto max-w-4xl px-6 py-10">
      <p className="text-sm font-semibold uppercase tracking-[0.2em] text-cyan-300">Personal shopping assistant</p>
      <h1 className="mt-2 text-3xl font-bold text-white">What are you looking for?</h1>
      <p className="mb-6 mt-3 text-slate-400">Include your budget, preferred brand, and how you plan to use it.</p>
      <ChatWindow />
    </main>
  );
}
