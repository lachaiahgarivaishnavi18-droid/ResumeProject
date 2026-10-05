import type { CartItem } from '@/types/cart';

export function CartSummary({ items, total }: { items: CartItem[]; total: number }) {
  return (
    <aside className="h-fit rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-lg font-semibold text-white">Order summary</h2>
      <div className="mt-4 flex justify-between text-sm text-slate-400">
        <span>Items ({items.reduce((count, item) => count + item.quantity, 0)})</span>
        <span>₹{total.toLocaleString('en-IN')}</span>
      </div>
      <div className="mt-4 border-t border-slate-800 pt-4">
        <div className="flex justify-between font-semibold text-white">
          <span>Subtotal</span>
          <span>₹{total.toLocaleString('en-IN')}</span>
        </div>
        <p className="mt-3 text-xs leading-5 text-slate-500">This demo does not process payments. Your cart is saved in this browser.</p>
      </div>
    </aside>
  );
}
