import os
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests

cid = 1163475412056293466


token = os.environ['token']
editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")
import time
import random

client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False
@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(cid)
 # print(text_channel)
  if text_channel != None:
   # words = ["gaeming","om","ap","harry","nato"]
    #print(x)
    num = random.randint(1,10000000000000000000000000)
    await text_channel.send(num)
    intervals = [2.0, 2.1, 2.2, 2.3, 2.4]
    await asyncio.sleep(random.choice(intervals))

@tasks.loop(seconds=14400)
async def sleeper():
  time.sleep(seconds = 3600)
  spammer.start()
#pokes = ['pikachu','charixadd','swellow','pidove',input('option')]
spammer.start()

@client.command()
async def stop(ctx):
    spammer.stop()

@client.command()
async def spam(ctx):
  spammer.start()

keep_alive()
client.run(token,bot=False)