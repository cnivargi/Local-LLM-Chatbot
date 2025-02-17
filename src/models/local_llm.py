from langchain_openai import OpenAI

# Load Local LLM via LM Studio API
def load_local_llm():
    return OpenAI(
        openai_api_base="http://127.0.0.1:1234",  # ✅ Corrected endpoint (removed `/v1`)
        openai_api_key="sk-fake-key",  # LM Studio does not need an API key, but LangChain expects one
        model="llama-3.2-3b-instruct-uncensored"  # ✅ Updated model name
    )

if __name__ == "__main__":
    llm = load_local_llm()
    print("✅ Local LLM (Llama 3.2 3B) initialized successfully!")
