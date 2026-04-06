# 🤖 SAP AI Assistant

An AI-powered Q&A assistant for SAP Security built with FastAPI + LangChain + Groq LLaMA.

## 🚀 Features
- Ask any SAP Security question in natural language
- Powered by Groq LLaMA3 (free LLM)
- TF-IDF based document retrieval
- REST API built with FastAPI
- 36+ SAP Security knowledge chunks

## 🛠️ Tech Stack
- Python 3.14
- FastAPI
- LangChain
- Groq (LLaMA3)
- Scikit-learn (TF-IDF)

## ⚙️ Setup & Run

### 1. Clone the repo
git clone https://github.com/hrjd-harshit/sap-ai-assistant.git
cd sap-ai-assistant

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
python -m pip install -r requirements.txt

### 4. Add your Groq API key
Create a .env file:
GROQ_API_KEY=your-key-here

### 5. Ingest knowledge base
python -m app.ingest

### 6. Run the server
uvicorn app.main:app --reload

### 7. Test it
curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question": "What is SU53?"}'

## 📡 API Endpoints
- GET / — Welcome message
- POST /ask — Ask an SAP Security question

## 👨‍💻 Author
Harshit Jain — SAP Security Consultant & Python Developer