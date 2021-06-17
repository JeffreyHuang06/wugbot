from typing import List
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import random
import json
import os
from src.decorators import wccmd

from src.wugcache import WugCache

WugCache.init()

def get_bot_key() -> str:
    # return os.environ.get("DISCORD_KEY")

    with open("api.key", "r") as f:
        return f.read().rstrip("\n")

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print ("Bot is ready")

# TODO: add cogs
@bot.command()
async def load(ctx, extension: str):
    bot.load_extension(f"cogs.{extension}")

    await ctx.send(f"Successfully loaded {extension}")

@bot.command()
async def unload(ctx, extension: str):
    bot.unload_extension(f"cogs.{extension}")

    await ctx.send(f"Successfully unloaded {extension}")

@bot.command()
async def reload(ctx, extension: str):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")

    await ctx.send(f"Successfully reloaded {extension}")

@slash.slash(name="listwug", description="Lists all the plurals of a wug")
async def listwug(ctx: SlashContext):
    await ctx.send(str(WugCache.wc["wug_plurals"]))

@wccmd
@slash.slash(name="twowug", description="Here is a wag, ")
async def twowug(ctx: SlashContext):
    wc = WugCache.wc

    await ctx.send(f"{wc['before_plural']['default']} {random.choice(wc['wug_plurals'])}{random.choice(wc['after_plural'])}")

@wccmd
@slash.slash(name="wug", description="Here is a wug, ")
async def wug(ctx: SlashContext):
    wc = WugCache.wc

    random_collective = random.choice(wc["before_plural"]["collective"])
    indef_art = "an" if random_collective[0] in list("aeiou") else "a"

    await ctx.send(f"Now there is {indef_art} {random_collective} of {random.choice(wc['wug_plurals'])}{random.choice(wc['after_plural'])}")

if __name__ == "__main__":
    load_cogs()

    bot.run(get_bot_key())