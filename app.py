from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/joke", methods=["GET"])
def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json().get("value")
        return jsonify({"joke": joke})
    else:
        return jsonify({"error": "Could not fetch joke"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)