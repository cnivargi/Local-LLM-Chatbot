import requests

url = "http://127.0.0.1:8000/chat"  # ✅ Correct API endpoint
data = {"message": "Hello, chatbot!"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
