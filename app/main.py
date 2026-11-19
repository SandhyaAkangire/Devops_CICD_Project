from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps CI/CD Project is running!"

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/version")
def version():
    return jsonify(version="1.0.0"), 200