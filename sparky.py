import os
import discord
from discord.ext import commands
from libraries.console import Console
from libraries.help import CustomHelpCommand

# Print title to the console
os.system("cls")
C = Console()
C.title()

# Set up the bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command = CustomHelpCommand())

# Link cogs
try:
    for filename in os.listdir(f'{str(__file__)[:-9]}libraries/'):
        if filename.endswith('.py') and filename != "console.py" and filename != "help.py" and filename != "embeds.py":
            bot.load_extension(f"libraries.{filename[:-3]}")
except: C.Error("Cogs aren't loaded in successfully.")

# Run the bot
try: bot.run(os.environ.get('SPARKY_TOKEN'))
except: C.Error("I can't get the TOKEN")
