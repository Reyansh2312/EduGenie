import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
        # Yahan wahi model name hai jo latest aur sabse stable hai
        model = genai.GenerativeModel('gemini-pro-latest')
        prompt = f"Explain the following educational topic in simple terms: {topic}"
        
        response = model.generate_content(prompt)
        
        # SABSE IMPORTANT LINE: Hum sirf text bhej rahe hain, koi dictionary {} nahi.
        return str(response.text).strip()
        
    except Exception as e:
        return f"Error: {str(e)}"