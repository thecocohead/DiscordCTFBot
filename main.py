import discord
from DiscordCTFlib import *
import re
import sys

client = discord.Client()


@client.event
async def on_ready():
    # Sets up the bot for usage- prints username and sets currently playing
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='!help'))


@client.event
async def on_message(message):
    # Main controls for the bot
    if message.author == client.user:  # Don't respond to ourselves
        return

    if message.content.startswith('!help'):  # Help menu
        await message.channel.send(
            'Help\n-------------\n`!event` Current event\n`!left` Time left in current event\n`!next` Upcoming events')

    if message.content.startswith('!event'):  # Returns current event
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        if isEvent() == "false":
            await message.channel.send(author + '- There is no current event.')
        else:
            await message.channel.send(author + '- The current event is: ' + isEvent())

    if message.content.startswith('!left'):  # Returns time left in current event
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        if startEnd() == -1:
            await message.channel.send(author + '- There is no current event.')
        else:
            await message.channel.send(author + '- There is ' + str(datetime.timedelta(seconds=startEnd()[1])) + ' left.')

    if message.content.startswith('!next'):  # Returns future events
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        await message.channel.send(author + '-\n' + nextEvent())


# test if discord token is in script
if len(sys.argv) == 1:
    print('Run script with your discord bot token!')
    sys.exit()

# login and start bot
client.run(str(sys.argv[1]))
