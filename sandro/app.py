import os
import requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/llm", methods=["POST"])
def llm():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return jsonify({"error": "GROQ_API_KEY nao definida no ambiente"}), 500

    data = request.get_json(force=True)
    payload = {
        "model": MODEL,
        "messages": data.get("messages", []),
        "temperature": data.get("temperature", 0.7),
        "max_tokens": data.get("max_tokens", 300),
    }
    if data.get("json_mode"):
        payload["response_format"] = {"type": "json_object"}

    try:
        r = requests.post(
            GROQ_URL,
            json=payload,
            headers={"Authorization": f"Bearer {key}"},
            timeout=30,
        )
        r.raise_for_status()
        text = r.json()["choices"][0]["message"]["content"]
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
