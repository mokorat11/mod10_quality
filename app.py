"""This is a simple Flask application."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Return a greeting message"""
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)