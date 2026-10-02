class ApprovalService:
    def __init__(self):
        self.approvals = {}

    def request_approval(self, workflow_id: str, payload: dict) -> dict:
        self.approvals[workflow_id] = payload
        return {"workflow_id": workflow_id, "status": "pending_human_approval"}

    def resolve_approval(self, workflow_id: str, approved: bool) -> dict:
        return {"workflow_id": workflow_id, "approved": approved}
