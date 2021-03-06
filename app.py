import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def webhook():
  if request.method == 'POST':
    data = request.get_json()
    # We don't want to reply to ourselves!
    if data['name'] != 'Test Bot' and '!help' in data['text'].lower():
      msg = 'Hi {}! Every Monday at 6:30pm I will remind you all to take out the trash bins!'.format(data['name'])
      send_message(msg)

  if request.method == 'GET':
    print('App is awake')
    
  return "ok", 200

def format_message(data):
    formatted_msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    return formatted_msg

def send_message(msg):
    url     = 'https://api.groupme.com/v3/bots/post'
    payload = {          
                'bot_id' : os.getenv('GROUPME_BOT_ID'),
                'text'   : msg,
              }
    headers = {}
    res = requests.post(url, data=payload, headers=headers)