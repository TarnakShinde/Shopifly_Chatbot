from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS

# Import your chatbot model and other necessary components

app = Flask(__name__)
cors = CORS(app)


# @app.route('/chatbot', methods=['POST'])
# def chatbot_response():
#     data = request.json
#     user_input = data.get('message')
#
#     # Generate response using your chatbot model
#     response = generate_response(user_input)
#
#     return jsonify({'response': response})
#
#
# def generate_response(input_text):
#     # Preprocess input, pass it through the model, and postprocess the output
#     # This is a placeholder implementation
#     response = "This is a response from the model."
#     return response

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    text = request.get_json().get("message")
    response = get_response(text)
    # message = {"answer": response}
    return jsonify({'response': response})


# @app.post("/predict")
# def predict():
#     text = request.get_json().get("message")
#     response = get_response(text)
#     message = {"answer": response}
#     return jsonify(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
