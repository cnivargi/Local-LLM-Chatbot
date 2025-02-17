import requests

# ✅ Use the correct endpoint
url = "http://127.0.0.1:1234/v1/chat/completions"

data = {
    "model": "llama-3.2-3b-instruct-uncensored",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],  # ✅ Chat format
    "max_tokens": 50
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())  # ✅ Print API response
