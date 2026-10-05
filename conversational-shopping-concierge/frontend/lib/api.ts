import type { ChatResponse } from '@/types/chat';
import type { Product } from '@/types/product';

async function readError(response: Response): Promise<string> {
  const body: unknown = await response.json().catch(() => null);
  if (body && typeof body === 'object' && 'detail' in body && typeof body.detail === 'string') {
    return body.detail;
  }
  return `Request failed with status ${response.status}.`;
}

export async function getProducts(): Promise<Product[]> {
  const response = await fetch('/api/products', { cache: 'no-store' });
  if (!response.ok) {
    throw new Error(await readError(response));
  }
  return response.json() as Promise<Product[]>;
}

export async function sendChatMessage(message: string): Promise<ChatResponse> {
  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id: 'shopping-session', user_id: 'guest', message }),
  });
  if (!response.ok) {
    throw new Error(await readError(response));
  }
  return response.json() as Promise<ChatResponse>;
}
