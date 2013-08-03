
class PewbotMeta(type):
    def __repr__(self):
        if getattr(self, '__str__', False):
            return str(self)
        else:
            return self.__class__.__name__

class PewbotCommand(object):
    __metaclass__ = PewbotMeta
    help = ""

    def handle(self, message):
        """
        handle() should return either a list of messages to be sent
        to the room, or None
        """
        return []

    def help(self):
        """
        Returns a string telling people what's up
        """
        return self.help