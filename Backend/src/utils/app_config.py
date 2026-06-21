from dotenv import load_dotenv
from os import getenv

load_dotenv()

def _get_required_env(name: str) -> str:
    value = getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


class AppConfig:
    connection_string: str = _get_required_env("CONNECTION_STRING")
    openai_api_key: str = getenv("OPENAI_API_KEY", "")
    use_demo_mode: bool = getenv("USE_DEMO_MODE", "true").lower() == "true"
    frontend_origin: str = getenv("FRONTEND_ORIGIN", "http://localhost:5173")


if not AppConfig.use_demo_mode and not AppConfig.openai_api_key:
    raise RuntimeError("OPENAI_API_KEY is required when USE_DEMO_MODE is FALSE")
