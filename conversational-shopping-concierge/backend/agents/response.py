def build_response(product: dict, sources: list[str]) -> str:
    return f"I recommend {product.get('name', 'the product')} at ₹{product.get('price', 0)}. Sources: {', '.join(sources) if sources else 'product catalog'}"
