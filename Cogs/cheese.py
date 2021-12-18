import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint
import os


class CheeseCog(commands.Cog, name="cheese command"):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        
    @commands.command(name = "cheese",
					usage="",
					description = "make's cheese")
                    
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def CHEESE(self, ctx):
        load_dotenv()
        embed = discord.Embed(title="American Cheese", description="Modern American cheese is a type of processed cheese developed in the 1910s made from cheddar, Colby, or similar cheeses", color=randint(0, 0xffffff))
        embed.set_image(url=os.getenv('PLACEHOLDER_CHEESE_IMAGE'))
        #embed.add_field(name="field", value="value", inline=False)
        embed.set_footer(text="bot made by tony")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(CheeseCog(bot))