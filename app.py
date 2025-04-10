from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS
import os
import nltk

# # Set up custom path for nltk_data
# NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
# os.makedirs(NLTK_DATA_PATH, exist_ok=True)
# nltk.data.path.append(NLTK_DATA_PATH)
#
# # Ensure punkt is downloaded in this folder
# try:
#     nltk.data.find("tokenizers/punkt")
# except LookupError:
#     nltk.download("punkt", download_dir=NLTK_DATA_PATH)

app = Flask(__name__)
cors = CORS(app)
CORS(app, resources={r"/chatbot": {"origins": "*"}})


@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    message = data.get("message")

    # Safeguard: Return error if message is missing
    if not message:
        return jsonify({"response": "No message provided"}), 400

    try:
        response = get_response(message)
        return jsonify({"response": response}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
