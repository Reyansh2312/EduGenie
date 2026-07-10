import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Gemini API setup (Jo already aapke baaki modules mein chal raha hai)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> dict:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Explain the following educational topic in simple and clear terms: {topic}"
        
        response = model.generate_content(prompt)
        
        # Frontend exactly yahi format expect kar raha hai
        return {"explanation": response.text.strip()}
    except Exception as e:
        return {"error": str(e)}