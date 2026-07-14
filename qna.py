import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_answer(question: str) -> str:
    try:
        # Models fetch karna
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
        
        # Prompt ko strict rakha hai, par line ko cut hone se rokne ke liye hard limit hata di
        prompt = f"Provide a brief, direct answer in exactly 2 or 3 sentences. Do not use lists, bullet points, or headings. Keep it short. Question: {question}"
        
        # Yahan se generation_config (token limit) hata diya hai taaki sentence poora ho!
        response = model.generate_content(prompt)
        
        return str(response.text).strip()
        
    except Exception as e:
        return f"Error: {str(e)}"