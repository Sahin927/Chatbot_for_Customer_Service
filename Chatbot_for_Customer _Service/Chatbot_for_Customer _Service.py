# ------------------------------------------
# Step 1: Import required libraries
# ------------------------------------------
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already installed
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


# ---------------------------------------------------
# Step 2: Define intents and rule-based responses
# ---------------------------------------------------
responses = {
    'greeting': ["Hello! How can I assist you today?", 
                 "Hi there! What can I help you with?"],
    
    'pricing': ["Our pricing varies by product. Can you specify which product you're interested in?"],
    
    'refund': ["You can request a refund within 30 days of purchase. Would you like me to guide you?"],
    
    'delivery': ["Standard delivery takes 3–5 business days."],
    
    'goodbye': ["Thank you for contacting us! Have a great day!"],
    
    'unknown': ["I'm sorry, I didn’t understand that. Could you rephrase it?"]
}


# ---------------------------------------------------
# Step 3: NLP preprocessing function
# ---------------------------------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    return tokens


# ---------------------------------------------------
# Step 4: Intent detection using simple keyword matching
# ---------------------------------------------------
def detect_intent(user_msg):

    tokens = preprocess(user_msg)

    # Keyword lists
    intent_keywords = {
        'greeting': ['hi', 'hello', 'hey', 'good morning', 'good evening'],
        'pricing': ['price', 'pricing', 'cost', 'charge'],
        'refund': ['refund', 'return', 'money back'],
        'delivery': ['delivery', 'ship', 'shipping', 'status'],
        'goodbye': ['bye', 'goodbye', 'see you']
    }

    # Check for keywords in tokens
    for intent, keywords in intent_keywords.items():
        for word in tokens:
            if word in keywords:
                return intent

    return 'unknown'


# ---------------------------------------------------
# Step 5: Chatbot Response Function
# ---------------------------------------------------
import random

def get_response(user_msg):
    intent = detect_intent(user_msg)
    return random.choice(responses[intent])


# ---------------------------------------------------
# Step 6: Chatbot Loop
# ---------------------------------------------------
def run_chatbot():
    print("🤖 Customer Service Chatbot (type 'exit' to stop)")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        
        bot_reply = get_response(user_input)
        print("Bot:", bot_reply)


# Run the chatbot
run_chatbot()

