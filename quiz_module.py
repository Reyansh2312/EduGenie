import os
from dotenv import load_dotenv
import google.generativeai as genai
import re
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    try:
        # Smart Auto-Detect code
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        if not available_models:
            return [{"question": "⚠️ Error: No models available for this API key.", "options": ["A", "B", "C", "D"], "answer": "A"}]
        
        best_model = next((m for m in available_models if 'flash' in m), None) or \
                     next((m for m in available_models if 'pro' in m), None) or \
                     available_models[0]
        
        model = genai.GenerativeModel(best_model)
        
        # Quiz ka prompt
        prompt = f"""Create a 3-question multiple-choice quiz based on the general knowledge of this topic: '{text}'. 
IMPORTANT: Do not use phrases like 'in the passage' or 'in the text'. Just ask direct questions about the topic.

Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]"""
        response = model.generate_content(prompt)
        cleaned_text = clean_json_block(response.text.strip())
        return json.loads(cleaned_text)
        
    except Exception as e:
        return [{"question": f"⚠️ Error in Quiz: {e}", "options": ["A", "B", "C", "D"], "answer": "A"}]