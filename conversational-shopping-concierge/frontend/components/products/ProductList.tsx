'use client';

import { ProductCard } from './ProductCard';
import type { Product } from '@/types/product';

export function ProductList({ products }: { products: Product[] }) {
  if (products.length === 0) {
    return <p className="rounded-xl border border-slate-800 bg-slate-900 p-6 text-slate-300">No products are available right now.</p>;
  }
  return (
    <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
      {products.map((product) => <ProductCard key={product.product_id} product={product} />)}
    </div>
  );
}
