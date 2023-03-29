from flask import Flask, render_template, request
import requests
import csv
import csvread

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def read_csv():
    with open("world_cities\citys.csv", encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip header
        cities = []
        for row in csv_reader:
            cities.append(row[1]) # Append city name to list
        return cities


def index():
    api_key = "4744851151544ac1578cc038d586d99b"

    # List of cities for the dropdown
    # cities = read_csv("WindCentral\citys.csv")
    cities = []
    cities.append(read_csv())  

    if request.method == 'POST':
        # Get the selected city from the form
        city = request.form['city']
    else:
        # Default city if no city selected yet
        city = "London"

    # Make the API request with the selected city
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
                                          is_day=is_day,
                                          cities=cities,
                                          selected_city=city)

if __name__ == '__main__':
    app.run()
