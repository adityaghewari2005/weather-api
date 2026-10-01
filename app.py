from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Weather API is running!",
        "status": "success"
    })

@app.route("/weather")
def weather():
    return jsonify({
        "city": "Pune",
        "temperature": "28°C",
        "condition": "Cloudy",
        "humidity": "70%"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)