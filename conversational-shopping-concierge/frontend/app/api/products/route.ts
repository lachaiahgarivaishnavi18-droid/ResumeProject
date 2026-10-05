import { NextResponse } from 'next/server';

const backendUrl = process.env.API_URL ?? process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function GET() {
  try {
    const response = await fetch(`${backendUrl}/api/products`, { cache: 'no-store' });
    const body = await response.text();
    return new Response(body, {
      status: response.status,
      headers: { 'Content-Type': response.headers.get('Content-Type') ?? 'application/json' },
    });
  } catch {
    return NextResponse.json({ detail: 'The product service is unavailable. Start the backend and try again.' }, { status: 502 });
  }
}
