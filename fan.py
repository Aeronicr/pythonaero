import discord
from discord.ext import commands


class Fan(commands.Cog, name="Fan"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def послати(self, member, ctx,*, message):
        for channel in member.guild.channels:
            if str(channel) == "славетна-флудильня":
                await channel.send(message)
                await ctx.message.delete()



def setup(bot):
    bot.add_cog(Fan(bot))