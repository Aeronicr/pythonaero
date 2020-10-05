import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
import asyncio
import typing
from typing import Optional


class Admin(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['бан', 'заблокувати'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban (self, ctx, member:discord.Member = None, reason = None):
        modRole = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole2 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        if modRole.mention == member.top_role.mention or modRole2.mention == member.top_role.mention:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заблокувати себе та інших модераторів, а також користувачів, що вже є заблокованими! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if reason == None:
                reason = "<причину блокування не вказано>"
            message = f"Вас заблоковано модератором на {ctx.guild.name} за {reason}"
            await member.send(message)
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} заблоковано за {reason}!", value="Сподіваємось це буде уроком для решти.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.guild.ban(member, reason=reason)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['кік', 'вигнати'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def kick (self, ctx, member:discord.Member = None, reason = None):
        modRole3 = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole4 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        if modRole3.mention == member.top_role.mention or modRole4.mention == member.top_role.mention:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете вигнати себе та інших модераторів, а також користувачів, що не є учасниками серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if reason == None:
                reason = "<причину блокування не вказано>"
            message = f"Вас вигнали із серверу {ctx.guild.name} за {reason}"
            await member.send(message)
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} виключено із серверу за {reason}!", value="Сподіваємось це буде уроком для решти.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.guild.kick(member, reason=reason)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['мют', 'заглушити'])
    @has_permissions(administrator=True, manage_messages=True)
    async def mute (self, ctx, time: typing.Optional[int], member:discord.Member = None, reason=None):
        modRole5 = [r for r in ctx.guild.roles if r.name == "Славетний радник"][0]
        modRole6 = [r for r in ctx.guild.roles if r.name == "Батя"][0]
        modRole7 = [r for r in ctx.guild.roles if r.name == "Троляка"][0]
        if modRole5.mention == member.top_role.mention or modRole6.mention == member.top_role.mention or modRole7.mention == member.top_role.mention:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заглушити себе та інших модераторів, а також користувачів, що вже є заглушеними! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            role = discord.utils.get(member.guild.roles, name='Троляка')
            await member.add_roles(role)
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            if reason == None:
                reason = "<причину блокування не вказано>"
            if time == None:
                time = "<час блокування не вказано>"
            embed.add_field(name=f"Користувача {member} заглушено за {reason} на {time} хвилин(у)!", value="Уважно прочитайте правила серверу.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await asyncio.sleep(time*60)
            await member.remove_roles(role)
            embed = discord.Embed(color=0x63ff52, title=':white_check_mark: Знято покарання :white_check_mark:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} розглушено", value="Сподіваємось ви усвідомили свою помилку.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True)
    async def one (self, ctx, member:discord.Member = None, reason=None):
        role_names = (str(r.name) for r in ctx.guild.roles)
        roles = tuple(get(ctx.guild.roles, name=n) for n in role_names)
        await ctx.send(role_names)
        await ctx.send(roles)
        await member.remove_roles(*roles)
        await ctx.send(f'Removed **all** experimental roles.')

    @commands.command(pass_context = True , aliases=['анмют', 'розглушити'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def unmute (self, ctx, member:discord.Member = None):
        modRole5 = [r for r in ctx.guild.roles if r.name == "Троляка"][0]
        member = ctx.author if not member else member
        if modRole5.mention == member.top_role.mention:
            await member.remove_roles(discord.utils.get(member.guild.roles, name='Троляка'))
            embed = discord.Embed(color=0x63ff52, title=':white_check_mark: Знято покарання :white_check_mark:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} розглушено", value="Сподіваємось ви усвідомили свою помилку.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Користувач {member.name} не є заглушеним на даному сервері! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['del', 'очистити', 'чистити'])
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        messages = []
        amount = int(amount)
        async for message in channel.history(limit=amount):
                messages.append(message)

        await channel.delete_messages(messages)
        while amount in range (1,5) or amount in range (21,25) or amount in range (31,35) or amount in range (41,45) or amount in range (51,55) or amount in range (61,65) or amount in range (71,75) or amount in range (81,85) or amount in range (91,95):
            await(await ctx.send(f'{amount} повідомлення видалено.')).delete(delay=5)
            break
        while amount in range(5,21) or amount in range(25,31) or amount in range(35,41) or amount in range(45,51) or amount in range(55,61) or amount in range(65,71) or amount in range(75,81) or amount in range(85,91) or amount in range(95,101):
            await(await ctx.send(f'{amount} повідомлень видалено.')).delete(delay=5)
            break
        if amount > 100:
            await(await ctx.send(f'Повідомлень видалено: {amount}.')).delete(delay=5)
        


def setup(bot):
    bot.add_cog(Admin(bot))