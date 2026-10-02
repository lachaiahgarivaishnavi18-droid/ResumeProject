def route_after_validation(state: dict) -> str:
    decision = state.get("validation_result", {}).get("decision", "PASS")
    return "response" if decision == "PASS" else "product_search"
