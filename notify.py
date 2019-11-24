#!/usr/bin/env python3

import discord
import time
import sys
import os
from CalLib import *

main_channel = 646239853893124097 # Your CTF team's announcement channel
delay = 30 # Time between checking for a new event
debug = False # If true, prints debug statements.
client = discord.Client()


@client.event
async def on_ready():
    # print and set channel to say to
    print('Logged in as {0.user}'.format(client))
    channel = client.get_channel(main_channel)
    # upon event start, print start message
    if debug:
        print("start")
    if startEnd()[0]<delay*2:
        await channel.send(":triangular_flag_on_post: It's CTF Time @everyone! Event has started: " + isEvent())
    elif debug:
        print("not printed due to delay")
    print(startEnd()[1])
    time.sleep(startEnd()[1])  # sleep till event end
    # Print ending message
    if debug:
        print("end")
    await channel.send(":triangular_flag_on_post: We are done @everyone! Event has ended: " + isEvent())
    time.sleep(delay*2)
    os.execl('notify.py', 'notify.py', sys.argv[1])

# test if discord token is in script
if len(sys.argv) == 1:
    print('Run script with your discord bot token!')
    sys.exit()

# Check every x seconds for an event
while True:
    if isEvent() != "false":
        client.run(str(sys.argv[1]))
    else:
        time.sleep(delay)
        if debug:
            print("delay")