"""This is a simple Flask application."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Return a greeting message"""
    return render_template("index.htlml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)