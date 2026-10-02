def check_inventory(product_id: str) -> dict:
    inventory = {
        "LAP001": {"product_id": "LAP001", "available": True, "quantity": 15, "warehouse": "BLR01"},
        "MON001": {"product_id": "MON001", "available": True, "quantity": 12, "warehouse": "BLR02"},
        "PHN001": {"product_id": "PHN001", "available": True, "quantity": 44, "warehouse": "MUM01"},
    }
    return inventory.get(product_id, {"product_id": product_id, "available": False, "quantity": 0, "warehouse": "UNKNOWN"})


def get_inventory(product_id: str) -> dict:
    return check_inventory(product_id)
