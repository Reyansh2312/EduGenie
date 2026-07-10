# EduGenie - AI Learning Assistant 🧞‍♂️

EduGenie is an advanced AI-powered educational assistant designed to make learning simplified, interactive, and personalized.

## 🚀 Features & Modules

*   **Explanation Module:** Utilizes the LaMini-Flan-T5 model to deliver educational content in a simplified and highly readable manner. Perfect for beginners and school students.
*   **QnA Module:** Powered by Gemini 1.5 Pro, enabling it to handle a wide range of general knowledge and academic question-answering tasks with precision.
*   **Quiz Module:** Generates three multiple-choice questions (MCQs) from a given passage, returning structured JSON output with plausible distractors.
*   **Summary Module:** Leverages Gemini's generative capabilities to summarize long paragraphs into concise, easy-to-understand versions for quick revision.
*   **Learning Path Module:** Generates a personalized, structured learning path for any given topic from beginner to advanced levels.

## ⚙️ Backend Infrastructure

The backend infrastructure of the EduGenie Learning Assistant is built using the **FastAPI framework**. FastAPI was selected because of its high performance, asynchronous request handling, simplicity, and easy API integration capabilities.

The backend architecture is designed in a modular manner, where each endpoint is connected to its respective AI functionality. 

### RESTful API Endpoints:
*   `GET /qa` → Handles educational question answering.
*   `POST /explain/` → Generates simplified explanations for topics.
*   `POST /quiz` → Creates AI-generated multiple-choice quizzes.
*   `POST /summarize/` → Summarizes lengthy educational content.
*   `GET /learn/recommendations` → Generates personalized learning paths.

Each endpoint receives user input through request parameters or JSON data, validates the input, calls the corresponding module logic, and finally returns the generated educational response in JSON format.