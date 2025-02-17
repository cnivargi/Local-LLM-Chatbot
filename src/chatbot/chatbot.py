from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from src.models.local_llm import load_local_llm

# Initialize the chatbot
memory = ConversationBufferMemory()
llm = load_local_llm()
chatbot = ConversationChain(llm=llm, memory=memory)

def chat():
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chatbot.run(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()