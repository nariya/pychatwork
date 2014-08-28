# -*- coding: utf-8 -*-
from pychatwork import Chatwork
import os

#enter your chatwork token.
CHATWORK_TOKEN = os.environ['CHATWORK_TOKEN']

#enter your room id
CHATWORK_ROOM = os.environ['CHATWORK_ROOM']

c = Chatwork(CHATWORK_TOKEN)
message = u"""
you can use UTF-8 message 
　　　△　　￥　▲
　　（　㊤　皿　㊤）　　がしゃーん
　　（　　　　　　）　　　　　　
　／│　　肉　　│＼　　　　　　　　　がしゃーん
＜　　＼＿＿__／　　＞
　　　　┃　　　┃
　　　　＝　　　＝
chatworkロボだよ
chatwork.pyから自動でchatworkにつぶやけるすごいやつだよ
"""
c.send(CHATWORK_ROOM, message)
