from fastapi import FastAPI
from pydantic import BaseModel
from video_generator import VideoGenerator
import io
from starlette.responses import FileResponse
import base64

def save_base64_image(base64_string, output_path):
    """
    Decodes a base64 string and saves it as an image file.
    
    Args:
        base64_string (str): The base64 string of the image.
        output_path (str): The path where the image will be saved.
    """
    try:
        # Decode the base64 string
        image_data = base64.b64decode(base64_string)
        
        # Write the image data to a file
        with open(output_path, 'wb') as image_file:
            image_file.write(image_data)
        
        print(f"Image successfully saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

app = FastAPI()

generator = VideoGenerator()
generator.setup()

class Input(BaseModel):
  base64_image:str

@app.get("/data")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate(input:Input):
  save_base64_image(input.base64_image, "base64.png")
  return input.base64_image
  generator.generate("base64.png", "output.mp4")
  return "output.mp4"

@app.get('/load')
async def load(path:str):
  return FileResponse(path)
  return path
  with open(path, "rb") as f:
    return f.read()

# path = "test3.png"
# generator.generate(path)