import discord
from discord.ext import commands
import sys, traceback
import os

custom_prefixes = {}
default_prefixes = ['.']
async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes
initial_extensions = ['fun', 'animals', 'info']
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
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command()
@commands.has_any_role("Батя","Славетний радник")
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")

bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])



