'use client';

import { useState } from 'react';
import { sendChatMessage } from '@/lib/api';
import type { ChatMessage } from '@/types/chat';

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome',
      role: 'assistant',
      content: 'Hi! Tell me what you are shopping for, your budget, and any features that matter most.',
    },
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function sendMessage(content: string) {
    const trimmed = content.trim();
    if (!trimmed || loading) return;
    setError(null);
    setMessages((current) => [...current, { id: crypto.randomUUID(), role: 'user', content: trimmed }]);
    setLoading(true);
    try {
      const result = await sendChatMessage(trimmed);
      setMessages((current) => [
        ...current,
        {
          id: result.workflow_id,
          role: 'assistant',
          content: result.response,
          recommendations: result.recommendations,
        },
      ]);
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : 'Unable to reach the shopping assistant.');
    } finally {
      setLoading(false);
    }
  }

  return { messages, loading, error, sendMessage };
}
