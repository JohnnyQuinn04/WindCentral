from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = "4744851151544ac1578cc038d586d99b"

    # List of cities for the dropdown
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'San Francisco', 'Charlotte', 'Indianapolis', 'Seattle', 'Denver', 'Washington',
              'Boston', 'Nashville', 'El Paso', 'Detroit', 'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Mesa', 'Atlanta', 'Kansas City', 'Colorado Springs', 'Miami', 'Raleigh',
              'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland', 'Minneapolis', 'Tulsa', 'Wichita', 'New Orleans', 'Arlington']


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
