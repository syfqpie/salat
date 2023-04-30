import ast
from decouple import config

from typing import Any, List, Union
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = config("PROJECT_NAME", "")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = config("BACKEND_CORS_ORIGINS", [])
    VERSION: str = config("VERSION", "0.0.1")
    DESCRIPTION = """
    Salat API helps you get your Malaysian local area prayer times 🕌
    """
    DEBUG: bool = config("DEBUG", False)

    class Config:
        case_sensitive = True

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            """
            Override default function to add custom scenario
            """
            if field_name == "BACKEND_CORS_ORIGINS":
                return cls._assemble_cors_origins(raw_val)

            return cls.json_loads(raw_val)

        def _assemble_cors_origins(raw_val: Union[str, List[str]]) -> List[AnyHttpUrl]:
            """
            Process BACKEND_CORS_ORIGINS value from env and convert into a list
            """
            if isinstance(raw_val, str) and not raw_val.startswith("["):
                return [i.strip() for i in raw_val.split(",")]
            elif isinstance(raw_val, (list, str)):
                # Return converted str representation of list to list
                return ast.literal_eval(raw_val)
            elif isinstance(raw_val, list):
                # If raw_val already a list, return self
                return raw_val


settings = Settings()
