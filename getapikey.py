import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

MY_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not MY_API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Create a .env file (see .env.example) "
        "with your Gemini API key."
    )

genai.configure(api_key=MY_API_KEY)

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")