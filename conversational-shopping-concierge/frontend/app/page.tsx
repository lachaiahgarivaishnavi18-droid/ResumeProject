'use client';

import { useMemo, useState } from 'react';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

const products = [
  { id: 'LAP001', name: 'AeroPro G14', brand: 'AeroPro', price: 74999, stock: 'In stock', tag: 'Gaming / coding' },
  { id: 'MON001', name: 'VisionMax 27U', brand: 'VisionMax', price: 24999, stock: 'In stock', tag: '4K compatible' },
  { id: 'PHN001', name: 'PixelLens M9', brand: 'PixelLens', price: 33999, stock: 'In stock', tag: 'Camera + battery' },
];

export default function Home() {
  const [query, setQuery] = useState('I need a gaming laptop under ₹80,000 with 16GB RAM.');
  const [result, setResult] = useState('Looking through the catalog and compatibility data.');

  const suggestions = useMemo(() => products, []);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setResult('Searching product catalog and checking available inventory...');

    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: 'session_001', user_id: 'user_001', message: query }),
      });
      const data = await response.json();
      setResult(data.response || 'No recommendations returned.');
    } catch (error) {
      setResult('The backend is unavailable. Please run the FastAPI service locally.');
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-slate-50">
      <div className="mx-auto max-w-7xl p-6">
        <header className="mb-8 flex items-center justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.25em] text-cyan-400">AI Commerce</p>
            <h1 className="mt-2 text-3xl font-bold">Conversational Shopping Concierge</h1>
          </div>
          <span className="rounded-full border border-cyan-500/40 bg-cyan-500/10 px-3 py-1 text-sm text-cyan-300">
            Workflow active
          </span>
        </header>

        <div className="grid gap-6 lg:grid-cols-[1.4fr_0.8fr]">
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-2xl">
            <form onSubmit={handleSubmit} className="space-y-4">
              <label className="block text-sm text-slate-300">Ask for a product</label>
              <textarea
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                className="h-28 w-full rounded-xl border border-slate-700 bg-slate-950 p-3 text-sm text-slate-100 outline-none ring-0"
              />
              <button type="submit" className="rounded-xl bg-cyan-500 px-5 py-3 font-medium text-slate-950 transition hover:bg-cyan-400">
                Search products
              </button>
            </form>

            <div className="mt-6 rounded-xl border border-slate-800 bg-slate-950 p-4">
              <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Assistant reply</p>
              <p className="mt-3 text-base text-slate-200">{result}</p>
            </div>
          </section>

          <aside className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-lg font-semibold">Workflow status</h2>
            <ul className="mt-5 space-y-3 text-sm text-slate-300">
              <li>Requirement Understanding</li>
              <li>Product Search</li>
              <li>Inventory</li>
              <li>Compatibility</li>
              <li>Knowledge Retrieval</li>
              <li>Recommendation</li>
              <li>Validation</li>
              <li>Response</li>
            </ul>
          </aside>
        </div>

        <section className="mt-8">
          <h2 className="mb-4 text-xl font-semibold">Recommended products</h2>
          <div className="grid gap-4 md:grid-cols-3">
            {suggestions.map((product) => (
              <article key={product.id} className="rounded-2xl border border-slate-800 bg-slate-900 p-4">
                <div className="mb-4 h-24 rounded-xl bg-gradient-to-br from-cyan-500/30 via-sky-500/10 to-slate-900" />
                <p className="text-xs uppercase tracking-[0.18em] text-cyan-300">{product.tag}</p>
                <h3 className="mt-2 text-xl font-semibold">{product.name}</h3>
                <p className="text-sm text-slate-400">{product.brand}</p>
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold">₹{product.price}</span>
                  <span className="text-xs text-emerald-400">{product.stock}</span>
                </div>
                <div className="mt-4 flex gap-2">
                  <button className="rounded-lg border border-slate-700 px-3 py-2 text-sm">View details</button>
                  <button className="rounded-lg bg-cyan-500 px-3 py-2 text-sm font-medium text-slate-950">Buy</button>
                </div>
              </article>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
