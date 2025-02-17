from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import logging

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Enable CORS (Important for Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define Chat Request Structure
class ChatRequest(BaseModel):
    message: str

# ✅ LM Studio API Endpoint (Modify if your LM Studio port changes)
LM_STUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        user_message = request.message
        logger.info(f"Received message: {user_message}")

        # ✅ Prepare request payload for LM Studio
        payload = {
            "model": "llama-3.2-3b-instruct-uncensored",
            "messages": [{"role": "user", "content": user_message}],
            "temperature": 0.7,
            "max_tokens": 200
        }

        # ✅ Send request to LM Studio
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        
        # ✅ Check if LM Studio responded successfully
        if response.status_code == 200:
            result = response.json()
            chat_response = result["choices"][0]["message"]["content"]
            logger.info(f"LLM Response: {chat_response}")
            return {"response": chat_response}
        else:
            logger.error(f"LM Studio Error: {response.text}")
            return {"error": "Failed to fetch response from LLM"}

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": str(e)}

# ✅ Handle unexpected favicon requests
@app.get("/favicon.ico")
async def favicon():
    return {}

# ✅ Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Local LLM Chatbot API!"}

# ✅ Run FastAPI Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
