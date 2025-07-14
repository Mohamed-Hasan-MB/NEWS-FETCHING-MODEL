import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Generative Model
model = genai.GenerativeModel("models/gemini-1.5-pro")
def summarize_text(text):
    if not text.strip():
        return "No content to summarize."

    try:
        prompt = f"Summarize the following news article:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error during summarization: {str(e)}"