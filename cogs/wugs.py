import random
import discord
from discord.ext import commands
from discord_slash import cog_ext
from src.decorators import wccmd
from src.wugcache import WugCache

class Wugs (commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
    
    @wccmd
    @cog_ext.cog_slash(name="twowug", description="Here is a wag, ")
    async def twowug(self, ctx):
        wc = WugCache.wc

        await ctx.send(f"{wc['before_plural']['default']} {random.choice(wc['wug_plurals'])}{random.choice(wc['after_plural'])}")

    @wccmd
    @cog_ext.cog_slash(name="wug", description="Here is a wug, ")
    async def wug(self, ctx):
        wc = WugCache.wc

        random_collective = random.choice(wc["before_plural"]["collective"])
        indef_art = "an" if random_collective[0] in list("aeiou") else "a"

        await ctx.send(f"Now there is {indef_art} {random_collective} of {random.choice(wc['wug_plurals'])}{random.choice(wc['after_plural'])}")

def setup(bot):
    bot.add_cog(Wugs(bot))
