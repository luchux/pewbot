from pewbot.base import PewbotCommand
import campsettings

import requests

TOWN_LAT_LNG = {
    'melbourne': '-37.8139,144.9634',
    'geelong': '-38.1485,144.3602'
}
class Command(PewbotCommand):
    help = "get the current weather for melbourne"
    def handle(self, message, room_id):
        if message.startswith('pewbot forecast'):
            words = message.split(' ')
            if len(words) > 2:
                town = words[2]
                if town in TOWN_LAT_LNG.keys():
                    api_key = getattr(campsettings, 'FORECAST_API_KEY', None)
                    lat_lng = TOWN_LAT_LNG.get(town)
                    url = "https://api.forecast.io/forecast/{}/{}".format(api_key, lat_lng)
                    response = requests.get(url).json()
                    return ["It's currently {} ({:.2f}C)".format(response['currently']['summary'], (float(response['currently']['temperature']) - 32) * (5.0 / 9.0) )]
