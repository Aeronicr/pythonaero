import discord
from discord.ext import commands
import sys, traceback
import os
from discord.ext.commands import has_permissions

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
    # await channel.send("AeroBot долучився до серверу та готовий працювати!")

@bot.event
async def on_member_join(member):
     embed = discord.Embed(color=0x63ff52, title=':confetti_ball: Новий користувач долучився до серверу :confetti_ball:')
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name=f"Вітаю тебе, {member} на славетному сервері Славенія.", value="Сподіваюсь ти станеш частинкою даної спільноти. Перш ніж перейти до ближчого знайомства, пропоную тобі переглянути інформацію про даний сервер та правила у #славетний-закон та #славетні правила. Уважно прочитай усе, лише уважні отримають доступ до усіх каналів :)", inline=False)
    embed.set_footer(text=f"Приємного спілкування {member}", icon_url=member.avatar_url)
    await ctx.send(755473910115336192, embed=embed)

@bot.event
async def on_member_remove(member):
    await member.send('Remove')

@bot.command(aliases=['префікс'])
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")




bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])



