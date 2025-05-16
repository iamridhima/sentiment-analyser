# Sentiment Analyzer - FastAPI Microservice

## What It Does
This FastAPI microservice analyzes the sentiment of input text as **Positive**, **Negative**, or **Neutral** using TextBlob.

## Demo Video
Watch the full video [here](https://drive.google.com/file/d/1mm6Unsz434X2SjX7vmO6N7EEZb2GWyzs/view).

## How to Run

### Option 1: Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/iamridhima/sentiment-analyser.git
   cd sentiment-analyser

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora

4. Run the app:
   ```bash
   uvicorn app.main:app --reload

5. Visit: http://127.0.0.1:8000/docs to test the API
    
## Option 2: Run with docker
   ```bash
   docker build -t sentiment-analyser .
   docker run -p 8000:8000 sentiment-analyser
