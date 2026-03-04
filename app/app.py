from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def home():
    return "HelloOps 🚀 v1.0.2"

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/info")
def info():
    return jsonify(
        app="helloops",
        version=os.getenv("APP_VERSION", "dev"),
        time=datetime.utcnow().isoformat() + "Z"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)