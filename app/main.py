from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.rag import get_answer
import traceback

app = FastAPI(
    title="SAP AI Assistant",
    description="Ask any SAP Security question and get AI-powered answers!",
    version="1.0.0"
)

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {
        "message": "Welcome to SAP AI Assistant! 🤖",
        "usage": "Send a POST request to /ask with your SAP question"
    }

@app.post("/ask")
def ask(query: Query):
    try:
        answer = get_answer(query.question)
        return {
            "question": query.question,
            "answer": answer
        }
    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ ERROR: {error_details}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "details": error_details}
        )