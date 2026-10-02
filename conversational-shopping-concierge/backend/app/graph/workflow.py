from __future__ import annotations

import re
from typing import Any

from langgraph.graph import END, StateGraph

from app.data.products import PRODUCTS
from app.graph.state import AgentState


def parse_requirements(text: str) -> dict[str, Any]:
    lowered = text.lower()
    category = "laptop" if "laptop" in lowered else "monitor" if "monitor" in lowered else "smartphone" if "phone" in lowered else None
    budget_match = re.search(r"(?:under|within|budget|max|upto|up to|below)\s*₹?\s?(\d{3,6})", text, re.IGNORECASE)
    budget = float(budget_match.group(1)) if budget_match else None
    use_cases = []
    if "gaming" in lowered:
        use_cases.append("gaming")
    if "coding" in lowered:
        use_cases.append("coding")
    if "travel" in lowered:
        use_cases.append("travel")
    if "study" in lowered:
        use_cases.append("study")
    requirements = {"ram": "16GB" if "16gb" in lowered or "16 gb" in lowered else None}
    if "4k" in lowered:
        requirements["resolution"] = "4K"
    return {
        "category": category,
        "budget": {"currency": "INR", "maximum": budget},
        "use_cases": use_cases,
        "requirements": {k: v for k, v in requirements.items() if v is not None},
        "confidence": 0.88,
        "missing_information": [],
    }


def requirement_understanding_node(state: AgentState) -> AgentState:
    state["shopping_requirements"] = parse_requirements(state["user_query"])
    state["intent"] = "shopping"
    state["status"] = "requirements_parsed"
    return state


def product_search_node(state: AgentState) -> AgentState:
    requirements = state.get("shopping_requirements", {})
    category = requirements.get("category")
    max_budget = (requirements.get("budget") or {}).get("maximum")
    candidates = []
    for product in PRODUCTS:
        if category and product["category"].lower() != category:
            continue
        if max_budget and product["price"] > max_budget:
            continue
        candidates.append(product)
    state["product_candidates"] = candidates[:5]
    state["status"] = "products_found"
    return state


def inventory_node(state: AgentState) -> AgentState:
    results = []
    for product in state.get("product_candidates", []):
        inventory = product.get("inventory", {})
        results.append({
            "product_id": product["product_id"],
            "available": inventory.get("availability_status") == "IN_STOCK",
            "quantity": inventory.get("quantity", 0),
            "warehouse": inventory.get("warehouse", "UNKNOWN"),
        })
    state["inventory_results"] = results
    state["status"] = "inventory_verified"
    return state


def compatibility_node(state: AgentState) -> AgentState:
    query = state.get("user_query", "")
    results = []
    if "4k" in query.lower() or "monitor" in query.lower():
        for product in state.get("product_candidates", []):
            compatibility = product.get("compatibility", {})
            result = {
                "product_id": product["product_id"],
                "compatible": compatibility.get("supports_4k_monitor", False),
                "confidence": 0.92,
                "evidence": compatibility.get("evidence", ["No explicit evidence available"]),
                "sources": [f"spec:{product['product_id']}"]
            }
            results.append(result)
    else:
        results = [{"product_id": p["product_id"], "compatible": True, "confidence": 0.9, "evidence": ["No compatibility issue identified"], "sources": []} for p in state.get("product_candidates", [])]
    state["compatibility_results"] = results
    state["status"] = "compatibility_checked"
    return state


def rag_node(state: AgentState) -> AgentState:
    state["retrieved_documents"] = [{
        "title": "Monitor compatibility guide",
        "source": "compatibility_manual.pdf",
        "excerpt": "HDMI 2.1 devices support 4K at 120Hz. USB-C DisplayPort adapters are compatible with most 4K displays.",
        "section": "Display",
        "citation": "compatibility_manual.pdf#display",
    }]
    state["retrieved_data"] = {"context": "HDMI 2.1 supports 4K 120Hz and USB-C DisplayPort adapters are compatible.", "citations": ["compatibility_manual.pdf#display"]}
    state["status"] = "rag_complete"
    return state


def recommendation_node(state: AgentState) -> AgentState:
    recommendations = []
    for product in state.get("product_candidates", []):
        inventory = next((item for item in state.get("inventory_results", []) if item["product_id"] == product["product_id"]), {})
        compatibility = next((item for item in state.get("compatibility_results", []) if item["product_id"] == product["product_id"]), {})
        recommendations.append({
            "product_id": product["product_id"],
            "name": product["name"],
            "price": product["price"],
            "reason": "Matches budget and compatibility requirements.",
            "available": inventory.get("available", False),
            "compatible": compatibility.get("compatible", False),
        })
    state["recommendations"] = recommendations
    state["status"] = "recommendation_ready"
    return state


def validation_node(state: AgentState) -> AgentState:
    issues = []
    if not state.get("product_candidates"):
        issues.append("No products matched the request.")
    decision = "PASS" if not issues else "RETRY"
    state["validation_result"] = {
        "decision": decision,
        "confidence": 0.9,
        "issues": issues,
        "missing_evidence": [],
    }
    state["status"] = "validated"
    return state


def response_node(state: AgentState) -> AgentState:
    recs = state.get("recommendations", [])
    primary = recs[0] if recs else {}
    response = (
        f"I found the best match: {primary.get('name', 'Product')} at ₹{primary.get('price', 0)}. "
        f"It is {'currently in stock' if primary.get('available') else 'not confirmed in stock'} and "
        f"{'compatible with the requested monitor' if primary.get('compatible') else 'compatibility needs verification'}."
    )
    state["final_response"] = response
    state["status"] = "completed"
    return state


def supervisor_node(state: AgentState) -> AgentState:
    state["intent"] = "shopping"
    state["status"] = "supervised"
    return state


def build_workflow():
    workflow = StateGraph(AgentState)
    workflow.add_node("requirement_understanding", requirement_understanding_node)
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("product_search", product_search_node)
    workflow.add_node("inventory", inventory_node)
    workflow.add_node("compatibility", compatibility_node)
    workflow.add_node("rag", rag_node)
    workflow.add_node("recommendation", recommendation_node)
    workflow.add_node("validation", validation_node)
    workflow.add_node("response", response_node)

    workflow.set_entry_point("requirement_understanding")
    workflow.add_edge("requirement_understanding", "supervisor")
    workflow.add_edge("supervisor", "product_search")
    workflow.add_edge("product_search", "inventory")
    workflow.add_edge("inventory", "compatibility")
    workflow.add_edge("compatibility", "rag")
    workflow.add_edge("rag", "recommendation")
    workflow.add_edge("recommendation", "validation")
    workflow.add_conditional_edges(
        "validation",
        lambda state: "response" if state["validation_result"]["decision"] == "PASS" else "product_search",
        {
            "response": "response",
            "product_search": "product_search",
        },
    )
    workflow.add_edge("response", END)
    return workflow.compile()
