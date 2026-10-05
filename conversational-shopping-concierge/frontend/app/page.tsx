import Link from 'next/link';

const highlights = [
  { title: 'Tell us what you need', detail: 'Describe your budget, use case, and must-have features in plain language.' },
  { title: 'Compare confident matches', detail: 'Explore recommendations grounded in the product catalog and availability.' },
  { title: 'Shop at your pace', detail: 'Review product details and keep a local cart as you decide.' },
];

export default function Home() {
  return (
    <main className="mx-auto max-w-6xl px-6 py-16 sm:py-24">
      <section className="rounded-3xl border border-slate-800 bg-gradient-to-br from-slate-900 via-slate-900 to-cyan-950/40 p-8 shadow-2xl sm:p-14">
        <p className="text-sm font-semibold uppercase tracking-[0.24em] text-cyan-300">AI shopping, made personal</p>
        <h1 className="mt-5 max-w-3xl text-4xl font-bold tracking-tight text-white sm:text-6xl">
          Find the right product without the guesswork.
        </h1>
        <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
          Get tailored suggestions for your budget and needs, with product details and stock information in one place.
        </p>
        <div className="mt-9 flex flex-wrap gap-3">
          <Link href="/chat" className="rounded-xl bg-cyan-400 px-5 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300">
            Chat with the concierge
          </Link>
          <Link href="/products" className="rounded-xl border border-slate-600 px-5 py-3 font-semibold text-white transition hover:border-cyan-300">
            Browse products
          </Link>
        </div>
      </section>

      <section className="grid gap-4 py-10 sm:grid-cols-3">
        {highlights.map((item, index) => (
          <article key={item.title} className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
            <p className="text-sm font-semibold text-cyan-300">0{index + 1}</p>
            <h2 className="mt-4 text-lg font-semibold text-white">{item.title}</h2>
            <p className="mt-2 leading-6 text-slate-400">{item.detail}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
