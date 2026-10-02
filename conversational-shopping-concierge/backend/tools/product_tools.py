def search_products(category: str | None = None, max_price: float | None = None, brand: str | None = None) -> list[dict]:
    """Return mock product matches from the local catalog."""
    products = [
        {"product_id": "LAP001", "name": "AeroPro G14", "brand": "AeroPro", "category": "Laptop", "price": 74999},
        {"product_id": "MON001", "name": "VisionMax 27U", "brand": "VisionMax", "category": "Monitor", "price": 24999},
        {"product_id": "PHN001", "name": "PixelLens M9", "brand": "PixelLens", "category": "Smartphone", "price": 33999},
    ]
    return [p for p in products if (not category or p["category"].lower() == category.lower()) and (not max_price or p["price"] <= max_price) and (not brand or p["brand"].lower() == brand.lower())]


def get_product(product_id: str) -> dict:
    catalog = {"LAP001": {"product_id": "LAP001", "name": "AeroPro G14", "brand": "AeroPro", "category": "Laptop", "price": 74999}, "MON001": {"product_id": "MON001", "name": "VisionMax 27U", "brand": "VisionMax", "category": "Monitor", "price": 24999}, "PHN001": {"product_id": "PHN001", "name": "PixelLens M9", "brand": "PixelLens", "category": "Smartphone", "price": 33999}}
    return catalog.get(product_id, {"product_id": product_id, "status": "not_found"})
