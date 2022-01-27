import os
import sys
import discord
import youtube_dl
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
    
    # Join command: the bot will join the specific voice channel
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice == None:
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Join error", description = "You have to be in a voice channel. Use `!help` command to list every commands.", color = 0x009de0))
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client != None:
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Join error", description = "I am already in a voice channel. Use `!help` command to list every commands.", color = 0x009de0))
            return
        await voice_channel.connect()
    
    # Disconnect command: the bot will leave the specific voice channel
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
    
    # Play command: the bot will play music
    @commands.command()
    async def play(self, ctx, music_url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {"before_options":"-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options":"-nv"}
        YDL_OPTIONS = {"format":"bestaudio"}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(music_url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    
    # Pause command: the bot will pause the music    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Music action", description = "The music is paused.", color = 0x009de0))
    
    # Resume command: the bot will resume the music   
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = "Music action", description = "The music is resumed.", color = 0x009de0))
        
    # Adminhelp command: a simple help command for the moderators and admins
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        embed = discord.embed(title = "Admin help", description = "", color = 0x009de0)
        embed.add_field(name="!clear", value = "This command will delete messages.", inline = True)
        embed.add_field(name="!reboot", value = "This command will restart the bot.", inline = True)
        embed.add_field(name="!ban", value = "This command will ban a specific user.", inline = True)
        embed.add_field(name="!unban", value = "This command will unban a specific user.", inline = True)
        await ctx.send(embed = None)
    
    # Clear command: delete messages from the channel (only authorized users can use)    
    @commands.command(aliases = ["del", "delete", "clean"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)
        self.C.Information(f"@{ctx.message.author} just deleted {amount} message(s) in the #{ctx.channel.name} channel!")

    # Ban command: Ban the user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, reason = None):
        await member.ban(reason=reason)
        self.C.Information(f"@{ctx.message.author} has banned @{member}.")
        
    # Ban command: Ban the user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        member_name, member_discriminator = member.split("#")
        for ban_entry in await ctx.guild.bans():
            if (ban_entry.name, ban_entry.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(ban_entry.user)
                self.C.Information(f"@{ctx.message.author} has unbanned @{ban_entry.name}#{ban_entry.discriminator}.")
                return
    
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
