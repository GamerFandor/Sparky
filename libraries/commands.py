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
        self.C.Information(f"@{ctx.message.author} has unbanned @{member}.")
        
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
