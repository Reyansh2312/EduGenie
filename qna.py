import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env file se key uthana
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_ai_answer(question: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="gemini-pro-latest")
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"