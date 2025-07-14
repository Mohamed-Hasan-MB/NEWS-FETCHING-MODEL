import requests

response = requests.post(
    "http://localhost:5000/summarize",
    json={"topic": "F1"}
)
print(response.json())
