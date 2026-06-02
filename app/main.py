from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "eks-production-platform",
        "status": "healthy",
        "host": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
