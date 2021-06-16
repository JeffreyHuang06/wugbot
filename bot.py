from typing import List
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import random
import json
import os

from wugcache import WugCache

WugCache.init()

def get_bot_key() -> str:
    return os.environ.get("DISCORD_KEY")

def space(lis: List[str]):
    accum: str = ""
    
    for i in lis: accum += i + ' '
    
    accum = accum[:-1]

    return accum

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print ("Bot is ready")

# TODO: add cogs

@slash.slash(name="listwug", description="Lists all the plurals of a wug")
async def listwug(ctx: SlashContext):
    print(WugCache.wc["wug_plurals"])
    await ctx.send(str(WugCache.wc["wug_plurals"]))

@slash.slash(name="twowug", description="Here is a wag, ")
async def twowug(ctx: SlashContext):
    wc = WugCache.wc

    await ctx.send(space([
        wc["before_plural"]["default"],

        random.choice(wc["wug_plurals"])

    ]) +
        random.choice(wc["after_plural"])
    )

@slash.slash(name="wug", description="Here is a wug, ")
async def wug(ctx: SlashContext):
    wc = WugCache.wc

    random_collective = random.choice(wc["before_plural"]["collective"])

    await ctx.send(space([
        # before phrase, between default or randomly selected collective noun
        space([
            "Now there is",
            "an" if random_collective[0] in list("aeiou") else "a",
            random_collective,
            "of"
        ]),

        # picks a random plural
        random.choice(wc["wug_plurals"])

    ]) +
        # picks a random after-phrase
        # TODO: afterplural eithermore options and random bool check or make it constant
        random.choice(wc["after_plural"])
    )

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