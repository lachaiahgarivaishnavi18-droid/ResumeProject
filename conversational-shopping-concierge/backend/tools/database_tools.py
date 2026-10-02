def query_database(table: str, filters: dict | None = None) -> list[dict]:
    return [{"table": table, "filters": filters or {}}, {"table": table, "filters": filters or {}}]
