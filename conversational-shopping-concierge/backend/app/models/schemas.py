from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class Budget(BaseModel):
    currency: str = "INR"
    maximum: float | None = None
    minimum: float | None = None


class ShoppingRequirements(BaseModel):
    category: str | None = None
    product_type: str | None = None
    budget: Budget | None = None
    use_cases: list[str] = Field(default_factory=list)
    requirements: dict[str, Any] = Field(default_factory=dict)
    brand: str | None = None
    preferred_features: list[str] = Field(default_factory=list)
    compatibility_requirements: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    quantity: int = 1
    location: str | None = None
    confidence: float = 0.0


class ChatRequest(BaseModel):
    session_id: str = "session_001"
    user_id: str = "user_001"
    message: str


class ChatResponse(BaseModel):
    workflow_id: str
    session_id: str
    status: str
    response: str
    sources: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    requires_approval: bool = False


class ValidationResult(BaseModel):
    decision: Literal["PASS", "RETRY", "HUMAN_REVIEW", "BLOCK"] = "PASS"
    confidence: float = 0.0
    issues: list[str] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)


class HumanApprovalRequest(BaseModel):
    approve: bool = False
    notes: str | None = None
