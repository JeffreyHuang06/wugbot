from typing import Dict, List
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
import random
import json
import os

from wugcache import WugCache

WugCache.init()

def get_bot_key() -> str:
    return os.environ.get("DISCORD_KEY")

def construct_random_plural_phrase() -> str:
    wc = WugCache.wc

    return random.choice(wc["before_plural"]) + random.choice(wc["wug_plurals"]) + random.choice(wc["after_plural"])

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

# @bot.event
# async def on_ready():
#     print ("Bot is ready")

@slash.slash(name="listwug", description="Lists all the plurals of a wug")
async def listwug(ctx: SlashContext):
    await ctx.send(str(WugCache.wc["wug_plurals"]))

@slash.slash(name="wug", description="Here is a wug, ")
async def wug(ctx: SlashContext):
    await ctx.send(construct_random_plural_phrase())

@slash.slash(name="dbg_wug_add", description="writes the actual json file adn adds a wug")
async def dbg_wug_add(ctx: SlashContext, wugname: str):

    WugCache.wc["wug_plurals"].append(wugname)

    with open("wugplurals.json", 'w') as f:
        try:
            f.write(json.dumps(WugCache.wc))
            await ctx.send(f"Successfully added {wugname}")

        except Exception as e:
            await ctx.send(f"Error adding wug {wugname}\n")
            await ctx.send(f"```\n{str(e)}\n```")

if __name__ == "__main__":
    bot.run(get_bot_key())