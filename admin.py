import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class Admin(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['бан'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban (self, ctx, *, member:discord.Member = None, reason = None):
        roles = [role for role in member.roles]
        await ctx.channel.send(member.top_role.mention)
        if member.top_role.mention == '@Славетний радник':
            await ctx.channel.send("Ok")
        # if ctx.author.id == 339372925301948427:
        #     # member == None or member == ctx.message.author
        #     await ctx.channel.send("Ви не можете заблокувати себе")
        #     return
        # if reason == None:
        #     reason = "причину блокування не вказано"
        # message = f"Вас заблоковано модератором на {ctx.guild.name} за {reason}"
        # await member.send(message)
        # await ctx.guild.ban(member, reason=reason)
        # await ctx.channel.send(f"{member} заблоковано!")

    @ban.error
    async def ban_error(self, error, ctx):
        if isinstance(error, CheckFailure):
            await ctx.channel.send("Ви не можете заблокувати інших модераторів")

def setup(bot):
    bot.add_cog(Admin(bot))