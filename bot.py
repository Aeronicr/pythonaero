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
    await channel.send("AeroBot долучився до серверу та готовий працювати!")

    channel = bot.get_channel(755473910115336192)
    Text= "Якщо ти пипаєш у борделі то став :slavetnyi_kreygasm:"
    Moji = await client.send_message(channel, Text)
    await client.add_reaction(Moji, emoji=':slavetnyi_kreygasm:')

@bot.event
@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel(755473910115336192)
    if reaction.message.channel.id != Channel
    return
    if reaction.emoji == "":
      Role = discord.utils.get(user.server.roles, name="Еротика")
      await client.add_roles(user, Role)

@bot.command(aliases=['префікс'])
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")

bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])



