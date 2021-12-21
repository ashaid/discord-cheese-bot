import discord
from discord import file
from discord.ext import commands, tasks
from dotenv import load_dotenv
from random import randint
from datetime import datetime, date, timedelta
import src.gen as gen
import asyncio
import json


class CheeseCog(commands.Cog, name="cheese command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.timeLeftNum = None
        self.newKey = False
        self.timeNow = None
        self.timeEnd = None
        self.printing = True

    @commands.command(name="cheese",
                      usage="",
                      description="make's cheese")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def CHEESE(self, ctx):
        channel_name = str({ctx.channel.id}).strip("{}")
        server_name = str({ctx.guild.name}).strip("{}").replace("\"", "")
        ch_dictionary = {
            "server": server_name,
            "channel": channel_name
        }

        with open("src/data/servers.json", "r") as outfile:
            file_data = json.load(outfile)

        for each in file_data:
            if ch_dictionary == each:
                self.newKey = False
                each.pop("channel", None)
                each.pop("server", None)
                await ctx.send(
                    f"removing channel `{ctx.channel}` from cheese printing 🧀")
                break
            else:
                self.newKey = True

        if self.newKey:
            file_data.append(ch_dictionary)
            await ctx.send(f"channel `{ctx.channel}` from `{ctx.guild}` will now print daily cheese 🧀")

        file_data = self.remove_empty_elements(file_data)
        with open("src/data/servers.json", "w") as outfile:
            json.dump(file_data, outfile, indent=4)

        # channel = self.bot.get_channel(922712336245096469)
        # await channel.send('hey')

    def remove_empty_elements(self, d):
        """recursively remove empty lists, empty dicts, or None elements from a dictionary"""

        def empty(x):
            return x is None or x == {} or x == []

        if not isinstance(d, (dict, list)):
            return d
        elif isinstance(d, list):
            return [v for v in (self.remove_empty_elements(v) for v in d) if not empty(v)]
        else:
            return {k: v for k, v in ((k, self.remove_empty_elements(v)) for k, v in d.items()) if not empty(v)}

    async def broadcast(self, embed):
        with open("src/data/servers.json", "r") as outfile:
            file_data = json.load(outfile)

        for each in file_data:
            try:
                channel = self.bot.get_channel(int(each['channel']))
                await channel.send('🧀🧀🧀🧀 CHEESE OF THE DAY 🧀🧀🧀🧀')
                self.timeNow = datetime.now()
                self.timeEnd = self.timeNow + timedelta(hours=24)
                await channel.send(embed=embed)
            except Exception:
                continue

    async def cheese_task(self, embed):
        while self.printing:
            await self.broadcast(embed)
            await asyncio.sleep(86400)

    @commands.command(name="start", description="starts cheese")
    @commands.is_owner()
    async def start_cheese(self, ctx):
        cheese = gen.Generate_Cheese()
        embed = discord.Embed(title=cheese["name"] + " - " + cheese["type"],
                              description=cheese["description"], color=randint(0, 0xffffff))
        embed.set_image(url=cheese["url"][0])
        embed.set_footer(text="bot made by tony")
        await ctx.send('sending cheese')
        await self.cheese_task(embed)

    @commands.command(name="left",
                      aliases=["tl"],
                      usage="",
                      description="get how much time left until cheese of the day")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def timeLeft(self, ctx: commands.Context):
        self.timeNow = datetime.now()
        self.timeLeftNum = str(self.timeEnd - self.timeNow)

        await ctx.send("🧀⏰: " + ':'.join(str(self.timeLeftNum).split('.')[:-1]))


def setup(bot: commands.Bot):
    bot.add_cog(CheeseCog(bot))
