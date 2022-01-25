import os
import sys
import discord
from discord.ext import commands
try: from libraries.console import Console    
except: from console import Console
   
class Cog(commands.Cog):
    C = None
    
    def __init__(self, bot):
        self.bot = bot
        self.C = Console()
    
    # Events --------------------------------    
    @commands.Cog.listener()
    async def on_ready(self):
        # Feedback on console
        os.system("cls")
        self.C.title()
        self.C.Success("All systems are fully operational.")
        
        # Set custom activity
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you 😈"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.message.author.mention}! Please pass in all required arguments! If something doesn't work properly, try the `!help` command or notify an admin!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}! You don't have permission to use this command.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{ctx.message.author.mention}! This command doesn't exist. Use `!help` command to list every commands.")
        else:
            await ctx.send(f"{ctx.message.author.mention}! Something went wrong. Use `!help` command to list every commands.")
    
    # Commands ------------------------------
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ping(self, ctx):
        await ctx.send(f"⏲️ {round(self.bot.latency, 2)}ms")
        
    @commands.command(aliases = ["del", "delete", "clean"])
    async def clear(self, ctx, amount = 1):
        amount = amount + 1
        await ctx.channel.purge(limit = amount)
        self.C.Warning(f"@{ctx.message.author} just deleted {amount - 1} message(s) in the #{ctx.channel.name} channel!")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def reboot(self, ctx):
        self.C.Information(f"The bot will be rebooted by @{ctx.author}.")
        os.execv(sys.executable, ['python'] + sys.argv)
            
# Connect to the bot  
def setup(bot):
    bot.add_cog(Cog(bot))

# Test cogs locally
if __name__ == "__main__":
    C = Console("")
    
    C.Message("Message example")
    C.Success("Success example")
    C.Information("Information example")
    C.Warning("Warning example")
    C.Error("Error example")
   