import discord
from discord import channel
from discord.client import Client
from discord.ext import commands
import json


class Code(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.newKey = False

    @commands.command(name="code",
                      usage="",
                      description="get code and developer")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def code(self, ctx: commands.Context):
        await ctx.send("bot made by tony. view the source code at https://github.com/ashaid/discord-cheese-bot")

    @commands.command(name="reload", description="reloads a module")
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f"cogs.{extension}")
        embed = discord.Embed(
            title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
        await ctx.send(embed=embed)

    @ commands.is_owner()
    @ commands.command(name="broadcast", description="broadcast to channels", pass_context=True, hidden=True)
    async def broadcast(self, ctx, *, msg):
        with open("src/data/servers.json", "r") as outfile:
            file_data = json.load(outfile)

        for each in file_data:
            try:
                channel = self.bot.get_channel(int(each['channel']))
                await channel.send(msg)
            except Exception:
                continue


def setup(bot: commands.Bot):
    bot.add_cog(Code(bot))
