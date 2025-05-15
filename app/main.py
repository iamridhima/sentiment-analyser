from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.post("/analyze")
def analyze(input: TextInput):
    return {"sentiment": analyze_sentiment(input.text)}
