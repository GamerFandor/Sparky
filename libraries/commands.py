import os
import sys
import discord
from discord.ext import commands
from better_profanity import profanity as prof
try: from libraries.console import Console
except: from console import Console

class Commands(commands.Cog):
    # Reference to class Console
    C = None

    # Constructor
    def __init__(self, bot):
        self.bot = bot
        self.C = Console()
        self.C.Success("All commands are successfully loaded.")
    
    # Ping command: returns the latency of the bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.send(f"⏲️ {round(self.bot.latency, 2)}ms")
    
    # Who is command: returns a few information about a server member
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def whois(self, ctx, member:discord.Member):
        await ctx.send(f"this member is {member.mention}")
        self.C.Information(f"@{ctx.message.author} just asked information about @{member}")
    
    # Clear command: delete messages from the channel (only authorized users can use)    
    @commands.command(aliases = ["del", "delete", "clean"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)
        self.C.Information(f"@{ctx.message.author} just deleted {amount} message(s) in the #{ctx.channel.name} channel!")

    # Reboot command: restart the discord bot (only authorized users can use)
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def reboot(self, ctx):
        self.C.Information(f"The bot will be rebooted by @{ctx.author}.")
        os.execv(sys.executable, ['python'] + sys.argv)

    # Test command: test new features (developer tool - delete when you want to release the bot)
    @commands.command()
    async def test(self, ctx):
        await ctx.author.send("This is your dm?")   

# Connect to the bot  
def setup(bot):
    bot.add_cog(Commands(bot))

# Test commands locally
if __name__ == "__main__":
    pass
