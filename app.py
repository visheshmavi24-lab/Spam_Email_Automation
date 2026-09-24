from flask import Flask, request, jsonify, render_template
from spam_detector import detect_spam

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check-email", methods=["POST"])
def check_email():

    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({
            "error": "Please provide email text."
        }), 400

    email_text = data["email"]

    if not isinstance(email_text, str) or not email_text.strip():
        return jsonify({
            "error": "Email text cannot be empty."
        }), 400

    result = detect_spam(email_text)

    return jsonify({
        "email": email_text,
        **result
    })


if __name__ == "__main__":
    app.run(debug=True)