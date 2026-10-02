def check_compatibility(product_id: str, target: str = "4K monitor") -> dict:
    if product_id == "LAP001":
        return {
            "product_id": product_id,
            "compatible": True,
            "confidence": 0.93,
            "evidence": ["HDMI 2.1 supported", "DisplayPort via USB-C"],
            "sources": ["compatibility_manual.pdf#display"],
        }
    return {"product_id": product_id, "compatible": False, "confidence": 0.0, "evidence": ["No evidence found"], "sources": []}
