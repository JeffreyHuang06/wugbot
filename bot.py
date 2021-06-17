from typing import List
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os

from src.wugcache import WugCache

WugCache.init()

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

def get_bot_key() -> str:
    # return os.environ.get("DISCORD_KEY")

    with open("api.key", "r") as f:
        return f.read().rstrip("\n")

def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print ("Bot is ready")

if __name__ == "__main__":
    load_cogs()

    bot.run(get_bot_key())