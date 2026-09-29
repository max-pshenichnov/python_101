import requests
from flask import Flask, render_template, jsonify, request
from configure import WEATHER_API_KEY

CITY = "Лондон"


def get_weather_emoji(condition):
    """Return a readable emoji for a WeatherAPI condition."""
    condition = condition or {}
    code = str(condition.get("code", ""))
    text = str(condition.get("text", "")).casefold()

    # Use the numeric code for the main conditions so the result does not
    # depend on the language selected for the API response.
    if code == "1000":
        return "☀️"
    if code == "1003":
        return "⛅"
    if code in {"1006", "1009"}:
        return "☁️"
    if code == "1030":
        return "🌫️"

    # The text is localized by the API. These fallbacks cover localized
    # conditions and keep the mapping useful if a condition code is unknown.
    if any(word in text for word in ("thunder", "storm", "гроз", "шторм")):
        return "⛈️"
    if any(word in text for word in ("sleet", "ice pellets", "freezing", "лёд", "лед", "мокрый снег", "слякоть")):
        return "🧊"
    if any(word in text for word in ("snow", "blizzard", "снег", "метель", "снегопад")):
        return "🌨️"
    if any(word in text for word in ("rain", "drizzle", "shower", "дожд", "морос")):
        return "🌧️"
    if any(word in text for word in ("mist", "fog", "haze", "туман", "дымк")):
        return "🌫️"
    if any(word in text for word in ("partly", "перемен")):
        return "⛅"
    if any(word in text for word in ("cloud", "overcast", "облач", "пасмур")):
        return "☁️"
    if any(word in text for word in ("sunny", "clear", "ясно", "солнеч")):
        return "☀️"

    return "🌡️"


app = Flask(__name__)
app.json.ensure_ascii = False


class WeatherAPIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code


# Получаем данные о погоде
def weather(city=CITY):
    city = city.strip() or CITY
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "lang": "ru"
    }

    try:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        condition = data["current"]["condition"]
        our_data = {
            "city": data["location"]["name"],
            "timezone": data["location"]["tz_id"],
            "temp": round(data["current"]["heatindex_c"]),
            "text": condition["text"],
            "emoji": get_weather_emoji(condition),
            "feels": data["current"]["feelslike_c"]
        }
        return our_data
    except requests.HTTPError as error:
        if response.status_code == 400:
            message = "Город не найден. Проверьте название и попробуйте ещё раз."
            status_code = 400
        else:
            message = "Сервис погоды временно недоступен. Попробуйте позже."
            status_code = 502
        raise WeatherAPIError(message, status_code) from error
    except (requests.RequestException, ValueError) as error:
        raise WeatherAPIError(
            "Не удалось получить данные о погоде. Попробуйте позже.",
            status_code=503
        ) from error


def get_city():
    return request.args.get("city", CITY).strip() or CITY


def weather_error_response(city, error):
    if request.path.startswith("/api/"):
        return jsonify({"error": str(error)}), error.status_code
    return render_template(
        "index.html", city=city, error=str(error)
    ), error.status_code


@app.route("/")
def index():
    city = get_city()
    try:
        w = weather(city)
    except WeatherAPIError as error:
        return weather_error_response(city, error)
    return render_template("index.html", w=w, city=city)


@app.route("/api/weather")
def api():
    city = get_city()
    try:
        return jsonify(weather(city))
    except WeatherAPIError as error:
        return weather_error_response(city, error)


app.run(debug=True, port=5004)

