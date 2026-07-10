import os
from dotenv import load_dotenv
import google.generativeai as genai
import re
import json

# .env file se key uthana
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    try:
        model = genai.GenerativeModel(model_name="gemini-pro-latest")
        prompt = f"""You are a quiz generator.
From the following passage, create 3 multiple-choice questions. Each question should include:
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
]

Passage:
{text}"""
        response = model.generate_content(prompt)
        cleaned_text = clean_json_block(response.text.strip())
        return json.loads(cleaned_text)
    except Exception as e:
        return [{"question": f"⚠️ Error in Quiz: {e}", "options": [], "answer": ""}]