from flask import Flask, request, jsonify

app = Flask(__name__)
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]
cars = [
    {"num": 1, "name": "Honda", "Model": "Accourd", "Year": 2017},
    {"num": 2, "name": "KIA", "Model": "SportAge", "Year": 2023},
]


def _find_next_id():
    return max(country["id"] for country in countries) + 1


# Cars
@app.get("/cars")
def get_car():
    return jsonify(cars)


# Countries
@app.get("/countries")
def get_countries():
    return jsonify(countries)


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


@app.route('/')
def index():
    return "Welcome to API Webservices"


if __name__ == "__main__":
    app.run(debug=True)
