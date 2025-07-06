def chatbot_reply(message):
    message = message.lower()

    if message == "hello":
        return "Hi there!"
    elif message == "how are you":
        return "I'm just code, but I'm doing great!"
    elif message == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

# Main chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Chat ended. Bye!")
        break

    reply = chatbot_reply(user_input)
    print("Bot:", reply)