from typing import List
import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand
import os
import random

from src.wugcache import WugCache
from src.activities import activities

WugCache.init()

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

def get_bot_key() -> str:
    return os.environ.get("DISCORD_KEY")

    with open("api.key", "r") as f:
        return f.read().rstrip("\n")

def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print ("Bot is ready")
    change_activity.start()

@tasks.loop(seconds=15)
async def change_activity():
    await bot.change_presence(activity=random.choice(activities))

if __name__ == "__main__":
    load_cogs()

    bot.run(get_bot_key())

#status is studying altaic