import requests
from PIL import Image
from io import BytesIO

def load_image_with_headers(url, headers):
    """
    Load an image from a URL with custom headers.
    
    Args:
        url (str): The URL of the image.
        headers (dict): A dictionary of custom headers.
    
    Returns:
        Image: The loaded image.
    """
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Open the image using PIL
    image = Image.open(BytesIO(response.content))
    return image

# Example usage
url = "http://66.114.112.70:16095/file=/workspace/stable-diffusion-webui/outputs/txt2img-images/2024-06-08/00012-949075773.png?1717830693.9563658"
headers = {
    "Cookie": "ai_dock_token=df1a86bcdc67c261f3ea4ebb1780ef5772e0aefabbb5a6796262e700880e84dc"
}

image = load_image_with_headers(url, headers)
image.show() 