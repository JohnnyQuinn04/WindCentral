from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

# def read_csv():
#     with open("world_cities\citys.csv", encoding='utf-8') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader) # Skip header
#         cities = []
#         for row in csv_reader:
#             cities.append(row[1]) # Append city name to list
#         return cities


def index():
    api_key = "fab82b38f04168391a45abcb24338382"

    # List of cities for the dropdown
    # cities = read_csv("WindCentral\citys.csv")
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 
              'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'San Francisco', 'Charlotte', 'Indianapolis', 
              'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'El Paso', 'Detroit', 'Memphis', 'Portland', 'Oklahoma City', 
              'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 'Sacramento', 'Atlanta', 
              'Kansas City', 'Colorado Springs', 'Miami', 'Raleigh', 'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland', 'Minneapolis', 
              'Tulsa', 'Wichita', 'New Orleans', 'Arlington', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St. Louis', 'Pittsburgh', 
              'Corpus Christi', 'Riverside', 'Cincinnati', 'Lexington', 'Anchorage', 'Stockton', 'Toledo', 'Saint Paul', 'Newark', 'Greensboro', 
              'Buffalo', 'Plano', 'Lincoln', 'Henderson', 'Fort Wayne', 'Jersey City', 'St. Petersburg', 'Chula Vista', 'Norfolk', 'Orlando', 
              'Chandler', 'Laredo', 'Madison', 'Winston-Salem', 'Lubbock', 'Baton Rouge', 'Durham', 'Garland', 'Glendale', 'Reno', 'Hialeah', 
              'Chesapeake', 'Scottsdale', 'North Las Vegas', 'Irving', 'Fremont', 'Irvine', 'Birmingham', 'Rochester', 'San Bernardino', 
              'Spokane', 'Gilbert', 'Arlington', 'Montgomery', 'Boise', 'Richmond', 'Des Moines', 'Modesto', 'Fayetteville', 'Shreveport', 
              'Akron', 'Augusta', 'Grand Rapids', 'Huntsville', 'Salt Lake City', 'Mobile', 'Knoxville', 'Tallahassee', 'Worcester', 'Tempe', 
              'Grand Prairie', 'Brownsville', 'Overland Park', 'Santa Clarita', 'Providence', 'Garden Grove', 'Chattanooga', 'Oceanside', 
              'Jackson', 'Fort Lauderdale', 'Santa Rosa', 'Rancho Cucamonga', 'Port St. Lucie', 'Temecula', 'Ontario', 'Vancouver', 'Cape Coral',
                'Sioux Falls', 'Springfield', 'Peoria', 'Pembroke Pines', 'Elk Grove', 'Salem', 'Lancaster', 'Corona', 'Palmdale', 'Salinas', 
                'Alexandria', 'Lafayette', 'Sterling Heights', 'New Haven', 'Fullerton', 'Mesquite', 'Sunnyvale', 'Miramar', 'Waco', 'Thornton', 
                'West Valley City', 'Manhattan', 'Midland', 'Charleston', 'Denton', 'Carrollton', 'Surprise', 'Roseville', 'Daly City', 
                'College Station', 'Berkeley', 'Columbia', 'Independence', 'Redding', 'Livermore', 'Waterbury', 'Costa Mesa', 'Portsmouth', 
                'Downey', 'Clearwater', 'Westminster', 'Fairfield',]
    cities.sort()
    # cities.append(read_csv())  
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
