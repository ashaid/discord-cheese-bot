import discord
from discord.ext import commands, tasks
import json
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# Get configuration.json
with open("configuration.json", "r") as config:
    load_dotenv()
    data = json.load(config)
    # keep_alive()
    token = os.environ['DISCORD_BOT_SECRET']
    prefix = data["prefix"]
    owner_id = data["owner_id"]


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents=intents, owner_id=owner_id)

# Load cogs
if __name__ == '__main__':
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))

bot.run(token)
