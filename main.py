from fastapi import FastAPI
from pydantic import BaseModel
from video_generator import VideoGenerator
import io
from starlette.responses import FileResponse

app = FastAPI()

generator = VideoGenerator()
generator.setup()

class Input(BaseModel):
  image_url:str

@app.get("/data")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate(input:Input):
  generator.generate(input.image_url, "output.mp4")
  return "output.mp4"

@app.get('/load')
async def load(path:str):
  return FileResponse(path)
  return path
  with open(path, "rb") as f:
    return f.read()

# path = "test3.png"
# generator.generate(path)