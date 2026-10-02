from __future__ import annotations

import uuid
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.graph.workflow import build_workflow
from app.models.schemas import ChatRequest, ChatResponse, HumanApprovalRequest

app = FastAPI(title="Conversational Shopping Concierge")
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = build_workflow()


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": settings.app_name}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    workflow_id = str(uuid.uuid4())
    state = {"session_id": request.session_id, "user_id": request.user_id, "user_query": request.message, "workflow_id": workflow_id, "status": "started"}
    result = workflow.invoke(state)
    final = result.get("final_response") or "I found a suitable recommendation for your request."
    return ChatResponse(
        workflow_id=workflow_id,
        session_id=request.session_id,
        status=result.get("status", "completed"),
        response=final,
        sources=[doc.get("citation", "") for doc in result.get("retrieved_documents", []) if doc.get("citation")],
        recommendations=[f"{r.get('name')} • ₹{r.get('price')}" for r in result.get("recommendations", [])],
        requires_approval=bool(result.get("human_approval")),
    )


@app.post("/api/agent/run")
def agent_run(payload: dict[str, Any]) -> dict[str, Any]:
    return {"status": "ok", "workflow_id": str(uuid.uuid4()), "output": payload}


@app.get("/api/workflows/{workflow_id}")
def get_workflow(workflow_id: str) -> dict[str, Any]:
    return {"workflow_id": workflow_id, "status": "completed"}


@app.post("/api/approval/{workflow_id}")
def approval(workflow_id: str, payload: HumanApprovalRequest) -> dict[str, Any]:
    if not payload.approve:
        return {"workflow_id": workflow_id, "status": "rejected", "message": "Approval was not granted."}
    return {"workflow_id": workflow_id, "status": "approved", "message": "Approval recorded."}


@app.get("/api/metrics")
def metrics() -> dict[str, Any]:
    return {"status": "ok", "metrics": {"requests": 0, "workflow_runs": 0}}


@app.get("/api/sessions/{session_id}")
def session(session_id: str) -> dict[str, Any]:
    return {"session_id": session_id, "status": "active"}


@app.post("/api/documents/upload")
def upload_document() -> dict[str, Any]:
    return {"status": "uploaded", "message": "Document upload endpoint ready."}


@app.post("/api/documents/ingest")
def ingest_documents() -> dict[str, Any]:
    return {"status": "ok", "message": "Ingestion pipeline initialized."}


@app.get("/api/products")
def products() -> list[dict[str, Any]]:
    return [{"product_id": p["product_id"], "name": p["name"], "price": p["price"]} for p in [
        {"product_id": "LAP001", "name": "AeroPro G14", "price": 74999},
        {"product_id": "PHN001", "name": "PixelLens M9", "price": 33999},
        {"product_id": "MON001", "name": "VisionMax 27U", "price": 24999},
    ]]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
