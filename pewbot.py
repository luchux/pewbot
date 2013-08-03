#!/usr/bin/env python

from datetime import date
from time import sleep
import sys
import os

from importlib import import_module

from campsettings import *
from pinder import Campfire

class Pewbot(object):
    commands = []
    rooms = []
    campfire = None
    message_log = []
    first_run = True
    pewbot_userid = 1429837
    ignore_users = []

    def __init__(self, *kwargs, **args):
        self.campfire = Campfire(CAMPFIRE_DOMAIN, API_KEY)
        self.ignore_users.append(self.pewbot_userid)

        for room in CAMPFIRE_ROOMS:
            croom = self.campfire.room(room)
            croom.join()
            self.rooms.append(croom)

        self.commands = self._discover_commands()

        if 'test' in args:
            _handle_message('melbourne', None)
        else:
            while len(self.rooms) > 0:
                try:
                    self._fetch_messages()
                    sleep(2)   # have a rest, pewbot
                except Exception as e:
                    print e

    def _discover_commands(self):
        command_dir = os.path.join('./pewbot/', 'commands')
        try:
            commands = []
            for f in os.listdir(command_dir):
                if not f.startswith('_') and f.endswith('.py') and f not in 'base.py':
                    module = import_module('pewbot.commands.%s' % (f[:-3]))
                    commands.append(module.Command())
            return commands
        except OSError:
            return []

    def _fetch_messages(self):
        for room in self.rooms:
            for message in room.transcript(date.today()):
                if message['id'] not in self.message_log:
                    self.message_log.append(message['id'])
                    print self.first_run, message['user_id'], message['id'], message['type'], message['body']
                    self._handle_message(message, room)
        self.first_run = False       # so that we don't spam the room reading the transcript

    def _handle_message(self, message, room):
        body = message['body']
        if body == 'pewbot help me' and not self.first_run:
            self.help(room)
            return

        if not self.first_run and body and message['user_id'] not in self.ignore_users:
            for c in self.commands:
                try:
                    messages = c.handle(body)
                    if messages:
                        for m in messages:
                            room.speak(m)
                except Exception as e:
                    print e

    def help(self, room):
        help_messages = []
        for c in self.commands:
            help_message = c.help
            if len(help_message) > 0:
                room.speak(help_message)

if __name__ == '__main__':
    pewbot = Pewbot()
