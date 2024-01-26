import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv("CaesarAIGemini/.env")
class CaesarAIGemini:
  def __init__(self) -> None:
    genai.configure(api_key = base64.b64decode(os.getenv("GOOGLE_AI_STUDIO_API_KEY").encode()).decode())

    self.model = genai.GenerativeModel('gemini-pro')
    self.chat = self.model.start_chat(history=[])
  def send_message(self,message):
    response = self.chat.send_message(message, stream=True)
    for chunk in response:
      yield chunk.text
     
