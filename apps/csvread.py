import csv
def read_csv():
    with open("world_cities\citys.csv", encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip header
        cities = []
        for row in csv_reader:
            cities.append(row[1]) # Append city name to list
            
    return cities
    