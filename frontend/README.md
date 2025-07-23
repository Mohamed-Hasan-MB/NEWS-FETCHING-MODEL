🗞️ News Fetching App
A full-stack application that fetches the latest news articles based on a user’s query using a Python backend and a React frontend. Summarization is handled via a third-party API (e.g., Gemini or OpenAI).

📁 Project Structure

News Fetching Model/
├── Backend/               # Python backend (Flask)
│   ├── app.py             # Main Flask app
│   ├── fetch_news.py      # News fetching logic
│   ├── summarize.py       # Summarization using Gemini/OpenAI
│   ├── test.py            # Script for testing
│   └── .env               # API keys (ignored in .gitignore)
├── frontend/              # React frontend
│   ├── public/
│   └── src/
├── .gitignore
└── README.md

🚀 Features

🔍 Fetches latest news based on a search term.

✂️ Summarizes long news using LLM APIs.

🖥️ Simple and responsive React frontend.

🧠 Clean modular backend using Flask.

📦 Tech Stack

Frontend: React.js

Backend: Python (Flask)

APIs: News API, Gemini / OpenAI for summarization

Other: Git, .env, Node.js, npm

🔧 Setup Instructions
Backend
cd Backend
python -m venv venv
venv\Scripts\activate        # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
python app.py
Frontend
cd frontend
npm install
npm start

🌐 Usage

Start backend (localhost:5000)
Start frontend (localhost:3000)

Enter a keyword, click "Fetch News"

View summarized headlines and articles

📁 .env (example)
ini
NEWS_API_KEY=your_news_api_key
GEMINI_API_KEY=your_gemini_api_key

📜 License
MIT License — feel free to use, modify, and share.