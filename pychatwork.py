# -*- coding: utf-8 -*-
# https://github.com/nariya/pychatwork
from __future__ import print_function
import requests


class Chatwork:
    def __init__(self, token):
        self.token = token
        self.apiurl = u'https://api.chatwork.com/v1/'

    def send(self, roomid, message):
        url = (self.apiurl + u'rooms/{}/messages').format(roomid)
        payload = {'body': message}
        headers = {'X-ChatworkToken': self.token}
        r = requests.post(url, params=payload, headers=headers)
        return r.text

    def read(self, roomid, force=0):
        url = (self.apiurl + u'rooms/{}/messages').format(roomid)
        payload = {'force': force}
        headers = {'X-ChatworkToken': self.token}
        r = requests.get(url, params=payload, headers=headers)
        return r.text

    def getme(self):
        url = self.apiurl + u'me'
        headers = {'X-ChatworkToken': self.token}
        r = requests.get(url, headers=headers)
        return r.text
