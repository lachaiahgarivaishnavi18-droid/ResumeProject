export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  recommendations?: string[];
}

export interface ChatResponse {
  workflow_id: string;
  session_id: string;
  status: string;
  response: string;
  sources: string[];
  recommendations: string[];
  requires_approval: boolean;
}
