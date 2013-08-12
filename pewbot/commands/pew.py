from pewbot.base import PewbotCommand

class Command(PewbotCommand):
    help = "Say pew again, I dare you!"
    def handle(self, message, room_id):
        if 'pewbot' not in message: 
            if 'pew?' in message:
                return ["That's right I said pew muthafucka!"]
            if 'pew' in message:
                return ['pew!']
            if 'pork roll' in message:
                return ['http://s3.amazonaws.com/barkpost-assets/50+GIFs/7.gif', 'Did somebody say pork roll?']
            if 'coffee' in message:
                return ['https://lh5.googleusercontent.com/-MlDz2f26eqQ/UY8qz1syY_I/AAAAAAAAA4o/EWq1ENUb71Y/95ff6c96.gif', 'Did somebody say coffee?']
