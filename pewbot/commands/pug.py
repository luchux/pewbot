from pewbot.base import PewbotCommand
import requests
import json

class Command(PewbotCommand):
    help = "pewbot pug me - post a picture of a pug"
    def handle(self, message, room_id):
        if message.startswith('pewbot pug me'):
            return [requests.get('https://pugme.herokuapp.com/random').json()['pug']]
