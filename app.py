import fastapi
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "MyKey"
    ALGORITHM: str = "HS256"


app = fastapi.FastAPI()
setting = Settings()
