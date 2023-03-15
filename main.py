from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to API Webservices"


if __name__ == "main":
    app.run(debug=True)