import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from random import randint
from datetime import datetime, date, timedelta
import src.gen as gen
import asyncio


class CheeseCog(commands.Cog, name="cheese command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.printing = False
        self.timeLeftNum = None
        self.timeNow = None
        self.timeEnd = None

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
            await ctx.send('🧀🧀🧀🧀 CHEESE OF THE DAY 🧀🧀🧀🧀')
            cheese = gen.Generate_Cheese()
            embed = discord.Embed(title=cheese["name"] + " - " + cheese["type"],
                                  description=cheese["description"], color=randint(0, 0xffffff))
            embed.set_image(url=cheese["url"][0])
            embed.set_footer(
                text="bot made by tony")
            self.timeNow = datetime.now()
            self.timeEnd = self.timeNow + timedelta(hours=24)
            await ctx.send(embed=embed)
            await asyncio.sleep(86400)

    @commands.command(name="left",
                      aliases=["tl"],
                      usage="",
                      description="get how much time left until cheese of the day")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def timeLeft(self, ctx: commands.Context):
        self.timeNow = datetime.now()
        print(self.timeNow)
        print(self.timeEnd)
        self.timeLeftNum = str(self.timeEnd - self.timeNow)

        await ctx.send("🧀⏰: " + ':'.join(str(self.timeLeftNum).split('.')[:-1]))


def setup(bot: commands.Bot):
    bot.add_cog(CheeseCog(bot))
