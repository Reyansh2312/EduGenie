import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Variable aur indentation fix kar diya gaya hai
        prompt = f"Explain the following educational topic in a very concise, short, and easy-to-understand way. Keep it under 3-4 sentences or use short bullet points so a student can read it quickly. Topic: {topic}"
        
        response = model.generate_content(prompt)
        
        return str(response.text).strip()
        
    except Exception as e:
        return f"Error: {str(e)}"