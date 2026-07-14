import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
        # Smart Auto-Detect code
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        if not available_models:
            return "Error: Your API key doesn't have access to any models."
        
        best_model = next((m for m in available_models if 'flash' in m), None) or \
                     next((m for m in available_models if 'pro' in m), None) or \
                     available_models[0]
        
        model = genai.GenerativeModel(best_model)
        
        # PROMPT CHANGE: Ab isko 4 se 5 sentences likhne ko bola hai ek proper paragraph mein.
        prompt = f"Explain the following educational topic clearly and comprehensively in exactly 4 to 5 sentences. Write it as a single informative paragraph that is engaging for a student. Topic: {topic}"
        
        response = model.generate_content(prompt)
        
        return str(response.text).strip()
        
    except Exception as e:
        return f"Error: {str(e)}"