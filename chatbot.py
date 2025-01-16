import nltk
import random
import string

# Download necessary NLTK packages
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Define some responses and patterns
responses = {
    "greeting": ["Hello! How can I help you?", "Hi there! How can I assist you today?", "Hey! What can I do for you?"],
    "how_are_you": ["I'm just a bot, but I'm doing fine! How about you?", "I'm good, thanks for asking! How are you?"],
    "bye": ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"],
    "unknown": ["Sorry, I didn't understand that. Could you rephrase?", "I'm not sure what you mean, can you clarify?"]
}

# Define a set of patterns and their associated responses
patterns = {
    "hello": "greeting",
    "hi": "greeting",
    "how are you": "how_are_you",
    "bye": "bye",
    "goodbye": "bye"
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = nltk.word_tokenize(user_input.lower())
    
    # Lemmatize the tokens to their base form
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return lemmatized_tokens

# Function to determine the bot's response
def generate_response(user_input):
    tokens = preprocess_input(user_input)

    # Check for known patterns in user input
    for word in tokens:
        if word in patterns:
            response_type = patterns[word]
            return random.choice(responses[response_type])
    
    # If no match found, return an unknown response
    return random.choice(responses["unknown"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Check if the user wants to end the chat
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: " + generate_response(user_input))
            break
        
        # Get bot's response and print it
        response = generate_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
