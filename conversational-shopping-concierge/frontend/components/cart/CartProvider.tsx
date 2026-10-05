'use client';

import { createContext, useEffect, useState, type ReactNode } from 'react';
import type { CartItem } from '@/types/cart';
import type { Product } from '@/types/product';

const CART_STORAGE_KEY = 'shopping-concierge-cart';

export interface CartContextValue {
  items: CartItem[];
  addItem: (product: Product) => void;
  setQuantity: (productId: string, quantity: number) => void;
  removeItem: (productId: string) => void;
  itemCount: number;
  total: number;
}

export const CartContext = createContext<CartContextValue | null>(null);

function isCartItem(value: unknown): value is CartItem {
  if (!value || typeof value !== 'object') return false;
  const item = value as Partial<CartItem>;
  return !!item.product && typeof item.product === 'object'
    && typeof item.product.product_id === 'string'
    && typeof item.product.name === 'string'
    && typeof item.product.price === 'number'
    && typeof item.quantity === 'number'
    && Number.isInteger(item.quantity)
    && item.quantity > 0;
}

function readCart(): CartItem[] {
  const saved = window.localStorage.getItem(CART_STORAGE_KEY);
  if (!saved) return [];
  try {
    const parsed: unknown = JSON.parse(saved);
    return Array.isArray(parsed) ? parsed.filter(isCartItem) : [];
  } catch {
    return [];
  }
}

export function CartProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<CartItem[]>([]);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setItems(readCart());
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (hydrated) window.localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(items));
  }, [hydrated, items]);

  function addItem(product: Product) {
    setItems((current) => {
      const existing = current.find((item) => item.product.product_id === product.product_id);
      if (existing) {
        return current.map((item) => item.product.product_id === product.product_id
          ? { ...item, quantity: item.quantity + 1 }
          : item);
      }
      return [...current, { product, quantity: 1 }];
    });
  }

  function setQuantity(productId: string, quantity: number) {
    if (!Number.isInteger(quantity) || quantity < 1) return;
    setItems((current) => current.map((item) => item.product.product_id === productId ? { ...item, quantity } : item));
  }

  function removeItem(productId: string) {
    setItems((current) => current.filter((item) => item.product.product_id !== productId));
  }

  const value: CartContextValue = {
    items,
    addItem,
    setQuantity,
    removeItem,
    itemCount: items.reduce((count, item) => count + item.quantity, 0),
    total: items.reduce((sum, item) => sum + item.product.price * item.quantity, 0),
  };

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}
