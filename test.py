import requests

url = "http://127.0.0.1:5000/summarize"
payload = {
    "topic": "India"
}

response = requests.post(url, json=payload)
print(response.json())
# This code sends a POST request to the Flask app running on localhost
# with a topic to summarize. It prints the JSON response from the server.