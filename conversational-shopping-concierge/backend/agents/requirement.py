import re


def parse_requirements(query: str) -> dict:
    lower = query.lower()
    budget = None
    match = re.search(r"(?:under|within|budget|upto|up to|below)\s*₹?\s?(\d{3,6})", query, re.IGNORECASE)
    if match:
        budget = float(match.group(1))
    requirements = {
        "category": "laptop" if "laptop" in lower else "monitor" if "monitor" in lower else "phone" if "phone" in lower else None,
        "budget": {"currency": "INR", "maximum": budget},
        "use_cases": ["gaming" if "gaming" in lower else "coding" if "coding" in lower else "travel" if "travel" in lower else "study" if "study" in lower else "general"],
        "requirements": {"ram": "16GB" if "16gb" in lower else "8GB" if "8gb" in lower else None},
        "compatibility_requirements": ["4K monitor"] if "4k" in lower else [],
        "missing_information": [],
        "confidence": 0.9,
    }
    return requirements
