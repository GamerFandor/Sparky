import os
import discord
from discord.ext import commands
from libraries.jsonloader import load

# os.getcwd()

# Set up the bot
bot = commands.Bot(command_prefix = load(__file__.replace("\\", "/").replace("bot.py", "") + "/databases/botdata.json", "prefix"))

# Link cogs
bot.load_extension("libraries.cogs")

# Run the bot
bot.run(load(__file__.replace("\\", "/").replace("bot.py", "") + "/databases/botdata.json", "TOKEN"))
