# DiscordCTFBot
[![Maintainability](https://api.codeclimate.com/v1/badges/d9f0f5d0ebe21d88410c/maintainability)](https://codeclimate.com/github/thecocohead/DiscordCTFBot/maintainability)

A bot made for keeping track of CTF competitions in Discord.
###What does this bot do?
These scripts automate many announcements made on ctf discord guilds. 

main.py handles user input and returns information based off a google calendar linked in DiscordCTFlib.py.

notify.py waits for a new event to start or end and notifies everyone when an event starts or ends. This also works off a google calendar linked in DiscordCTFlib.py.

###How to install
In order for the bot to work correctly, both scripts must be ran. Run `main.py` and `notify.py` in the command line with your discord bot token as the first argument. Add your google calendar to the DiscordCTFlib.py file and run both scripts.