import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Variable aur indentation fix kar diya gaya hai
        prompt = f"You are a helpful AI tutor. Answer the following question in MAXIMUM 3 to 4 lines. Be very concise, short, and direct. Do not write long paragraphs. Question: {question}"
        
        response = model.generate_content(prompt)
        
        return str(response.text).strip()
        
    except Exception as e:
        return f"Error: {str(e)}"