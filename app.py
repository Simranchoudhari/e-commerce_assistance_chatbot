from flask import Flask, request, jsonify
from chatbot import get_best_response  # Import the chatbot function

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the E-commerce Chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_best_response(user_message)  # Get response from the chatbot
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000)
