from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = FastAPI()

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu.be/)([a-zA-Z0-9_-]+)", url)
    return match.group(1)

@app.get("/transcript")
def get_transcript(url: str):

    video_id = extract_video_id(url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([t["text"] for t in transcript])

    return {"transcript": text}
