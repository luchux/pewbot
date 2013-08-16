from pewbot.base import PewbotCommand

class Command(PewbotCommand):
    help = "Say pew again, I dare you!"
    def handle(self, message, room_id):
        if 'pewbot' not in message: 
            if 'pew' in message:
                return ['pew!']
