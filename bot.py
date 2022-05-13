# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['15397707']
some_api_token = os.environ['c9cddaf32ac057b866abcf3b77397f8e']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(5369469717)
some_api = some_api_lib.connect(AAHdzXg0Z5aoqod_JN0tVTrc2iOdqr4AlDA)
#              ...
