from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "conversational-shopping-concierge"
    environment: Literal["dev", "test", "prod"] = "dev"
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", alias="OPENAI_MODEL")
    openai_embedding_model: str = Field(default="text-embedding-3-small", alias="OPENAI_EMBEDDING_MODEL")
    database_url: str = Field(default="sqlite:///./shopping_concierge.db", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    chroma_host: str = Field(default="localhost", alias="CHROMA_HOST")
    chroma_port: int = Field(default=8001, alias="CHROMA_PORT")
    langchain_api_key: str = Field(default="", alias="LANGCHAIN_API_KEY")
    langchain_tracing_v2: bool = Field(default=True, alias="LANGCHAIN_TRACING_V2")
    langchain_project: str = Field(default="conversational-shopping-concierge", alias="LANGCHAIN_PROJECT")
    next_public_api_url: str = Field(default="http://localhost:8000", alias="NEXT_PUBLIC_API_URL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
