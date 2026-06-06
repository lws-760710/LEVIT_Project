from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    levit_env: str = Field(default="development", alias="LEVIT_ENV")
    levit_api_host: str = Field(default="0.0.0.0", alias="LEVIT_API_HOST")
    levit_api_port: int = Field(default=8000, alias="LEVIT_API_PORT")
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    anthropic_api_key: str | None = Field(default=None, alias="ANTHROPIC_API_KEY")


settings = Settings()
