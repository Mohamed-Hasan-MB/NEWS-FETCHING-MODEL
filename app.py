from flask import Flask, request, jsonify
from fetch_news import fetch_news_articles
from summarize import summarize_text

app = Flask(__name__)
@app.route("/summarize", methods=["POST"])
def summarize_route():
    data = request.get_json()
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    # Step 1: Fetch news
    articles = fetch_news_articles(topic)

    # Step 2: Combine all article text
    combined_text = " ".join([article["content"] for article in articles if article["content"]])

    # Step 3: Summarize
    summary = summarize_text(combined_text)

    return jsonify({
        "summary": summary,
        "articles_found": len(articles)
    })
if __name__ == "__main__":
    app.run(debug=True)
