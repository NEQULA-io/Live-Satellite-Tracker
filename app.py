from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_N2YO_API_KEY_HERE"
SAT_ID = "NORAD_ID"
OBSERVER_LAT = 0
OBSERVER_LNG = 0
OBSERVER_ALT = 0
SECONDS = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/position")
def position():
    url = f"https://api.n2yo.com/rest/v1/satellite/positions/{SAT_ID}/{OBSERVER_LAT}/{OBSERVER_LNG}/{OBSERVER_ALT}/{SECONDS}/&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "positions" in data and data["positions"]:
            pos = data["positions"][0]
            return jsonify({
                "lat": pos["satlatitude"],
                "lng": pos["satlongitude"],
                "alt": pos["sataltitude"]
            })
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify({"error": "Unable to get position"})

if __name__ == "__main__":
    app.run(debug=True)
