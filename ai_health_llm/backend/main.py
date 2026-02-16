from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm.health_llm import health_diagnosis
import os

app = FastAPI(title="AI Diagnostic System")

# Add CORS middleware to allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomInput(BaseModel):
    symptoms: str

# Serve the frontend HTML
@app.get("/")
async def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    return FileResponse(frontend_path)

# AI diagnosis route (POST)
@app.post("/ai-diagnosis")
async def diagnosis(data: SymptomInput):
    result = health_diagnosis(data.symptoms)
    return {
        "ai_response": result,
        "disclaimer": "This is not a medical diagnosis."
    }