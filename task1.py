def chatbot():
    print("Hello! I'm your rule-based chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm just code, but I'm functioning perfectly! How about you?")
        elif "your name" in user_input:
            print("Bot: I'm a simple chatbot created by Devanshi.")
        elif "time" in user_input:
            from datetime import datetime
            print(f"Bot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif "date" in user_input:
            from datetime import date
            print(f"Bot: Today's date is {date.today().strftime('%B %d, %Y')}")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: I'm not sure how to respond to that. Can you rephrase?")

chatbot()
