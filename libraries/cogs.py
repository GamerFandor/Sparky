import os
import discord
from discord.ext import commands
from console import Console

class Cog(commands.Cog):
    C = None
    
    def __init__(self, bot):
        self.bot = bot
        self.C = Console()
        
    @commands.Cog.listener()
    async def on_ready(self):
        # Feedback on console
        os.system("cls")
        self.C.Success("All systems are fully operational.")
        
        # Set custom activity
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you 😈"))

def setup(bot):
    bot.add_cog(Cog(bot))
    