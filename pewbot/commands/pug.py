from pewbot.base import PewbotCommand
import requests
import json

class Command(PewbotCommand):
    help = "pewbot pug me - post a picture of a pug"
    def handle(self, message, room_id):
        if message.startswith('pewbot pug me'):
            try:
                response = []
                num = int(message.split("pewbot pug me")[1])
                for x in range(num):
                    response.append(requests.get('https://pugme.herokuapp.com/random').json()['pug'])
                return response
            except:
                # who cares?
                pass
            return [requests.get('https://pugme.herokuapp.com/random').json()['pug']]
