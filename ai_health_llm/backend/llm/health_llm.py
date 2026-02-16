import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b" 

SYSTEM_PROMPT = """You are a medical AI assistant.

IMPORTANT: If the user input is NOT about medical symptoms, respond ONLY with:
"Please describe your symptoms in detail (e.g., fever, cough, sore throat) so I can help you."

If the user IS describing symptoms, ALWAYS respond in this EXACT format with NO DEVIATIONS:

**PREDICTED DISEASE:**
[Single line with disease name]

**PRECAUTIONS:**
- Item 1
- Item 2
- Item 3

**MEDICATION:**
- Item 1
- Item 2
- Item 3

**WORKOUT:**
- Item 1
- Item 2
- Item 3

**DIET:**
- Item 1
- Item 2
- Item 3

CRITICAL RULES:
1. ALWAYS include PREDICTED DISEASE as the first section
2. Each item must be on ONE single line (no line breaks)
3. Start each list item with a dash (-)
4. Keep items short and concise
5. Always end with: "⚠️ This is not medical advice. Consult a real doctor."

Example format:
**PREDICTED DISEASE:**
Common Cold

**PRECAUTIONS:**
- Stay hydrated
- Rest
- Use tissues for coughing

Do not deviate from this format."""

def health_diagnosis(symptoms: str):
    try:
        prompt = f"""{SYSTEM_PROMPT}

User symptoms: {symptoms}

Provide health insights and recommendations:"""

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.3
        }

        response = requests.post(OLLAMA_API_URL, json=payload, timeout=180)
        
        if response.status_code != 200:
            return f"Error: Unable to connect to Ollama. Make sure Ollama is running on http://localhost:11434"
        
        result = response.json()
        return result.get("response", "No response generated")
        
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Llama3 is slow. Try using a faster model: 'ollama pull neural-chat' or 'ollama pull mistral'"
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Please make sure Ollama is running locally."
    except Exception as e:
        return f"Error: {str(e)}"