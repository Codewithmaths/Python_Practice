from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Train the chatbot with a predefined corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Sample conversation
print("Hello! I'm your chatbot. Type 'exit' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = get_response(user_input)
    print(f"Bot: {bot_response}")






