import os
from discord.ext import commands
from libraries.console import Console

# Set up the bot
bot = commands.Bot(command_prefix = "!")

# Link cogs
bot.load_extension("libraries.cogs")

# Run the bot
C = Console()
try: bot.run(os.environ.get('SPARKY_TOKEN'))
except: C.Error("I can't get the TOKEN")
