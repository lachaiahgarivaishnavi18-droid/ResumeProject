'use client';

import Link from 'next/link';
import { CartSummary } from '@/components/cart/CartSummary';
import { useCart } from '@/hooks/useCart';

export default function CartPage() {
  const { items, total, setQuantity, removeItem } = useCart();
  return (
    <main className="mx-auto max-w-6xl px-6 py-10">
      <h1 className="text-3xl font-bold text-white">Your cart</h1>
      {items.length === 0 ? (
        <div className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-8 text-center">
          <p className="text-slate-300">Your cart is empty.</p>
          <Link href="/products" className="mt-5 inline-block rounded-xl bg-cyan-400 px-5 py-3 font-semibold text-slate-950">Browse products</Link>
        </div>
      ) : (
        <div className="mt-8 grid items-start gap-6 lg:grid-cols-[1fr_320px]">
          <section className="space-y-3">
            {items.map(({ product, quantity }) => (
              <article key={product.product_id} className="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-slate-800 bg-slate-900 p-5">
                <div>
                  <h2 className="font-semibold text-white">{product.name}</h2>
                  <p className="mt-1 text-sm text-slate-400">₹{product.price.toLocaleString('en-IN')} each</p>
                </div>
                <div className="flex items-center gap-3">
                  <label htmlFor={`quantity-${product.product_id}`} className="text-sm text-slate-400">Qty</label>
                  <input
                    id={`quantity-${product.product_id}`}
                    type="number"
                    min="1"
                    value={quantity}
                    onChange={(event) => {
                      const value = Number(event.target.value);
                      if (Number.isInteger(value) && value > 0) setQuantity(product.product_id, value);
                    }}
                    className="w-20 rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white"
                  />
                  <button onClick={() => removeItem(product.product_id)} className="text-sm text-rose-300 hover:text-rose-200">Remove</button>
                </div>
              </article>
            ))}
          </section>
          <CartSummary items={items} total={total} />
        </div>
      )}
    </main>
  );
}
