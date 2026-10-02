def generate_recommendation(products: list[dict], inventory: list[dict]) -> list[dict]:
    result = []
    for product in products:
        match = next((item for item in inventory if item["product_id"] == product["product_id"]), None)
        result.append({
            "product_id": product["product_id"],
            "name": product["name"],
            "price": product["price"],
            "reason": "Matches budget and compatibility requirements.",
            "available": bool(match and match.get("available")),
        })
    return result
