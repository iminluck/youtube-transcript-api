from fastapi import FastAPI
import requests
import re

app = FastAPI()

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu.be/)([a-zA-Z0-9_-]+)", url)
    return match.group(1)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/transcript")
def get_transcript(url: str):

    try:
        video_id = extract_video_id(url)

        transcript_url = f"https://video.google.com/timedtext?lang=en&v={video_id}"

        response = requests.get(transcript_url)

        return {"transcript_xml": response.text}

    except Exception as e:
        return {"error": str(e)}
