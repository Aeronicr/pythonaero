import discord
from discord.ext import commands


class Admin(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['бан'])
    @commands.has_any_role("Батя","Славетний радник")
    async def ban (self, ctx, *, member:discord.Member=None, reason =None):
        if member == None or member == ctx.message.author or ctx.message.author.server_permissions.administrator:
            await ctx.channel.send("Ви не можете забанити себе або інших модераторів")
            return
        if reason == None:
            reason = "причину бану не вказано"
        message = f"Ви забанили користувача {ctx.guild.name} за {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} забанено!")

def setup(bot):
    bot.add_cog(Admin(bot))