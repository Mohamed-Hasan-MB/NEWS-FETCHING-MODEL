from flask import Flask, request, jsonify
from fetch_news import fetch_news_articles
from summarize import summarize_text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/summarize", methods=["POST"])
def summarize_route():
    data = request.get_json()
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    # Step 1: Fetch news articles
    articles = fetch_news_articles(topic)

    if not articles:
        return jsonify({"error": "No articles found"}), 404

    # Step 2: Combine all article content
    combined_text = " ".join([
        article.get("content", "") for article in articles if article.get("content")
    ])

    # Step 3: Summarize using Gemini
    summary = summarize_text(combined_text)

    # ✅ Return both articles and summary
    return jsonify({
        "articles": articles,
        "summary": summary
    })

if __name__ == "__main__":
    app.run(debug=True)
