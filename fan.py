import discord
from discord.ext import commands


class Fan(commands.Cog, name="Fan"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def послати(self, ctx,*, message):
        target_channel = bot.get_channel("412678093006831617")
        await ctx.send(channel, message)



def setup(bot):
    bot.add_cog(Info(bot))