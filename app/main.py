from fastapi import FastAPI
from app.api.v1.endpoints import router as sentiment_router
from app.core.config import settings

app = FastAPI(title=settings.model_name)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/")
def health_check():
    return {"status": "ok", "env": settings.env}


app.include_router(sentiment_router, prefix="/api/v1")
