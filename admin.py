import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get


class Admin(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['бан'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban (self, ctx, member:discord.Member = None, reason = None):
        modRole = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole2 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        if modRole.mention == member.top_role.mention or modRole2.mention == member.top_role.mention:
            await ctx.channel.send("Ви не можете заблокувати себе та інших модераторів")
        else:
            if reason == None:
                reason = "порушення правил серверу"
            message = f"Вас заблоковано модератором на {ctx.guild.name} за {reason}"
            await member.send(message)
            await ctx.guild.ban(member, reason=reason)
            await ctx.channel.send(f"Користувача {member} заблоковано!")

    @commands.command(pass_context = True , aliases=['кік', 'вигнати'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def kick (self, ctx, member:discord.Member = None, reason = None):
        modRole3 = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole4 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        if modRole3.mention == member.top_role.mention or modRole4.mention == member.top_role.mention:
            await ctx.channel.send("Ви не можете вигнати себе та інших модераторів")
        else:
            if reason == None:
                reason = "порушення правил серверу"
            message = f"Вас вигнали із серверу {ctx.guild.name} за {reason}"
            await member.send(message)
            await ctx.guild.ban(member, reason=reason)
            await ctx.channel.send(f"Користувача {member} виключено із серверу!")

    @commands.command(pass_context = True , aliases=['мют', 'заглушити'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def mute (self, ctx, member:discord.Member = None):
        modRole5 = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole6 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        if modRole5.mention == member.top_role.mention or modRole6.mention == member.top_role.mention:
            await ctx.channel.send("Ви не можете заглушити себе та інших модераторів")
        else:
            await member.add_roles(discord.utils.get(member.guild.roles, name='Троляка'))
            await ctx.channel.send(f"Користувача {member} заглушено!")

    @commands.command(pass_context=True, aliases=['del', 'очистити'])
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        messages = []
        amount = int(amount)
        async for message in channel.history(limit=amount):
                messages.append(message)

        await channel.delete_messages(messages)
        await ctx.send('Повідомлення видалено.')


def setup(bot):
    bot.add_cog(Admin(bot))