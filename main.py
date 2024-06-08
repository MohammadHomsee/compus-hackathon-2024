from fastapi import FastAPI
from pydantic import BaseModel
from video_generator import VideoGenerator

app = FastAPI()

generator = VideoGenerator()

class Input(BaseModel):
  image_url:str

@app.get("/data")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate(input:Input):
    generator.generate(input.image_url)