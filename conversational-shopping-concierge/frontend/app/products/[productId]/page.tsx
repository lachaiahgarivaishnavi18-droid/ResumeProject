'use client';

import { useParams } from 'next/navigation';
import { ProductDetails } from '@/components/products/ProductDetails';
import { useProducts } from '@/hooks/useProducts';

export default function ProductPage() {
  const params = useParams<{ productId: string }>();
  const { products, loading, error } = useProducts();
  const product = products.find((item) => item.product_id === params.productId);

  if (loading) return <main className="mx-auto max-w-5xl px-6 py-10 text-slate-400" role="status">Loading product…</main>;
  if (error) return <main className="mx-auto max-w-5xl px-6 py-10 text-rose-200" role="alert">{error}</main>;
  if (!product) return <main className="mx-auto max-w-5xl px-6 py-10 text-slate-300">Product not found.</main>;
  return <ProductDetails product={product} />;
}
