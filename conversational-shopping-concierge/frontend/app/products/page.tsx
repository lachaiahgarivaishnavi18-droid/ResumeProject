'use client';

import { ProductList } from '@/components/products/ProductList';
import { useProducts } from '@/hooks/useProducts';

export default function ProductsPage() {
  const { products, loading, error } = useProducts();
  return (
    <main className="mx-auto max-w-6xl px-6 py-10">
      <p className="text-sm font-semibold uppercase tracking-[0.2em] text-cyan-300">Catalog</p>
      <h1 className="mt-2 text-3xl font-bold text-white">Browse products</h1>
      <p className="mt-3 text-slate-400">Compare products, check availability, and add items to your cart.</p>
      <div className="mt-8">
        {loading ? <p className="text-slate-400" role="status">Loading products…</p>
          : error ? <p className="rounded-xl border border-rose-900 bg-rose-950/60 p-4 text-rose-200" role="alert">{error}</p>
            : <ProductList products={products} />}
      </div>
    </main>
  );
}
