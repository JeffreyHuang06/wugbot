import discord
from discord.ext import commands

class Loader (commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def load(self, ctx, extension: str):
        self.bot.load_extension(f"cogs.{extension}")

        await ctx.send(f"Successfully loaded {extension}")

    @commands.command()
    async def unload(self, ctx, extension: str):
        self.bot.unload_extension(f"cogs.{extension}")

        await ctx.send(f"Successfully unloaded {extension}")

    @commands.command()
    async def reload(self, ctx, extension: str):
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")

        await ctx.send(f"Successfully reloaded {extension}")

def setup(bot):
    bot.add_cog(Loader(bot))