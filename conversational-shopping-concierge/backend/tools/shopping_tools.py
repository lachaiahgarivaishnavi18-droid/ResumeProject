def add_to_cart(product_id: str, user_id: str) -> dict:
    return {"status": "success", "product_id": product_id, "user_id": user_id, "cart_id": "CART-1"}


def create_order(product_id: str, user_id: str) -> dict:
    return {"status": "success", "product_id": product_id, "user_id": user_id, "order_id": "ORD-1001"}


def cancel_order(order_id: str) -> dict:
    return {"status": "success", "order_id": order_id, "cancelled": True}
