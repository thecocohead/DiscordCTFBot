import discord
import time
import sys
from DiscordCTFlib import *

main_channel = 0
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    channel = client.get_channel(main_channel)
    await channel.send(":triangular_flag_on_post: It's CTF Time @players! Event has started: " + isEvent())
    #TODO: Make bot work multiple times
    time.sleep(timeToNextPing())
    await channel.send(":triangular_flag_on_post: We are done @players! Event has ended: " + isEvent())
    sys.exit()
while True:
    if isEvent()!="false":
        client.run('token')
    else:
        print("no event")
        time.sleep(30)