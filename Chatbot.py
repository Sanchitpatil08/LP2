import random

# Define intents directly within the script
intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
            "responses": ["Hello! Welcome to our support chat.", "Hi there! How can I assist you today?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "see you", "goodbye", "talk to you later"],
            "responses": ["Goodbye! Have a great day.", "See you next time!", "Take care!"]
        },
        {
            "tag": "thanks",
            "patterns": ["thank you", "thanks", "appreciate it", "thx"],
            "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
        },
        {
            "tag": "order_status",
            "patterns": ["where is my order", "track my order", "order status", "order update"],
            "responses": ["You can track your order here: www.example.com/track", "Please enter your order ID to get the latest status."]
        },
        {
            "tag": "return_policy",
            "patterns": ["what is your return policy", "can I return my order", "how do I return an item"],
            "responses": ["You can return products within 7 days of delivery.", "Visit www.example.com/returns to start your return process."]
        },
        {
            "tag": "refund_status",
            "patterns": ["when will I get my refund", "refund status", "how long does refund take"],
            "responses": ["Refunds are processed within 3-5 business days.", "You will receive an email once your refund is completed."]
        },
        {
            "tag": "payment_issue",
            "patterns": ["payment failed", "my payment didn’t go through", "I was charged twice", "payment issue"],
            "responses": ["Sorry about that! Please contact our billing team at support@example.com.", "You can also raise a complaint at www.example.com/support."]
        },
        {
            "tag": "shipping_info",
            "patterns": ["how long does delivery take", "shipping time", "delivery duration"],
            "responses": ["Shipping typically takes 3-5 business days.", "We aim to deliver all orders within 5 days."]
        },
        {
            "tag": "cancel_order",
            "patterns": ["how do I cancel my order", "cancel my order", "I want to cancel"],
            "responses": ["You can cancel your order from your profile under 'My Orders'.", "Visit www.example.com/cancel to cancel your order."]
        }
    ]
}

# Function to get a response based on user input
def get_simple_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for easier comparison
    
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])
    
    return "I'm not sure I understand. Can you try asking in a different way?"

# Chatbot interaction loop
def chat():
    print("Hello! I am your chatbot. Type 'exit' to end the chat.\n")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Goodbye! Have a great day!")
            break

        response = get_simple_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
