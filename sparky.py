# Modules
import os
import discord
from discord.ext import commands
from libraries.console import Console
from libraries.queries import get_token

# Print the title to the console
os.system("cls")
C = Console()
C.title()

# Set up the bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command = None)

# Link cogs
try:
    for filename in os.listdir(f'{str(__file__)[:-9]}libraries/'):
        if filename.endswith('.py') and filename != "console.py" and filename != "queries.py":
            bot.load_extension(f"libraries.{filename[:-3]}")
except:
    C.Error("I was not able to load the cogs.")

# Run the bot
try: bot.run(get_token())
except: C.Error("I was not able to get the TOKEN.")
