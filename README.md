# 🏆 Local LLM Chatbot - Powered by LM Studio

## 🚀 Project Overview
This project is a **local AI chatbot** powered by **FastAPI, Streamlit, and LM Studio**, allowing users to interact with **Llama 3** models on their own hardware.

## 🛠️ Features
✅ **FastAPI Backend** - Handles chat requests  
✅ **Streamlit UI** - Clean interface for users  
✅ **LM Studio Integration** - Runs Llama 3 locally  
✅ **Voice Input & File Uploads** - Enhances AI interaction  
✅ **Dark Mode & Custom Themes**  

## 📌 Installation
```sh
git clone https://github.com/your-username/Local-LLM-Chatbot.git
cd Local-LLM-Chatbot
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt


Business Case: Why Build This Chatbot?
🔍 Problem Statement
With the rise of Generative AI, many users want to run local LLMs (Large Language Models) on their own machines without relying on OpenAI APIs. However, setting up a custom AI chatbot that works with LM Studio (which allows local LLM execution) is challenging due to:

Compatibility issues between FastAPI, Streamlit, and LM Studio
Network and CORS restrictions when calling local APIs
Optimization of LLMs for low-VRAM GPUs
Creating a user-friendly UI for easy interaction
🛠️ Our Goal
Build an AI chatbot that runs fully locally
Use LM Studio to execute Llama 3 LLM
Create a FastAPI backend for API requests
Build a Streamlit-based UI for easy interaction
Allow voice input, file uploads, and dynamic UI features


Our Solution Approach

![image](https://github.com/user-attachments/assets/91d381c5-6ede-45ed-968a-d393b2b64cb1)

📌 Step-by-Step Implementation
✅ Step 1: Setting Up the Environment
Why?
We need to isolate our dependencies so that our Python packages don’t conflict.

Steps Taken:

Created a virtual environment (.venv)
Installed necessary dependencies: FastAPI, Streamlit, Uvicorn, Requests, etc.
Verified installation with pip list
✅ Step 2: Setting Up FastAPI Backend
Why?
FastAPI is used to create an API endpoint that Streamlit UI can interact with.

Steps Taken:

Created server.py in the src/api/ folder
Set up a FastAPI app to receive chat messages
Integrated LM Studio by sending POST requests
✅ Step 3: Running LM Studio with Local LLM
Why?
LM Studio allows us to run Llama 3 locally, replacing API-based solutions like OpenAI.

Steps Taken:

Downloaded Llama 3.2-3B-instruct-uncensored
Verified it runs on http://127.0.0.1:1234
Ensured that the correct API format was used
✅ Step 4: Building the Streamlit UI
Why?
A good UI allows easy interaction with the chatbot without using command-line tools.

Steps Taken:

Created chat_ui.py to interact with FastAPI
Added chat history, avatars, file uploads, and dark mode
✅ Step 5: Debugging API Connectivity Issues
Why?
The API was working in PowerShell but not in Streamlit, which meant CORS issues.

Errors Faced & Fixes:

❌ Error: Could not reach API → Fixed by enabling CORS in FastAPI
❌ Error: Unprocessable Entity (422) → Fixed by ensuring request format matched FastAPI
✅ Step 6: Adding Extra Features
📂 File Uploads: Allow AI to analyze PDFs
🎤 Voice Input: Convert speech-to-text
🌙 Dark Mode: Toggle between themes
🚀 Quick Prompts: Predefined AI queries

Errors Faced & Fixes

![image](https://github.com/user-attachments/assets/407a3df4-b5b4-45a6-8600-59a8dfaa128d)



Future Improvement Areas
✅ 1. Better UI with Gradio / React
✅ 2. Database for Storing Chat Conversations
✅ 3. Dockerizing the Application for Easier Deployment
✅ 4. Custom RAG (Retrieval-Augmented Generation) for Personalized Responses
✅ 5. Deploying on Cloud (Google Cloud / AWS / Railway)
