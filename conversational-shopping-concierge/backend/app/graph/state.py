from __future__ import annotations

from typing import Any, TypedDict


class AgentState(TypedDict, total=False):
    session_id: str
    user_id: str
    user_query: str
    conversation_history: list[str]
    intent: str
    entities: list[str]
    shopping_requirements: dict[str, Any]
    retrieved_data: dict[str, Any]
    retrieved_documents: list[dict[str, Any]]
    product_candidates: list[dict[str, Any]]
    inventory_results: list[dict[str, Any]]
    compatibility_results: list[dict[str, Any]]
    investigation_result: dict[str, Any]
    recommendations: list[dict[str, Any]]
    proposed_actions: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]
    confidence: float
    validation_result: dict[str, Any]
    human_approval: dict[str, Any]
    errors: list[str]
    final_response: str
    workflow_id: str
    status: str
