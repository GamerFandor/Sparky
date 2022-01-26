import os
import discord
from discord.ext import commands
from better_profanity import profanity as prof
try: from libraries.console import Console
except: from console import Console

class Events(commands.Cog):
    # Reference to class Console
    C = None

    # Constructor
    def __init__(self, bot):
        self.bot = bot
        self.C = Console()  
        self.C.Success("All events are successfully loaded.")
    
    # Feedback when the bod is ready to work
    @commands.Cog.listener()
    async def on_ready(self):
        self.C.Success("All systems are fully operational.")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you 😈"))

    # Delete messages that contain unallowed words and warn the author about it's violation
    @commands.Cog.listener()
    async def on_message(self, message):
        if prof.contains_profanity(message.content):
            await message.channel.send(f"{message.author.mention} You used unallowed word(s). Do not do it again, or you will be kicked by me!")
            self.C.Message(f"@{message.author} used unallowed word(s). Warning message has been sent to the user.")
            await message.delete()
            # TODO: send DM message when someone does rule violation
            
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.message.author.mention} Please pass in all required arguments! If something doesn't work properly, try the `!help` command or notify an admin!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention} You don't have permission to use this command.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{ctx.message.author.mention} This command doesn't exist. Use `!help` command to list every commands.")
        else:
            await ctx.send(f"{ctx.message.author.mention} Something went wrong. Use `!help` command to list every commands.")
        self.C.Message(f"{ctx.author} caused command error.")

        
# Connect to the bot  
def setup(bot):
    bot.add_cog(Events(bot))

# Test commands locally
if __name__ == "__main__":
    pass
