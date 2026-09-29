import requests
from flask import Flask, render_template, jsonify
from configure import WEATHER_API_KEY

CITY = "Лондон"

app = Flask(__name__)
app.json.ensure_ascii = False

# Получаем данные о погоде
def weather():
    params = {
    "key": WEATHER_API_KEY, 
    "q": CITY, 
    "lang": "ru"
    }

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params,
        timeout=10
    )
    data = response.json()
    our_data = {
        "city": data["location"]["name"],
        "timezone": data["location"]["tz_id"],
        "temp": round(data["current"]["heatindex_c"]),
        "text": data["current"]["condition"]["text"],
        "feels": data["current"]["feelslike_c"]
    }
    return our_data

@app.route("/")
def index():
    return render_template("index.html", w=weather())

@app.route("/api/weather")
def api():
    return jsonify(weather())

app.run(debug=True, port=5004)
