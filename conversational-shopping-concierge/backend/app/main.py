from __future__ import annotations

import uuid
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.data.products import PRODUCTS
from app.graph.workflow import build_workflow
from app.models.schemas import ChatRequest, ChatResponse, HumanApprovalRequest
from app.observability import (
    fetch_alerts,
    fetch_all_traces,
    fetch_approvals,
    fetch_drift,
    fetch_drift_overview,
    fetch_errors,
    fetch_guardrails,
    fetch_log_by_id,
    fetch_logs,
    fetch_metrics,
    fetch_overview,
    fetch_security_events,
    fetch_trace,
    init_observability_db,
    seed_demo_observability_data,
)

app = FastAPI(title="Conversational Shopping Concierge")
settings = get_settings()
init_observability_db()
seed_demo_observability_data()

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
    return PRODUCTS


@app.get("/api/observability/overview")
def observability_overview() -> dict[str, Any]:
    return fetch_overview()


@app.get("/api/logs")
def api_logs(
    limit: int = 50,
    offset: int = 0,
    environment: str | None = None,
    level: str | None = None,
    request_id: str | None = None,
    trace_id: str | None = None,
    session_id: str | None = None,
    endpoint: str | None = None,
    search: str | None = None,
) -> dict[str, Any]:
    return fetch_logs(limit=limit, offset=offset, environment=environment, level=level, request_id=request_id, trace_id=trace_id, session_id=session_id, endpoint=endpoint, search=search)


@app.get("/api/logs/{log_id}")
def api_log_by_id(log_id: int) -> dict[str, Any]:
    log = fetch_log_by_id(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log


@app.get("/api/metrics/requests")
def metrics_requests() -> dict[str, Any]:
    return fetch_metrics("requests")


@app.get("/api/metrics/llm")
def metrics_llm() -> dict[str, Any]:
    return fetch_metrics("llm")


@app.get("/api/metrics/agents")
def metrics_agents() -> dict[str, Any]:
    return fetch_metrics("agents")


@app.get("/api/metrics/tools")
def metrics_tools() -> dict[str, Any]:
    return fetch_metrics("tools")


@app.get("/api/metrics/rag")
def metrics_rag() -> dict[str, Any]:
    return fetch_metrics("rag")


@app.get("/api/metrics/system")
def metrics_system() -> dict[str, Any]:
    return fetch_metrics("system")


@app.get("/api/metrics/database")
def metrics_database() -> dict[str, Any]:
    return fetch_metrics("database")


@app.get("/api/metrics/cost")
def metrics_cost() -> dict[str, Any]:
    return fetch_metrics("cost")


@app.get("/api/traces")
def api_traces(limit: int = 50, offset: int = 0) -> dict[str, Any]:
    return fetch_all_traces(limit=limit, offset=offset)


@app.get("/api/traces/{trace_id}")
def api_trace(trace_id: str) -> dict[str, Any]:
    trace = fetch_trace(trace_id)
    if trace["trace"] is None:
        raise HTTPException(status_code=404, detail="Trace not found")
    return trace


@app.get("/api/drift")
def api_drift() -> dict[str, Any]:
    return {"overview": fetch_drift_overview(), "data": fetch_drift("data"), "model": fetch_drift("model"), "prediction": fetch_drift("prediction"), "concept": fetch_drift("concept"), "prompt": fetch_drift("prompt"), "retrieval": fetch_drift("retrieval")}


@app.get("/api/drift/data")
def api_drift_data() -> dict[str, Any]:
    return fetch_drift("data")


@app.get("/api/drift/model")
def api_drift_model() -> dict[str, Any]:
    return fetch_drift("model")


@app.get("/api/drift/prediction")
def api_drift_prediction() -> dict[str, Any]:
    return fetch_drift("prediction")


@app.get("/api/drift/concept")
def api_drift_concept() -> dict[str, Any]:
    return fetch_drift("concept")


@app.get("/api/drift/prompt")
def api_drift_prompt() -> dict[str, Any]:
    return fetch_drift("prompt")


@app.get("/api/drift/retrieval")
def api_drift_retrieval() -> dict[str, Any]:
    return fetch_drift("retrieval")


@app.get("/api/errors")
def api_errors() -> dict[str, Any]:
    return fetch_errors()


@app.get("/api/security")
def api_security() -> dict[str, Any]:
    return fetch_security_events()


@app.get("/api/guardrails")
def api_guardrails() -> dict[str, Any]:
    return fetch_guardrails()


@app.get("/api/approvals")
def api_approvals() -> dict[str, Any]:
    return fetch_approvals()


@app.get("/api/alerts")
def api_alerts() -> dict[str, Any]:
    return fetch_alerts()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
