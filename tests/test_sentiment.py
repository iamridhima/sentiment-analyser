import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.sentiment import analyze_sentiment


def test_positive_sentiment():
    assert analyze_sentiment("I love FastAPI!") == "Positive"


def test_negative_sentiment():
    assert analyze_sentiment("I hate bugs.") == "Negative"
