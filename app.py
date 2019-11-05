import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'Test Bot' and '!help' in data['text'].lower():
    msg = 'Hi {}! Every Monday at 7pm I will remind you all to take out the trash bins!'.format(data['name'])
    send_message(msg)

  return "ok", 200

def format_message(data):
    formatted_msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    return formatted_msg

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
            'bot_id' : os.getenv('GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()