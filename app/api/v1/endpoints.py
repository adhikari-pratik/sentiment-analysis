from fastapi import APIRouter
from pydantic import BaseModel
from app.models.sentiment import analyze_sentiment

router = APIRouter()


class TextInput(BaseModel):
    text: str


@router.post("/analyze")
def analyze(input: TextInput):
    sentiment = analyze_sentiment(input.text)
    return {"sentiment": sentiment}
