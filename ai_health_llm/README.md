# AI Health Diagnostics LLM

A ChatGPT-like web application that uses local AI (Ollama) to help identify diseases based on symptoms and provide personalized recommendations.

## Features

✅ **Disease Prediction** - AI analyzes symptoms and predicts potential diseases  
✅ **Precautions** - Get preventive measures  
✅ **Medication** - Suggested medicines  
✅ **Workout** - Recommended exercises  
✅ **Diet** - Personalized nutrition advice  
✅ **Local AI** - Runs on Ollama (no API costs!)  
✅ **Beautiful UI** - Modern ChatGPT-like interface  

## Project Structure

```
ai_health_llm/
├── backend/              # FastAPI backend
│   ├── main.py          # FastAPI app & routes
│   ├── llm/
│   │   └── health_llm.py # Ollama integration
│   ├── requirements.txt   # Python dependencies
│   └── .env             # Environment variables
├── frontend/            # Web interface
│   └── index.html       # ChatGPT-like UI
└── venv/               # Python virtual environment
```

## Requirements

- Python 3.8+
- Ollama (for local AI)
- fastapi, uvicorn, requests, pydantic

## Installation

### 1. Install Ollama
Download and install from [ollama.ai](https://ollama.ai)

### 2. Download AI Model
```bash
ollama pull llama3
```

### 3. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

## Running the Application

### Step 1: Start Ollama
Keep Ollama running in the background. It starts automatically on port 11434.

### Step 2: Start the Backend
```bash
cd backend
python -m uvicorn main:app --reload
```

### Step 3: Open the Web Interface
Open your browser and go to:
```
http://localhost:8000
```

## How It Works

1. User enters symptoms in the chat
2. FastAPI backend receives the request
3. Ollama processes the symptoms using local Llama3 AI
4. AI returns: Disease, Precautions, Medication, Workout, Diet
5. Frontend displays results in a beautiful formatted card

## API Endpoints

- `GET /` - Serves the frontend HTML
- `POST /ai-diagnosis` - Analyzes symptoms
  - Request: `{"symptoms": "fever, cough, sore throat"}`
  - Response: Disease prediction with recommendations

## Technologies Used

- **Backend**: FastAPI, Python, Ollama
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Llama3 (via Ollama)

## Disclaimer

⚠️ This application provides AI-based suggestions and is **NOT** a medical diagnosis. Always consult a qualified healthcare professional for medical advice.

## License

MIT License

## Future Enhancements

- [ ] Conversation history
- [ ] Multiple languages
- [ ] Export results as PDF
- [ ] Database for user sessions
- [ ] Faster models (Mistral, Neural-chat)
- [ ] Better medical knowledge base
