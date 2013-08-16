import requests
from pewbot.base import PewbotCommand
from xml.dom import minidom

APBASE_URL = "http://api.wolframalpha.com/v2/query?input="
P_ID = "449APJ-RJ8HAK69WK"


class Command(PewbotCommand):
    help = "Lets ask heaps of freaky shits to wolfram alpha!"
    def handle(self, message, room_id):
        if 'pewbot wolfram' in message:
            tokens = message.split(' ')
            if len(tokens)>2:
                query = tokens[2:]
                url =
                r = requests.get(BASE_URL + query + "&appid=" + APP_ID)
                print r.text
