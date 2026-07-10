import os
from dotenv import load_dotenv
import google.generativeai as genai
import traceback

# .env file se key uthana
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (links, books). Include beginner, intermediate, and advanced levels."""
    try:
        model = genai.GenerativeModel(model_name="gemini-pro-latest")
        response = model.generate_content(prompt)
        
        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "❌ Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"