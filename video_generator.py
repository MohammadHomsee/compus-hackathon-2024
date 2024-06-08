import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video

class VideoGenerator:
  def setup(self):
    self.pipeline = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
    )
    self.pipeline.enable_model_cpu_offload()

  def generate(self, image_input_url:str):
    image = load_image(image_input_url)
    image = image.resize((1024, 576))

    generator = torch.manual_seed(42)
    frames = self.pipeline(image, decode_chunk_size=8, generator=generator).frames[0]
    export_to_video(frames, "generated.mp4", fps=21)