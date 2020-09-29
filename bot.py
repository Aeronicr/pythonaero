import discord
from discord.ext import commands
import sys, traceback
import os
from discord.ext.commands import has_permissions
from discord.utils import get

custom_prefixes = {}
default_prefixes = ['.']
async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes
initial_extensions = ['fun', 'animals', 'info', 'admin']
bot = commands.Bot(command_prefix = determine_prefix, description='A Rewrite Cog Example')
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Помилка завантаження додатків {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    activity = discord.Game(name="Захоплення світу")
    channel = bot.get_channel(755473910115336192)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    embed = discord.Embed(color=0xfc5821, title=f':robot: AeroBot долучився до серверу та готовий працювати!:robot: ')
    await channel.send(embed=embed)


@bot.command(aliases=['префікс'])
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")

# @bot.command(pass_context=True)
# async def test(ctx, message):
#     if ctx.message.author.server_permissions.administrator:
#         testEmbed = discord.Embed(color = discord.Color.red())
#         testEmbed.set_author(name='Test')
#         testEmbed.add_field(name='Test', value='Test')

#     msg = await ctx.send(embed=testEmbed)
#     await message.add_reaction(msg, emoji=':slavetnyi_dypa:')

# @bot.event
# async def on_reaction_add(reaction, member):
#     if reaction.message.channel.id != '755473910115336192':
#         return
#     if reaction.emoji == ":slavetnyi_dypa:":
#         Role = discord.utils.get(member.server.roles, name="Еротика")
#         await member.add_roles(member, Role)



@bot.command(pass_context=True)
async def test(ctx):
    embed = discord.Embed(color=0x09c7ed, title=':bangbang: Оримання ролей та доступу до каналів :bangbang:')
    embed.add_field(name="Отримання початкової ролі на сервері:", value="Щоб отримати роль 'Новоприбулий' та перейти до основних каналів натисніть на реакцію :slavetnyi_heyguys:")
    embed.add_field(name="Отримання політичної ролі на сервері:", value="Щоб отримати роль 'Політика' та перейти до каналу із політичними обговореннями натисніть на реакцію :slavetnyi_monkas:")
    embed.add_field(name="Отримання еротичної ролі на сервері:", value="Щоб отримати роль 'Еротика' та перейти до каналу із контентом для дорослих натисніть на реакцію :slavetnyi_dypa: **Увага! Якщо вам немає 18+ років, не натискайте реакцію та перегляньте правила знову.**")
    embed.add_field(name="Отримання ґеймерської ролі на сервері:", value="Щоб отримати роль 'Ґеймер' та перейти до каналу із обговоренням ігор натисніть на реакцію :slavetnyi_wha:")
    msg = await ctx.send(embed=embed)
    emoji = discord.utils.get(bot.emojis, name='slavetnyi_dypa')
    emoji2 = discord.utils.get(bot.emojis, name='slavetnyi_monkas')
    emoji3 = discord.utils.get(bot.emojis, name='slavetnyi_wha')
    emoji4 = discord.utils.get(bot.emojis, name='slavetnyi_heyguys')
    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji2)
    await msg.add_reaction(emoji3)
    await msg.add_reaction(emoji4)

@bot.event
async def on_reaction_add(reaction, member):
    if reaction.message.channel.id != '755473910115336192':
        return
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_heyguys'):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Новоприбулий'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_monkas'):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Політика'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_dypa'):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Еротика'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_wha'):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Геймер'))

@bot.event
async def on_reaction_remove(reaction, member):
    if reaction.message.channel.id != '755473910115336192':
        return
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_dypa'):
        await member.remove_roles(discord.utils.get(member.guild.roles, name='Еротика'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_monkas'):
        await member.remove_roles(discord.utils.get(member.guild.roles, name='Політика'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_wha'):
        await member.remove_roles(discord.utils.get(member.guild.roles, name='Геймер'))
    if reaction.emoji == discord.utils.get(bot.emojis, name='slavetnyi_heyguys'):
        await member.remove_roles(discord.utils.get(member.guild.roles, name='Новоприбулий'))


bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])



