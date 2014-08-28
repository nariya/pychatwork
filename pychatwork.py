# -*- coding: utf-8 -*-
# https://github.com/nariya/pychatwork
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
		print r.text
