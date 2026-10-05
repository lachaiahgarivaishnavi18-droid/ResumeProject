import './globals.css';
import Link from 'next/link';
import { CartProvider } from '@/components/cart/CartProvider';

export const metadata = {
  title: 'Conversational Shopping Concierge',
  description: 'Find products that match your needs with a conversational shopping assistant.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="border-b border-slate-800 bg-slate-950/90">
          <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4" aria-label="Main navigation">
            <Link href="/" className="font-semibold tracking-tight text-white">
              <span className="text-cyan-300">Shop</span> Concierge
            </Link>
            <div className="flex items-center gap-5 text-sm text-slate-300">
              <Link href="/products" className="transition hover:text-cyan-300">Products</Link>
              <Link href="/chat" className="transition hover:text-cyan-300">Chat</Link>
              <Link href="/cart" className="transition hover:text-cyan-300">Cart</Link>
            </div>
          </nav>
        </header>
        <CartProvider>{children}</CartProvider>
      </body>
    </html>
  );
}
