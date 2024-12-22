# Fake News Detector

A web application to classify news articles as fake or real. The app uses a React frontend and a Flask backend, integrated with OpenAI's GPT API for processing and classifying news content. A video background enhances the visual appeal of the interface.

---

## Features
- **News URL Classification**: Submit a news URL to determine whether it's fake or real.
- **AI-Powered**: Leverages OpenAI's GPT model for intelligent analysis.
- **Video Background**: A visually appealing video plays in the background of the application.
- **Responsive Design**: The application is styled using Tailwind CSS for a modern and responsive interface.

---

## Technologies Used

### Frontend:
- **React**: For building the user interface.
- **Tailwind CSS**: For styling the application.

### Backend:
- **Flask**: Python-based backend framework.
- **OpenAI API**: GPT model for processing and classifying news content.

---

## Installation and Setup

### Prerequisites
- **Node.js**: Install from [Node.js Official Site](https://nodejs.org/).
- **Python 3.9+**: Install from [Python Official Site](https://www.python.org/).

### Backend Setup
1. Clone the repository and navigate to the backend folder:
   ```bash
   git clone https://github.com/mo-abdulai/fake-news-detector.git
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```
5. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

---

## Usage
1. Open your browser and navigate to `http://localhost:3000`.
2. Enter a news article URL in the input field.
3. Submit the form to classify the news article.
4. View the result displayed below the form.

---

## Project Structure
```
project-directory/
|-- backend/
|   |-- app.py                # Flask backend logic
|   |-- requirements.txt      # Backend dependencies
|   |-- .env                  # OpenAI API key
|   |-- ...
|
|-- frontend/
|   |-- src/
|   |   |-- App.js           # Main React component
|   |   |-- index.js         # React entry point
|   |   |-- assets/          # Video and other assets
|   |   |-- ...
|   |-- tailwind.config.js   # Tailwind CSS configuration
|   |-- ...
```

---

## Screenshots
### Home Page
![Home Page]()

---

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [OpenAI](https://openai.com/) for the GPT model.
- [Tailwind CSS](https://tailwindcss.com/) for the styling framework.

---

## Contact
For any questions or suggestions, feel free to reach out:
- Email: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [YourGitHubProfile](https://github.com/YourGitHubProfile)

