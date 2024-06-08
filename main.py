from fastapi import FastAPI
from pydantic import BaseModel
import base64

app = FastAPI()

class Input(BaseModel):
  image_url:str
  
@app.get("/data")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate(input:Input):
    print(input.image_url)
  
