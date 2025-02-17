import streamlit as st
import requests
import sys

# ✅ Set Streamlit Page Config (Must be First Command)
st.set_page_config(page_title="Chatbot UI", layout="wide")

# ✅ API Endpoint
API_URL = "http://127.0.0.1:8000/chat"

# 🎨 **Header**
st.markdown("<h1 style='text-align: center;'>🤖 Local AI Chatbot</h1>", unsafe_allow_html=True)

# ✅ Chat History Storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Sidebar Debugging Panel
with st.sidebar:
    st.subheader("🛠 Debugging Panel")
    st.write(f"✅ API URL: `{API_URL}`")
    st.write(f"🔍 Python Executable: `{sys.executable}`")

    # ✅ Collapsible Debug Information
    with st.expander("📤 Last API Request", expanded=False):
        if "last_request" in st.session_state:
            st.json(st.session_state.last_request)

    with st.expander("📥 Last API Response", expanded=False):
        if "last_response" in st.session_state:
            st.json(st.session_state.last_response)

# ✅ Chat Layout
col1, col2 = st.columns([3, 1])  # Left: Chat, Right: Sidebar

with col1:
    # ✅ Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])

    # ✅ User Input
    user_input = st.chat_input("Type your message...")

    if user_input:
        # ✅ Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # ✅ Display user message immediately
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(user_input)

        # ✅ Prepare API Request
        request_payload = {"message": user_input}
        st.session_state.last_request = request_payload  # Store for debugging

        # ✅ Send Request to FastAPI
        try:
            response = requests.post(API_URL, json=request_payload)
            st.session_state.last_response = response.json()  # Store for debugging

            if response.status_code == 200:
                reply = response.json()["response"]
            else:
                reply = f"⚠️ API Error: {response.text}"

        except Exception as e:
            reply = f"❌ Connection Error: {str(e)}"

        # ✅ Show AI Response
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"📝 **AI:** {reply}")

        # ✅ Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": reply})
