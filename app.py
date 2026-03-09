from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = FastAPI()

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu.be/)([a-zA-Z0-9_-]+)", url)
    return match.group(1)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/transcript")
def get_transcript(url: str):

    try:
        video_id = extract_video_id(url)

        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        text = " ".join([item.text for item in transcript])

        return {"transcript": text}

    except Exception as e:
        return {"error": str(e)}
