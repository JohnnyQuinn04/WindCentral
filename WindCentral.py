# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# @app.route("/")
# def index():
#     api_key = "4744851151544ac1578cc038d586d99b"
#     city = "London"
#     url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
#     response = requests.get(url)
#     data = response.json()
#     print(data)
#     temperature = data['current']['temperature']
#     wind_speed = data['current']['wind_speed']
#     # return render_template("Weather_Home.html", temperature=temperature, wind_speed=wind_speed,weather_descriptions=weather_descriptions)
# index()
# # if __name__ == "__main__":
# #     app.run(debug=True)
import requests

api_key = "4744851151544ac1578cc038d586d99b"
city = "London"

url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
response = requests.get(url)
data = response.json()

temperature = data['current']['temperature']
wind_speed = data['current']['wind_speed']
weather_descriptions = data['current']['weather_descriptions']

print(f"Current weather in {city}: {weather_descriptions[0]}. Temperature: {temperature}°C. Wind speed: {wind_speed} km/h.")
