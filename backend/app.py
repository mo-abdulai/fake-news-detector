import openai
from flask import Flask, request, jsonify
from flask_cors import CORS 
import validators
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
CORS(app)


openai.api_key = os.getenv("OPENAI_API_KEY")

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
        # max_tokens = 3000  
        # text = text[:max_tokens]

        prompt = f"Determine if the following news content is fake or real:\n\n{text}\n\nRespond with 'Fake' or 'Real'."
    
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use the appropriate model
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful assistant that detects fake news."
                },
                {
                    "role": "user", 
                    "content": prompt
                    }
            ]
        )
        
        result = response['choices'][0]['message']['content']
        print(result)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':  
   app.run(debug=True)