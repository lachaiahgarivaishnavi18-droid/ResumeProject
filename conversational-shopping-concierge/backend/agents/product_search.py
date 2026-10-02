def search_products(category: str | None = None, max_price: float | None = None) -> list[dict]:
    products = [
        {"product_id": "LAP001", "name": "AeroPro G14", "brand": "AeroPro", "price": 74999, "category": "Laptop", "ram": "16GB"},
        {"product_id": "MON001", "name": "VisionMax 27U", "brand": "VisionMax", "price": 24999, "category": "Monitor", "resolution": "4K"},
    ]
    return [p for p in products if (category is None or p["category"].lower() == category.lower()) and (max_price is None or p["price"] <= max_price)]
