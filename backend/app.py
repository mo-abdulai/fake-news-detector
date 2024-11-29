from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load a model (example using Hugging Face Transformers)
model = pipeline("text-classification", model="your-fake-news-model")

@app.route('/classify', methods=['POST'])
def classify_news():
    data = request.json
    url = data.get('url')

    # Simulate URL content extraction (replace with actual scraping logic)
    text = "Extracted content from the URL"

    # Predict using the LLM
    result = model(text)

    return jsonify({"result": result})
