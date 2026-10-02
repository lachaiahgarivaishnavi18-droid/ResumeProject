class MemoryService:
    def __init__(self):
        self.sessions = {}

    def set_session(self, session_id: str, data: dict) -> None:
        self.sessions[session_id] = data

    def get_session(self, session_id: str) -> dict:
        return self.sessions.get(session_id, {})
