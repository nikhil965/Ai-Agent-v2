BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "llama-3.3-70b-versatile"

import os
from dotenv import load_dotenv

result = load_dotenv()
print("load_dotenv success:", result)

API_KEY = os.getenv("GROQ_API_KEY")
print("API_KEY loaded:", repr(API_KEY))