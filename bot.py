import discord
from discord.ext import commands

# Set up the bot
bot = commands.Bot(command_prefix = "!")

# Link cogs
bot.load_extension("libraries.cogs")

# Run the bot
bot.run("OTExMzE5NDg0NjQ2NjkwODM2.YZfqaA.LY0dLGdZHtQwjbPF-EddM7Qb9R4")
