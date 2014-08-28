# -*- coding: utf-8 -*-
import requests
#import argparse
#import datetime

class Chatwork:

	def __init__(self, token):
		self.token = token
#		self.start_time = datetime.datetime.now()
		self.apiurl = u'https://api.chatwork.com/v1/'

	def send(self, roomid, message):
		url = (self.apiurl + u'rooms/{}/messages').format(roomid)
		payload = {'body': message}
		headers = {'X-ChatworkToken': self.token}
		r = requests.post(url, params=payload, headers=headers)
		print r.text
