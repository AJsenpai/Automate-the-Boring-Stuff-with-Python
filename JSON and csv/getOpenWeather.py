# Prints the weather for a location from the command line.


APPID = "197ce0f21c79a51b7743b1b98107a747"
import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = " ".join(sys.argv[1:])
# location = "Jaipur,IN"
print(location)

# Download the JSON data from OpenWeatherMap.org's API.
url = f"https://api.openweathermap.org/data/2.5/forecast/?q={location}&cnt=3&appid={APPID}"  # cnt = no. of days
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# print weather description
w = weatherData["list"]
# print(w)
print(f"Current weather in {location}")
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])


"""
Note: always check the API documnetation on website for API calls

https://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={your api key} # current weather
https://api.openweathermap.org/data/2.5/forecast/daily?q={city name},{state code},{country code}&cnt={cnt}&appid={your api key} # by days
https://api.openweathermap.org/data/2.5/forecast?q=Jaipur,IN&appid=197ce0f21c79a51b7743b1b98107a747
Parameters:
cnt number of days returned (from 1 to 16)
"""
