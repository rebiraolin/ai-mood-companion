"""
main.py
-------
FastAPI backend for the AI Mood Companion.

Run with:
    uvicorn backend.main:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from backend.model.emotion_model import predict_emotion
from backend.model.supportive_responses import get_supportive_response

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(
    title="AI Mood Companion API",
    description="Analyses text, predicts an emotion, and returns a supportive response.",
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------
class TextInput(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("text must not be empty or whitespace.")
        return value.strip()


class AnalysisResult(BaseModel):
    emotion: str
    response: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
@app.get("/", tags=["Health"])
def root():
    """Simple health-check endpoint."""
    return {"status": "ok", "message": "AI Mood Companion API is running."}


@app.post("/analyze", response_model=AnalysisResult, tags=["Emotion Analysis"])
def analyze(payload: TextInput):
    """
    Analyse the emotional content of the submitted text.

    - **text**: The user's message (must not be blank).

    Returns the predicted emotion and a supportive response.
    """
    try:
        emotion: str = predict_emotion(payload.text)
        response: str = get_supportive_response(emotion)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(exc)}",
        ) from exc

    return AnalysisResult(emotion=emotion, response=response)
