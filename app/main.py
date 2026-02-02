from fastapi import FastAPI
from config import APP_ENV, APP_NAME
from app.logger import logger

app = FastAPI(title=APP_NAME)

@app.get("/health")
def health():
    logger.info("health_check_called", extra={"env": APP_ENV})
    return {
        "status": "ok",
            "env": APP_ENV
            }