from flask import Flask, jsonify

app = Flask(__name__)

status = {
    "front_danger": False,
    "rear_danger": False,
    "mode": "AUTO"
}

@app.route("/status")
def get_status():
    return jsonify(status)

@app.route("/")
def home():
    return "SMART VEHICLE SYSTEM ACTIVE"

app.run(host="0.0.0.0", port=5000)
