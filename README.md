# 🧠✨ EduGenie - Your Personal AI Learning Assistant

Welcome to **EduGenie**, a smart, customized AI-powered educational assistant built to help students learn more efficiently. Instead of throwing overwhelming walls of text at learners, EduGenie processes complex educational queries in real-time to provide to-the-point answers, simple explanations, quick summaries, and interactive quizzes.

## 🔗 Project Links
* **Live Demo:** [Click here to experience EduGenie Live!](https://edugenie-1-jfw7.onrender.com)
* **GitHub Repository:** [Reyansh2312/EduGenie](https://github.com/Reyansh2312/EduGenie)

---

## 🚀 Features

* **Ask EduGenie:** A dynamic Q&A engine that gives short, precise, and direct answers to any educational queries without the fluff.
* **Need an Explanation?:** Automatically breaks down complex, heavy topics into simple, engaging, bite-sized paragraphs suitable for students.
* **Summarize a Paragraph:** Converts long, boring texts into quick, easy-to-read summaries.
* **Generate a Quiz:** Instantly generates 3-question Multiple Choice Questions (MCQs) in JSON format on any topic to test your knowledge.

---

## 🛠️ Tech Stack & Architecture

* **Programming Language:** Python 3.9+
* **Backend Framework:** FastAPI (for blazing fast API routing)
* **Server:** Uvicorn (ASGI web server)
* **AI Engine:** Advanced NLP / Large Language Model API for intelligent text generation and processing.
* **Deployment & Hosting:** Render (Cloud Hosting)
* **Environment Management:** `python-dotenv` for secure API key handling.

---

## ⚙️ How It Works (Project Flow)

1. **User Input:** The user types a question, topic, or paragraph into the frontend UI.
2. **API Routing:** FastAPI captures this input and routes it to the specific processing module.
3. **AI Processing:** The backend securely communicates with the NLP API, passing carefully engineered prompts to restrict length and format.
4. **Response Delivery:** The structured response is sent back to the user instantly on the web interface.

---

## 💻 Local Setup & Installation

Want to run EduGenie on your local machine? Follow these simple steps depending on your Operating System (Windows, Mac, or Linux):

### Prerequisites
Make sure you have **Python** and **Git** installed on your system.

### Step 1: Clone the Repository (All OS)
Open your terminal or command prompt and run:
`bash
git clone https://github.com/Reyansh2312/EduGenie.git
cd EduGenie
`

### Step 2: Install Dependencies
**For Windows:**
`cmd
pip install -r requirements.txt
`
**For Mac / Linux:**
`bash
pip3 install -r requirements.txt
`

### Step 3: Setup Environment Variables (All OS)
1. Create a file named `.env` in the root directory.
2. Add your API Key to this file:
`text
GEMINI_API_KEY=your_secret_api_key_here
`

### Step 4: Run the Server
**For Windows:**
`cmd
python -m uvicorn main:app --reload
`
**For Mac / Linux:**
`bash
python3 -m uvicorn main:app --reload
`

*The server will start running at `http://127.0.0.1:8000`. Open this URL in your browser to use EduGenie locally!*

---

## 💡 Future Enhancements
* Adding a history database to save past quizzes and answers.
* Implementing user authentication (Login/Signup).
* Adding voice-to-text input for hands-free querying.

---
*Built with ❤️ for better education.*