import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
import requests
from PIL import Image
from io import BytesIO

def load_image_with_headers(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Open the image using PIL
    image = Image.open(BytesIO(response.content))
    return image

class VideoGenerator:
  def setup(self):
    pass

  def generate(self, image_input_url:str, output_path:str):
    self.pipeline = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
    )
    self.pipeline.enable_model_cpu_offload()

    headers = {
        "Cookie": "ai_dock_token=df1a86bcdc67c261f3ea4ebb1780ef5772e0aefabbb5a6796262e700880e84dc"
    }
    image = load_image_with_headers(image_input_url, headers)
    print(type(image))
    # image = image.resize((1024, 576))

    # generator = torch.manual_seed(42)
    # frames = self.pipeline(image, decode_chunk_size=8, generator=generator).frames[0]
    # export_to_video(frames, output_path, fps=21)