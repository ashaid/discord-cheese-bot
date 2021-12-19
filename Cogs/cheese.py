import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint
import os
import src.gen as gen


class CheeseCog(commands.Cog, name="cheese command"):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        
    @commands.command(name = "cheese",
					usage="",
					description = "make's cheese")
                    
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def CHEESE(self, ctx):
        load_dotenv()
        cheese = gen.Generate_Cheese()
        embed = discord.Embed(title=cheese["name"], description=cheese["description"], color=randint(0, 0xffffff))
        print(cheese["url"])
        embed.set_image(url=cheese["url"][0])
        #embed.add_field(name="field", value="value", inline=False)
        embed.set_footer(text="bot made by tony")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(CheeseCog(bot))