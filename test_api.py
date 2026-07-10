import os
from dotenv import load_dotenv
import google.generativeai as genai

# Yeh .env file se safely key utha lega
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# ... (aapka baaki ka test code yahan rehne do)

print("⏳ Google se models ki list nikaal raha hu...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print("✅ Available Model:", m.name)
except Exception as e:
    print("\n❌ Error pakda gaya: ", e)