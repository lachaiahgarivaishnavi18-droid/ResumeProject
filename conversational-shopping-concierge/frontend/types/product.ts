export interface Product {
  product_id: string;
  name: string;
  brand?: string;
  category?: string;
  price: number;
  currency?: string;
  description?: string;
  inventory?: {
    quantity?: number;
    availability_status?: string;
    warehouse?: string;
  };
  [specification: string]: unknown;
}
