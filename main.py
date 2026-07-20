from weather import WeatherClient
city=input('Enter city: ')
print(WeatherClient().report(city))
