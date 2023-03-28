let urlString = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
guard let url = URL(string: urlString) else {
    print("Invalid URL")
    return
}

let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
    if let error = error {
        print("Error: \(error.localizedDescription)")
        return
    }
    
    guard let data = data else {
        print("No data received")
        return
    }
    
    do {
        let json = try JSONSerialization.jsonObject(with: data, options: [])
        print("JSON: \(json)")
        // Parse the JSON and extract the weather data
    } catch {
        print("Error parsing JSON: \(error.localizedDescription)")
    }
}

task.resume()