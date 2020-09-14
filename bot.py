import discord
from discord.ext import commands
from config import settings
import sys, traceback
import os


default_prefixes = ['.']
bot = commands.Bot(command_prefix=default_prefixes, description='A Rewrite Cog Example')
initial_extensions = ['fun', 'animals', 'info']
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

bot.remove_command("help")
bot.run(os.environ['DISCORD_TOKEN'])

# bot.run(settings['token'])

