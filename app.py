from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_key = "4744851151544ac1578cc038d586d99b"
    city = "London"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    data = response.json()

    weather_description = data['current']['weather_descriptions'][0]
    temperature = data['current']['temperature']
    wind_speed = data['current']['wind_speed']
    wind_direction = data['current']['wind_dir']
    pressure = data['current']['pressure']
    precipitation = data['current']['precip']
    humidity = data['current']['humidity']
    cloud_cover = data['current']['cloudcover']
    feels_like = data['current']['feelslike']
    uv_index = data['current']['uv_index']
    visibility = data['current']['visibility']
    is_day = data['current']['is_day']

    return render_template('index.html', weather_description=weather_description,
                                          temperature=temperature,
                                          wind_speed=wind_speed,
                                          wind_direction=wind_direction,
                                          pressure=pressure,
                                          precipitation=precipitation,
                                          humidity=humidity,
                                          cloud_cover=cloud_cover,
                                          feels_like=feels_like,
                                          uv_index=uv_index,
                                          visibility=visibility,
                                          is_day=is_day)

if __name__ == '__main__':
    app.run()