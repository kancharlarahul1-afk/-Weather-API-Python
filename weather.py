import requests
from datetime import datetime
from config import API_KEY
class WeatherClient:
    def report(self,city):
        u=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        r=requests.get(u,timeout=10);r.raise_for_status();d=r.json()
        s=datetime.fromtimestamp(d['sys']['sunrise']).strftime('%H:%M')
        ss=datetime.fromtimestamp(d['sys']['sunset']).strftime('%H:%M')
        out=f'''Weather Report
City: {d["name"]}
Temp: {d["main"]["temp"]} C
Feels Like: {d["main"]["feels_like"]} C
Humidity: {d["main"]["humidity"]}%
Pressure: {d["main"]["pressure"]} hPa
Wind: {d["wind"]["speed"]} m/s
Condition: {d["weather"][0]["description"]}
Sunrise: {s}
Sunset: {ss}'''
        open('logs/weather_log.txt','a').write(out+'\n\n')
        return out
