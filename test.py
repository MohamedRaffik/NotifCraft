import json
import requests

notify_json = json.load(open("./test_responses/test_movie.json", "r"))

response = requests.post("http://localhost:5000/notify/jellyfin", json=notify_json)
response.raise_for_status()
