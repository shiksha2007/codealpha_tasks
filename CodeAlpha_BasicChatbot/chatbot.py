
# CodeAlpha - Basic Chatbot
# Task 4: Rule-Based Chatbot

def get_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi" or message == "hey":
        return "Hi! Nice to meet you!"

    elif message == "how are you" or message == "how are you?":
        return "I'm fine, thanks! How are you?"

    elif message == "what is your name":
        return "I'm CodeAlpha Chatbot, your simple virtual assistant!"

    elif message == "help":
        return "You can say hello, ask how I am, or say bye."

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Please try something else."


def chatbot():
    print("===================================")
    print("       WELCOME TO CHATBOT")
    print("===================================")
    print("Type 'bye' to end the conversation.")
    print("You can also type 'help' to see options.")

    while True:
        user_message = input("\nYou: ")
        response = get_response(user_message)

        print("Bot:", response)

        if user_message.lower().strip() == "bye" or user_message.lower().strip() == "goodbye":
            break


chatbot()
