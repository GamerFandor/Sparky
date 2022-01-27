# Moduls
import discord
from discord.ext import commands
from discord.utils import get
from better_profanity import profanity as prof
from libraries.queries import *
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
        if get_activity_type()== "playing":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=get_activity_text()))
        elif get_activity_type()== "watching":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=get_activity_text()))
        elif get_activity_type()== "listening":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=get_activity_text()))
        elif get_activity_type()== "streaming":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=get_activity_text()))
        
    # Delete messages that contain unallowed words and warn the author about it's violation
    @commands.Cog.listener()
    async def on_message(self, message):
        if prof.contains_profanity(message.content):
            await message.author.send(embed = discord.Embed(title = "Rule violation", description = "You used unallowed word(s). Do not do it again, or you will be kicked by me!", color = 0xad0000))
            self.C.Message(f"@{message.author} used unallowed word(s). Warning message has been sent to the user.")
            await message.delete()
    
    # Add custom role to the new user and mention it
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.C.Message(f"@{member} has joined the server.")                
        try:
            role = get(member.guild.roles, id=get_default_role())
            await member.add_roles(role)
        except: 
            self.C.Error(f"Failed to give a startup role to @{member}")        
        try:
            channel = self.bot.get_channel(get_welcome_channel())
            embed = discord.Embed(title = f"@{member.name}", description = "Have fun on the server!", color = 0xc2c200)
            embed.set_author(name = "Welcome")
            embed.set_thumbnail(url = member.avatar_url)
            await channel.send(embed = embed)
        except:
            self.C.Error(f"Failed to send a welcome message to @{member}")
    
    # When a member leave the server, it will send a message to the console  
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.C.Message(f"@{member} has left the server.") 
    
    # Error handling        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = "Something went wrong. Use `!help` command to list every commands.", color = 0x009de0))
        self.C.Message(f"{ctx.author} caused command error.")
    
# Connect to the bot  
def setup(bot):
    bot.add_cog(Events(bot))

# Test commands locally
if __name__ == "__main__":
    pass
