import os
import io
import base64
import json
import google.generativeai as genai
from PIL import Image

class CaesarAIGemini:
  def __init__(self) -> None:
    genai.configure(api_key = (os.getenv("GOOGLE_AI_STUDIO_API_KEY")))

    self.model = genai.GenerativeModel('gemini-pro')
    self.chat = self.model.start_chat(history=[])
    self.vision_model = genai.GenerativeModel('gemini-pro-vision')
  def send_message(self,message):
    response = self.chat.send_message(message, stream=True)
    for chunk in response:
      try:
        yield chunk.text
      except ValueError as vex:
        yield ""
  def get_history(self):
   for message in self.chat.history:
     yield json.dumps({message.role:message.parts[0].text})
  def describe_image(self,image_content):
    image_stream = io.BytesIO(image_content)
    image_stream.seek(0)
    img = Image.open(image_stream)
    response = self.vision_model.generate_content(img)
    return response.text
  
if __name__ == "__main__":
  caesar = CaesarAIGemini()
  for i in caesar.send_message("hi"):
    print(i)
    

     
