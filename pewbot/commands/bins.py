from pewbot.base import PewbotCommand
from datetime import datetime

dayValue = 1 # Monday
startHour = 4 # 4am

class Command(PewbotCommand):
    """Could slash should be a reminder bot script
    """
    help = "Robot Bin Reminder: Reminds people to put the bins out"
        "every hour. When they are out type: yes the bins are out"
    def handle(self, message, room_id):
        if 'pewbot' not in message and str(room_id) in ["455251",]:
            dt = datetime.now()
            if dt.isoweekday() == dayValue:
                if dt.hour == startHour:
                    # reset the state
                    self.binState = False
                    self.hour = dt.hour
                if dt.hour >= startHour and self.binState is False:
                    # reminder per hour
                    if self.hour != dt.hour:
                        self.hour = dt.hour
                        return ["ARE THE BINS OUT YET??"]
            if 'yes the bins are out' == message:
                self.binState = True
                return ['Bins are out. May the force be with you. Pew']

