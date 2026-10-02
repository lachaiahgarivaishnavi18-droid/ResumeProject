def validate_result(data: dict) -> dict:
    issues = []
    if not data.get("product_candidates"):
        issues.append("No candidate products found")
    return {"decision": "PASS" if not issues else "RETRY", "confidence": 0.91, "issues": issues, "missing_evidence": []}
