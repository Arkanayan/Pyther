import requests, json

#city = input("Please enter the city: ")

def checkWeather(city_name):
    base_openweather_url = "http://api.openweathermap.org/data/2.5/weather?appid=0fdaec5a050be4cba14364f15b1ffe29&units=metric&q="

    final_api_url = base_openweather_url + city_name

    result = requests.get(final_api_url)

    # if result.status_code == 200:
    #     res_json = result.json()
    #     print("Weather forcast for {}".format(res_json['name']))
    #     print("Temp: {}°C".format(res_json['main']['temp']))
    #     print("Pressure: {} hPa".format(res_json['main']['pressure']))
    #     print("Humidity: {}%".format(res_json['main']['humidity']))
    # elif result.status_code == 404 or result.status_code == 502:
    #     print("Sorry, the city {} is not found.".format(city))

    if result.status_code == 200:
        res_json = result.json()
        long = res_json['coord']['lon']
        lat = res_json['coord']['lat']
        localtime = getLocalTime(lat, long)
        return res_json['main']['temp'], res_json['main']['pressure'], res_json['main']['humidity'], localtime
    else:
        return None, None, None, None

def getLocalTime(lat, long):
    base_url = "http://api.timezonedb.com/v2/get-time-zone?key=EFCY78UBD21D&by=position&format=json&"
    api_url = base_url + "lng=" + str(long) + "&lat=" + str(lat)
    result = requests.get(api_url)
    if result.status_code == 200:
        result_json = result.json()
        if result_json['status'] == 'OK':
            return result_json['formatted']
    return None