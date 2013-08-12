from pewbot.base import PewbotCommand
import time

TOWN_RADAR = {
    'melbourne': '023',
    'geelong': '023',
    'collingwood': '023',
    'abbotsford': '023',
    'portland': '143',
    'robe': '143',
    'adelaide': '643',
    'sydney': '713',
    'hobart': '763',
    'launceston': '523',
    'brisbane': '663',
    'perth': '703'
}
class Command(PewbotCommand):
    def handle(self, message, room_id):
        radar_id = None
        message = message.lower()
        if message.startswith('pewbot radar'):
            words = message.split(" ")
            if len(words) > 2:
                town = words[2]
                radar_id = TOWN_RADAR.get(town, None)
                if 'wide' in words:
                    radar_id = radar_id[:2] + '1'
            if radar_id:
                return ['http://www.bom.gov.au/radar/IDR%s.gif?%s' % (radar_id, str(time.time()).replace(".",""))]
            else:
                return ["I don't know about that city, choices are: %s" % ", ".join(TOWN_RADAR.keys())]
