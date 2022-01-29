# Modules
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
        
        for guild in self.bot.guilds:
            for member in guild.members:
                add_user_data(member.id, 0)
        
    # Delete messages that contain unallowed words and warn the author about it's violation
    @commands.Cog.listener()
    async def on_message(self, message):
        if prof.contains_profanity(message.content):
            await message.author.send(embed = discord.Embed(title = "Rule violation", description = "You used unallowed word(s). Do not do it again, or you will be kicked by me!", color = 0xad0000))
            self.C.Message(f"@{message.author} used unallowed word(s). Warning message has been sent to the user.")
            if violation_happend(message.author.id):
                self.C.Message(f"@{message.author} broke the rules five times. The user was removed from the server.")
                delete_user_database(message.author.id)
                await message.author.send(embed = discord.Embed(title = "Kick information", description = "You broke the rules five times and I kicked you as I told you.", color = 0xad0000))
                await message.author.kick(reason = "You broke the rules five times.")                
            await message.delete()
    
    # Add custom role to the new user and mention it
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.C.Message(f"@{member} has joined the server.")  
        add_user_data(member.id, 0)              
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
        delete_user_database(member.id)
    
    # Error handling        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", color = 0x009de0))
            self.C.Message(f"{ctx.author} caused command error. (Command on cooldown)")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = "You don't have permission to use this command. Use `!help` command to list every commands.", color = 0x009de0))
            self.C.Message(f"{ctx.author} caused command error. (Missing permission)")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = "You didn't give every required arguments. Use `!help` command to list every commands.", color = 0x009de0))
            self.C.Message(f"{ctx.author} caused command error. (Missing required argument)")
        elif isinstance(error, commands.ConversionError):
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = f"Conversion error. ({str(error)})", color = 0x009de0))
            self.C.Message(f"{ctx.author} caused command error. (Conversation error: {str(error)})")
        else:
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Command error", description = "Something went wrong. Use `!help` command to list every commands.", color = 0x009de0))
            self.C.Message(f"{ctx.author} caused command error.")
        
    
# Connect cog to the bot  
def setup(bot):
    bot.add_cog(Events(bot))
