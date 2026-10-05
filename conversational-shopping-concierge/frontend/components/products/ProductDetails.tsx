'use client';

import Link from 'next/link';
import { useCart } from '@/hooks/useCart';
import type { Product } from '@/types/product';

export function ProductDetails({ product }: { product: Product }) {
  const { addItem } = useCart();
  const specifications = Object.entries(product).filter(([key, value]) =>
    !['product_id', 'name', 'brand', 'category', 'price', 'currency', 'description', 'inventory', 'compatibility'].includes(key)
    && (typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean' || Array.isArray(value)));

  return (
    <main className="mx-auto max-w-5xl px-6 py-10">
      <Link href="/products" className="text-sm text-cyan-300 hover:text-cyan-200">← All products</Link>
      <div className="mt-6 grid gap-8 md:grid-cols-[1fr_1.2fr]">
        <div className="flex min-h-72 items-end rounded-3xl border border-slate-800 bg-gradient-to-br from-cyan-500/20 to-slate-900 p-6">
          <span className="rounded-full bg-slate-950/70 px-3 py-1 text-sm text-cyan-200">{product.category ?? 'Product'}</span>
        </div>
        <section>
          <p className="text-sm text-slate-400">{product.brand ?? product.product_id}</p>
          <h1 className="mt-2 text-3xl font-bold text-white">{product.name}</h1>
          <p className="mt-4 leading-7 text-slate-300">{product.description ?? 'Product information is available below.'}</p>
          <p className="mt-6 text-2xl font-bold text-white">₹{product.price.toLocaleString('en-IN')}</p>
          <p className="mt-2 text-sm text-slate-400">
            {product.inventory?.availability_status === 'IN_STOCK'
              ? `${product.inventory.quantity ?? 'Limited'} available`
              : 'Check availability before purchase'}
          </p>
          <button onClick={() => addItem(product)} className="mt-6 rounded-xl bg-cyan-400 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-300">
            Add to cart
          </button>
        </section>
      </div>
      {specifications.length > 0 && (
        <section className="mt-10 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-lg font-semibold text-white">Specifications</h2>
          <dl className="mt-4 grid gap-4 sm:grid-cols-2">
            {specifications.map(([key, value]) => (
              <div key={key}>
                <dt className="text-xs uppercase tracking-wide text-slate-400">{key.replaceAll('_', ' ')}</dt>
                <dd className="mt-1 text-slate-200">{Array.isArray(value) ? value.join(', ') : String(value)}</dd>
              </div>
            ))}
          </dl>
        </section>
      )}
    </main>
  );
}
