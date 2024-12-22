import openai
from flask import Flask, request, jsonify
from flask_cors import CORS 
import validators
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import requests


load_dotenv()

app = Flask(__name__)
CORS(app)


# openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_content(url):
    
    if not validators.url(url):
        raise ValueError("Invalid URL provided.")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    return ' '.join([p.get_text() for p in paragraphs])


@app.route('/classify', methods=['POST'])
def classify_news():
    try:
        data = request.json
        url = data.get('url')

        # Validate input
        if not url:
            return jsonify({"error": "URL is required"}), 400

        text = extract_content(url)

        prompt = f"Determine if the following news content is fake or real:\n\n{text}\n\nRespond with 'Fake' or 'Real'."

        # Replace with Google Gemini API request
        api_url = "https://gemini.googleapis.com/v1/text/generate"
        headers = {
            "Authorization": f"Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "gemini-v1",
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 300,
        }

        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code != 200:
            return jsonify({"error": f"Google Gemini API error: {response.text}"}), response.status_code

        result = response.json().get("text", "Error processing response")
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':  
   app.run(debug=True)