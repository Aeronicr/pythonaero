import discord
from discord.ext import commands
from discord.utils import get



class Fan(commands.Cog, name="Fan"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # async def послати(self, member,*, message):
    async def послати(self, member, *, message):
        for channel in member.guild.channels:
            if str(channel) == "славетна-флудильня":
                await channel.send(message)
                




def setup(bot):
    bot.add_cog(Fan(bot))