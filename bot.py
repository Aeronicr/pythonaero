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
async def on_ready(message):
    activity = discord.Game(name="Захоплення світу")
    channel = bot.get_channel(755473910115336192)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    embed = discord.Embed(color=0xfc5821, title=f':robot: AeroBot долучився до серверу та готовий працювати!:robot: ')
    await channel.send(embed=embed)

    Text= "YOUR_MESSAGE_HERE"
    Moji = await message.channel.send(channel, Text)
    await message.add_reaction(Moji, emoji=':slavetnyi_dypa:')

@bot.command(aliases=['префікс'])
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")

@bot.event
async def on_reaction_add(reaction, member):
    Channel = bot.get_channel('755473910115336192')
    if reaction.message.channel.id != Channel:
        return
    if reaction.emoji == ":slavetnyi_dypa:":
      role = get(member.guild.roles, name="Еротика")
      await member.add_roles(role)

bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])



