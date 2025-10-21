from google.genai import types
import google.genai as genai
from dotenv import load_dotenv 
import os

load_dotenv()


IMAGE_PATH = './foto.jpg'
IMAGE_MIME_TYPE = 'image/jpeg'
API_KEY= os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)


with open(IMAGE_PATH, 'rb') as f:
  image_bytes = f.read()
  for chunk in client.models.generate_content_stream(
  model='gemini-2.0-flash-001',
  contents=[
  'Describe lo que ves en la imagen',
  types.Part.from_bytes(data=image_bytes,
  mime_type=IMAGE_MIME_TYPE),
  ],
  ):
    print(chunk.text, end='', flush=True)