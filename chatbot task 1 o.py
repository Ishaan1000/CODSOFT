class RuleBasedChatbot:
    def __init__(self):
        self.responses = {
            "Hello": "Hello! Welcome to Alvo. How can I assist you today?",
            "How are you": "I'm just a bot, but I'm here to help!",
            "Bye": "Goodbye! Have a great day!",
            "Thanks for your help": "You're welcome! If you have any more questions or need further assistance, don't hesitate to ask. Have a great day!",
            "Name": "I'm Alvo ChatBot, your virtual assistant.",
            "Tell me about your latest laptop model.":  "Our latest laptop model features a sleek design, powerful processor, and high-resolution display. You can find more details on our website.",
            "I ordered a product. Can you check the status?": "Of course, I can help with that. Please provide your order number, and I'll check the status for you.",
            "How do I install your software?": "Installing our software is easy. Visit our website, go to the Downloads section, and follow the step-by-step installation guide.",
            "I forgot my password. What should I do?": "No problem! You can reset your password by clicking on the 'Forgot Password' link on our login page. Follow the prompts to create a new password.",
            "Your app is amazing!": "Thank you so much for your positive feedback! We're thrilled to hear that you're enjoying our app. Is there anything specific you like about it?",
            "Can I talk to a human?": "Of course! I can connect you with one of our support specialists. Please hold on for a moment.",
            "I'm having trouble downloading your app.": "I'm here to help. Make sure you're using a stable internet connection, and try clearing your browser cache. If the issue persists, I can provide alternative download links.",
            "When can I reach your tech support?": "Our tech support is available Monday to Friday, from 9 AM to 6 PM. Feel free to reach out during those hours for assistance.",
            "I wish your software had a dark mode.": "Thank you for the suggestion! Dark mode is a popular feature request. We'll definitely consider adding it to our roadmap.",
            "default": "I'm not sure how to respond to that. Could you please rephrase or ask something else?",
            
        }
    
    def get_response(self, message):
        for keyword in self.responses:
            if keyword.lower() in message.lower():
                return self.responses[keyword]
        return self.responses["default"]

def main():
    chatbot = RuleBasedChatbot()
    print("Rule-Based Chatbot: Hello! How can I assist you today? (type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Rule-Based Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Rule-Based Chatbot:", response)

if __name__ == "__main__":
    main()
