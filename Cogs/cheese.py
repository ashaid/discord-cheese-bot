import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from random import randint
import os
import src.gen as gen
import asyncio


class CheeseCog(commands.Cog, name="cheese command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.printing = False

    @commands.command(name="cheese",
                      usage="",
                      description="make's cheese")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def CHEESE(self, ctx):
        if self.printing:
            self.printing = False
            await ctx.send('Stopping Cheese Printer 🛑🧀🖨️')
        else:
            self.printing = True
            await ctx.send('Starting Cheese Printer 🟢🧀🖨️')
            await self.cheese_task(ctx)

    async def cheese_task(self, ctx):
        while self.printing:
            load_dotenv()
            cheese = gen.Generate_Cheese()
            embed = discord.Embed(title=cheese["name"] + " - " + cheese["type"],
                                  description=cheese["description"], color=randint(0, 0xffffff))
            embed.set_image(url=cheese["url"][0])
            embed.set_footer(text="bot made by tony")
            await ctx.send(embed=embed)
            await asyncio.sleep(3)


def setup(bot: commands.Bot):
    bot.add_cog(CheeseCog(bot))
