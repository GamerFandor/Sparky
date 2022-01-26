import os
import discord
from discord.ext import commands
from better_profanity import profanity as prof
try: from libraries.embeds import CustomEmbeds
except: from embeds import CustomEmbeds
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
            await CustomEmbeds.DMEmbed(message)
            self.C.Message(f"@{message.author} used unallowed word(s). Warning message has been sent to the user.")
            await message.delete()
    
    # Add custom role to the new user and mention it
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.C.Message(f"@{member} has joined the server.")   
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.C.Message(f"@{member} has left the server.") 
    
    # Error handling        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await CustomEmbeds.InformationEmbed(ctx, "Command error", "Something went wrong. Use `!help` command to list every commands.")
        self.C.Message(f"{ctx.author} caused command error.")

        
# Connect to the bot  
def setup(bot):
    bot.add_cog(Events(bot))

# Test commands locally
if __name__ == "__main__":
    pass
