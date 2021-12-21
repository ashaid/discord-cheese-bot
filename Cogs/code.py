import discord
from discord.ext import commands


class Code(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="code",
                      usage="",
                      description="get code and developer")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def code(self, ctx: commands.Context):
        await ctx.send("bot made by tony. view the source code at https://github.com/ashaid/discord-cheese-bot")


def setup(bot: commands.Bot):
    bot.add_cog(Code(bot))
