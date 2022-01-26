from pydoc import describe
import discord
from discord.ext import commands

class CustomEmbeds():
    async def InformationEmbed(ctx, Title = "Information",  text = None, mention = True, Color = 0x009de0):
        if mention:
            await ctx.send(ctx.message.author.mention, embed = discord.Embed(title = Title, description = text, color = Color))
        else:
            await ctx.send(embed = discord.Embed(title = Title, description = text, color = Color))
                
    async def DMEmbed(message, Title = "Rule violation",  text = "You used unallowed word(s). Do not do it again, or you will be kicked by me!", Color = 0xad0000):
        await message.author.send(embed = discord.Embed(title = Title, description = text, color = Color))

    async def WelcomeEmbed():
        pass

# Test CustomEmbeds locally
if __name__ == "__main__":
    pass 
