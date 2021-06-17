import json
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.context import SlashContext
from src.wugcache import WugCache

WugCache.init()

class Dbg(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @cog_ext.cog_slash(name="dbg_list_collectives", description="Lists all the collective nouns")
    async def dbg_list_collectives(self, ctx: SlashContext):

        await ctx.send(str(json.dumps(WugCache.wc["before_plural"]["collective"])))
    
    @cog_ext.cog_slash(name="dbg_list_wug", description="Lists all the plurals of a wug")
    async def dbg_list_wug(self, ctx: SlashContext):
        await ctx.send(str(WugCache.wc["wug_plurals"]))

    @cog_ext.cog_slash(name="dbg_wug_add", description="writes the actual json file and adds a wug")
    async def dbg_wug_add(self, ctx: SlashContext, wugname: str):

        WugCache.wc["wug_plurals"].append(wugname)

        try:
            WugCache.dumptofile()
            await ctx.send(f"Successfully added {wugname}")

        except Exception as e:
            await ctx.send(f"Error adding wug {wugname}\n")
            await ctx.send(f"```\n{str(e)}\n```")
    
    @cog_ext.cog_slash(name="dbg_cltv_add", description="writes the actual json and adds a collective noun")
    async def dbg_cltv_add(self, ctx, cltvname: str):
        
        # check if already in there
        if cltvname in WugCache.wc["before_plural"]["collective"]:
            await ctx.send(f"{cltvname} already in list")
            return
        
        WugCache.wc["before_plural"]["collective"].append(cltvname)
        WugCache.wc["before_plural"]["collective"].sort()

        try:
            WugCache.dumptofile()
            await ctx.send(f"Successfully added {cltvname}")

        except Exception as e:
            await ctx.send(f"Error adding noun {cltvname}\n")
            await ctx.send(f"```\n{str(e)}\n```")
    
def setup(bot):
    bot.add_cog(Dbg(bot))