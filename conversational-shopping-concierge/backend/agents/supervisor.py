def run_supervisor(query: str) -> dict:
    return {"intent": "shopping", "route": "search", "needs_rag": "monitor" in query.lower() or "warranty" in query.lower() or "return" in query.lower()}
