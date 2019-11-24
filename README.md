# DiscordCTFBot
[![Maintainability](https://api.codeclimate.com/v1/badges/d9f0f5d0ebe21d88410c/maintainability)](https://codeclimate.com/github/thecocohead/DiscordCTFBot/maintainability)

A bot made for keeping track of CTF competitions in Discord.

##What does this bot do?
These scripts automate announcements made on CTF discord servers. 
`main.py` handles user input and returns information based off an ical calendar linked in CalLib.py.
`notify.py` waits for a new event to start or end and notifies everyone when an event starts or ends. This also works off an ical calendar linked in CalLib.py.

##How to install
1. Install Python version >=3.7
2. Install discord.py. Typically, this can be done with `pip3 install discord.py`
3. Obtain a discord bot token & ical link.
4. Set `url` in CalLib to be your ical link.
5. Update `main_channel` in `notify.py` to your server's announcement channel id. [Check this link to get channel id.](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
5. Run `bot.sh`.
