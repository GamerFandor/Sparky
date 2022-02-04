# Modules
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
    
    # Help command: print every command on the discord chat room
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help", description = "There is every command that you can use. (This bot is made for administration. So these commands are made for the admins.)", color = 0x009de0)
        embed.add_field(name = "!clear [amount]", value = "This command will delete messages.", inline = True)
        embed.add_field(name = "!ban [member] [reason]", value = "This command will ban a member.", inline = True)
        embed.add_field(name = "!unban [member]", value = "This command will deletet the member from the banned members.", inline = True)
        embed.add_field(name = "!reboot", value = "This command will restart the bot.", inline = True)
        embed.set_footer(text = "If you need help, you are able to talk an admin or the server owner.")
        await ctx.send(ctx.message.author.mention, embed = embed)
    
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
            
            if (ban_entry.user.name, ban_entry.user.discriminator) == (member_name, member_discriminator):
                
                await ctx.guild.unban(ban_entry.user)
                self.C.Information(f"@{ctx.message.author} has unbanned @{ban_entry.user.name}#{ban_entry.user.discriminator}.")
                return
    
    # Reboot command: restart the discord bot (only authorized users can use)
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def reboot(self, ctx):
        self.C.Information(f"The bot will be rebooted by @{ctx.author}.")
        os.execv(sys.executable, ['python'] + sys.argv)

# Connect cog to the bot  
def setup(bot):
    bot.add_cog(Commands(bot))
