from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    cors_allowed_origin: list[str]
    cors_allowed_credentials: bool
    cors_allowed_methods: list[str]
    cors_allowed_headers: list[str]


def get_settings() -> Settings:
    return Settings(
        DATABASE_URL = "sqlite:///./my_db.db",
        cors_allowed_origin = ["http://localhost:3000"],
        cors_allowed_credentials = True,
        cors_allowed_methods = ["*"],
        cors_allowed_headers = ["*"],
    )

settings = get_settings()
