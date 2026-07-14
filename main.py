import os
import uvicorn
from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Modules import
from qna import get_ai_answer
from summary_module import get_summary
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations
from explanation_module import explain_topic

os.environ["GRPC_DNS_RESOLVER"] = "native"

app = FastAPI()

# HTML aur CSS setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 1. Q&A - GET API
@app.get("/qa")
async def answer_question(question: str = Query(...)):
    answer = get_ai_answer(question)
    return {"answer": answer}

# 2. Explanation - POST API
@app.post("/explain/")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}

# 3. Summarization - POST API
@app.post("/summarize/")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize."}, status_code=400)
    summary = get_summary(text)
    return {"summary": summary}

# 4. Quiz Generation - POST API
@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz."}, status_code=400)
    quiz = generate_quiz(text)
    return JSONResponse(content={"quiz": quiz})

# 5. Learning Recommendations - GET API
@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(...)):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}

# RENDER PORT FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)