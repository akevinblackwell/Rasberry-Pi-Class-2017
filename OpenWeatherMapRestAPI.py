import requests
import json

def get_city_weather(city, appid):
    payload = {"q":city, "appid":appid}
    r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
    j = json.loads(r.text)
    return j

targetcity = ""

while targetcity != "QUIT":
    targetcity = input('Target City or "Quit": ')

    appid = '4906b9aabdf6475230e1c5780d988d01'
    WeatherThere = get_city_weather(targetcity, appid)

    print('All: ', WeatherThere)
#    print('==========================================================')
#    print('Weather for:  ', WeatherThere['name'])
#    print('Coordinates: LAT', WeatherThere['coord']['lon'])
#    print('             LON', WeatherThere['coord']['lat'])
#    print('Current Conditions:', WeatherThere['weather'][0]['main'], ' - ', WeatherThere['weather'][0]['description'])
#    print('Readings: ', '    Current Temp:',"{:+.2f}".format((WeatherThere['main']['temp']-273)*1.8 + 32), 'degF')
#    print('           Current Pressure:', WeatherThere['main']['pressure'],'hpa')
#    print('           Current Humidity:', WeatherThere['main']['humidity'],'%')
#    print('                    Hi Temp:', "{:+.2f}".format((WeatherThere['main']['temp_max']-273)*1.8 + 32),'degF')
#    print('                    Lo Temp:', "{:+.2f}".format((WeatherThere['main']['temp_min']-273)*1.8 + 32),'degF')
#    print('                 Visibility:', "{:.0f}".format(WeatherThere['visibility']* 0.000621371),'miles')
#    print('                 Wind Speed:', "{:.2f}".format(WeatherThere['wind']['speed']/0.621371),"MPH")
#    print('             Wind Direction:', WeatherThere['wind']['deg'])
#    print('==========================================================')
#    print('')

#print('All: ', WeatherThere)