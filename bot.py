import discord
from discord.ext import commands
from libraries.jsonloader import load

# Set up the bot
bot = commands.Bot(command_prefix = load("databases/botdata.json", "prefix"))

# Link cogs
bot.load_extension("libraries.cogs")

# Run the bot
bot.run(load("databases/botdata.json", "TOKEN"))
