import discord
from DiscordCTFlib import *
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        if isEvent() == "false":
            await message.channel.send(author + '- Use !event to see current event, !left to see current time left, and !next for the next event.')

    if message.content.startswith('!event'):
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        if isEvent() == "false":
            await message.channel.send(author + '- There is no current event.')
        else:
            await message.channel.send(author + '- The current event is: ' + isEvent())

    if message.content.startswith('!left'):
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        if leftInEvent() == "false":
            await message.channel.send(author + '- There is no current event.')
        else:
            await message.channel.send(author + '- There is ' + leftInEvent() + ' left.')
    if message.content.startswith('!next'):
        author = str(message.author)
        author = re.findall(r'.*(?=#)', author)[0]
        await message.channel.send(author + '-\n' + nextEvent())

client.run('token')