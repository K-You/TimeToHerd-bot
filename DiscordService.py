from time import sleep

import requests
import yaml


class DiscordService():
  def __init__(self):

    with open(r'./properties.yml') as file:
      properties = yaml.full_load(file)
      self.DISCORD_HOOK = properties['discord']['hook']

  def send(self, message) :
    payload = {
      "content": message,
      "attachments": [{ 
        "fallback": "Oupsie !", 
        "image_url": "https://timetoherd.com/covid-19.jpg"
      }]
    }
    result = requests.post(self.DISCORD_HOOK, json=payload, headers={'Content-Type': 'application/json'})
