'use client';

import Link from 'next/link';
import { useCart } from '@/hooks/useCart';
import type { Product } from '@/types/product';

export function ProductCard({ product }: { product: Product }) {
  const { addItem } = useCart();
  const inStock = product.inventory?.availability_status === 'IN_STOCK';

  return (
    <article className="flex flex-col rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <div className="mb-5 flex h-32 items-end rounded-xl bg-gradient-to-br from-cyan-500/20 via-sky-500/10 to-slate-950 p-4">
        <span className="rounded-full border border-cyan-400/30 bg-slate-950/70 px-3 py-1 text-xs text-cyan-200">
          {product.category ?? 'Featured'}
        </span>
      </div>
      <p className="text-sm text-slate-400">{product.brand ?? product.product_id}</p>
      <h2 className="mt-1 text-xl font-semibold text-white">{product.name}</h2>
      <p className="mt-2 line-clamp-2 min-h-12 text-sm leading-6 text-slate-400">
        {product.description ?? 'Explore product details and specifications.'}
      </p>
      <div className="mt-5 flex items-center justify-between">
        <span className="text-lg font-bold text-white">₹{product.price.toLocaleString('en-IN')}</span>
        <span className={inStock ? 'text-xs text-emerald-300' : 'text-xs text-amber-300'}>
          {inStock ? `${product.inventory?.quantity ?? ''} in stock` : 'Availability varies'}
        </span>
      </div>
      <div className="mt-5 grid grid-cols-2 gap-2">
        <Link href={`/products/${encodeURIComponent(product.product_id)}`} className="rounded-lg border border-slate-700 px-3 py-2 text-center text-sm transition hover:border-cyan-300">
          Details
        </Link>
        <button onClick={() => addItem(product)} className="rounded-lg bg-cyan-400 px-3 py-2 text-sm font-semibold text-slate-950 transition hover:bg-cyan-300">
          Add to cart
        </button>
      </div>
    </article>
  );
}
