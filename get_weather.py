from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found. Please try again."
    
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
