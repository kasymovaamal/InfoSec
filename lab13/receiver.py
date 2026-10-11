from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

RECV_FILE = "received_logs.txt"

@app.route("/receive", methods=["POST"])
def receive():
    data = request.get_json(silent=True) or {}
    content = data.get("content", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(RECV_FILE, "a") as f:
        f.write(content)

    print(f"[+] Received '{content}' at {timestamp}")
    return jsonify({"message": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=9000)
