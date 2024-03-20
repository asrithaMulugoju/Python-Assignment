import nltk

from nltk.chat.util import Chat, reflections

patterns=[(r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm great, thanks for asking!"]),
    (r"what is your name?", ["My name is Chatbot.", "You can call me Chatbot."]),
    (r"quit|exit", ["Goodbye!", "Bye!", "See you later!"]),]

chatbot = Chat(patterns, reflections)

print("Welcome to the Chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == "quit":
        break