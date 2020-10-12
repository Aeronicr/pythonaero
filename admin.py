import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
import asyncio
import typing
from typing import Optional
from discord import Permissions


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['адмін', 'mod', 'модер'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def admin(self, ctx, status = None, role=None, color=None):
        await ctx.message.delete()
        if status == '+':
            self.name_role = role
            if get(ctx.guild.roles, name= role):
                await ctx.send("Роль вже існує на сервері")
            else:
                perms = discord.Permissions(send_messages=False, read_messages=True, read_message_history=True)
                await ctx.guild.create_role(name=self.name_role, permissions=perms, colour=discord.Colour(int('ffffff', 16)))
                embed = discord.Embed(color=0xfc5821, title=f'Створено роль {role}')
                embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
                await(await ctx.send(embed=embed)).delete(delay=50)
        else:
            delrole = role
            guild = ctx.guild
            for role in guild.roles:
                if role.name == delrole: 
                    await role.delete()
                    embed = discord.Embed(color=0xfc5821, title=f'Видалено роль {delrole}')
                    embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
                    await(await ctx.send(embed=embed)).delete(delay=50)

    @commands.command(pass_context = True , aliases=['бан', 'заблокувати'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban (self, ctx, member:discord.Member = None, reason = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        role = [role for role in member.roles][1:]
        role_owner1 = [r.name for r in ctx.guild.roles][-1:]
        role_owner2 = [role.name for role in member.roles][1:]
        role_mod1 = [r.name for r in ctx.guild.roles][-2:-1]
        role_mod2 = [role.name for role in member.roles][1:]
        if set(role_mod1).issubset(role_mod2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заблокувати модератора серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif set(role_owner1).issubset(role_owner2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заблокувати власника серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        else:
            if reason == None:
                reason = "<причину блокування не вказано>"
            message = f"Вас заблокували на сервері {ctx.guild.name} за {reason}"
            await member.send(message)
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} заблоковано за {reason}!", value="Сподіваємось це буде уроком для решти.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
            await ctx.guild.ban(member, reason=reason)

    @commands.command(pass_context = True , aliases=['кік', 'вигнати'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def kick (self, ctx, member:discord.Member = None, reason = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        role = [role for role in member.roles][1:]
        role_owner1 = [r.name for r in ctx.guild.roles][-1:]
        role_owner2 = [role.name for role in member.roles][1:]
        role_mod1 = [r.name for r in ctx.guild.roles][-2:-1]
        role_mod2 = [role.name for role in member.roles][1:]
        if set(role_mod1).issubset(role_mod2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете вигнати модератора серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif set(role_owner1).issubset(role_owner2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете вигнати власника серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        else:
            if reason == None:
                reason = "<причину блокування не вказано>"
            message = f"Вас вигнали із серверу {ctx.guild.name} за {reason}"
            await member.send(message)
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} виключено із серверу за {reason}!", value="Сподіваємось це буде уроком для решти.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
            await ctx.guild.kick(member, reason=reason)

    @commands.command(pass_context = True , aliases=['мют', 'заглушити'])
    @has_permissions(administrator=True, manage_messages=True)
    async def mute (self, ctx, member:discord.Member = None, time : int = None, reason=None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        role = [role for role in member.roles][1:]
        role_owner1 = [r.name for r in ctx.guild.roles][-1:]
        role_owner2 = [role.name for role in member.roles][1:]
        role_mod1 = [r.name for r in ctx.guild.roles][-2:-1]
        role_mod2 = [role.name for role in member.roles][1:]
        case = None
        if set(role_mod1).issubset(role_mod2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заглушити модератора серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif set(role_owner1).issubset(role_owner2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заглушити власника серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif [r for r in ctx.guild.roles if r.name == self.name_role][0] == member.top_role:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете заглушити користувача, який вже є заглушеним! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        else:
            await member.remove_roles(*role)
            role = discord.utils.get(member.guild.roles, name=self.name_role)
            await member.add_roles(role)
            if reason == None:
                reason = "<причину блокування не вказано>"
                case = ''
            if time == None:
                time = "на час до розблокування модераторами"
            elif time == 1 or time == 21 or time == 31 or time == 41:
                case = 'хвилину'
            elif time == 2 or time == 3 or time == 4 or time == 22 or time == 23 or time == 24 or time == 32 or time == 33 or time == 34 or time == 42 or time == 43 or time == 44:
                case = 'хвилини'
            elif time > 48:
                case = 'декілька днів'
                time = ''
            else:
                case = 'хвилин'
            embed = discord.Embed(color=0x730505, title=':no_entry: Застосовано покарання :no_entry:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} заглушено за {reason} на {time} {case}!", value="Уважно прочитайте правила серверу.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
            if time != 0 or time !=None:
                await asyncio.sleep(time*60)
                await member.remove_roles(role)
                embed = discord.Embed(color=0x63ff52, title=':white_check_mark: Знято покарання :white_check_mark:')
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name=f"Користувача {member} розглушено", value="Сподіваємось ви усвідомили свою помилку.", inline=False)
                embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
                await(await ctx.send(embed=embed)).delete(delay=50)

    @commands.command(pass_context = True , aliases=['анмют', 'розглушити'])
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def unmute (self, ctx, member:discord.Member = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        role = [role for role in member.roles][1:]
        role_owner1 = [r.name for r in ctx.guild.roles][-1:]
        role_owner2 = [role.name for role in member.roles][1:]
        role_mod1 = [r.name for r in ctx.guild.roles][-2:-1]
        role_mod2 = [role.name for role in member.roles][1:]
        role_used = [r for r in ctx.guild.roles if r.name == self.name_role][0]
        if set(role_mod1).issubset(role_mod2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете розглушити модератора серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif set(role_owner1).issubset(role_owner2):
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Ви не можете розглушити власника серверу! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        elif role_used.mention != member.top_role.mention:
            embed = discord.Embed(color=0xfc5821, title=f':bangbang: Користувач {member.name} не є заглушеним на даному сервері! :bangbang:')
            embed.set_footer(text=f"Системне повідомлення для {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)
        else:
            await member.remove_roles(*role)
            embed = discord.Embed(color=0x63ff52, title=':white_check_mark: Знято покарання :white_check_mark:')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f"Користувача {member} розглушено", value="Сподіваємось ви усвідомили свою помилку.", inline=False)
            embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
            await(await ctx.send(embed=embed)).delete(delay=50)

    @commands.command(pass_context=True, aliases=['del', 'очистити', 'чистити'])
    async def clear(self, ctx, amount):
        channel = ctx.message.channel
        messages = []
        amount = int(amount)
        async for message in channel.history(limit=amount):
                messages.append(message)

        await channel.delete_messages(messages)
        while amount in range (1,5) or amount in range (21,25) or amount in range (31,35) or amount in range (41,45) or amount in range (51,55) or amount in range (61,65) or amount in range (71,75) or amount in range (81,85) or amount in range (91,95):
            await(await ctx.send(f'{amount} повідомлення видалено.')).delete(delay=15)
            break
        while amount in range(5,21) or amount in range(25,31) or amount in range(35,41) or amount in range(45,51) or amount in range(55,61) or amount in range(65,71) or amount in range(75,81) or amount in range(85,91) or amount in range(95,101):
            await(await ctx.send(f'{amount} повідомлень видалено.')).delete(delay=15)
            break
        if amount > 100:
            await(await ctx.send(f'Повідомлень видалено: {amount}.')).delete(delay=15)
        


def setup(bot):
    bot.add_cog(Admin(bot))