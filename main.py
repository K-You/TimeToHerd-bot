from time import sleep

from DiscordService import DiscordService
from TimeToHerdBot import TimeToHerdBot

if __name__ == '__main__':
  tthBot = TimeToHerdBot()
  tthBot.gotToMain()
  tthBot.clickDropdown()

  days = tthBot.collectValue()
  country = tthBot.COUNTRY

  discord = DiscordService()
  discord.send("Remaining "+days+" before herd immunity in "+country)
  
