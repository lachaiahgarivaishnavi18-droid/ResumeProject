def check_inventory(product_id: str) -> dict:
    data = {
        "LAP001": {"product_id": "LAP001", "available": True, "quantity": 15, "warehouse": "BLR01"},
        "MON001": {"product_id": "MON001", "available": True, "quantity": 12, "warehouse": "BLR02"},
    }
    return data.get(product_id, {"product_id": product_id, "available": False, "quantity": 0, "warehouse": "UNKNOWN"})
