import os
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "Meeting Intelligence Agent API"
    VERSION: str = "0.25.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/meeting_intelligence"
    )

    # Integrations
    LINEAR_API_KEY: str = os.getenv("LINEAR_API_KEY", "")
    LINEAR_TEAM_ID: str = os.getenv("LINEAR_TEAM_ID", "")
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN", "")
    SLACK_CHANNEL_ID: str = os.getenv("SLACK_CHANNEL_ID", "")

settings = Settings()

