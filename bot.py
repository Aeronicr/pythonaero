import discord
from discord.ext import commands
from config import settings
import sys, traceback
import os

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['.', '= ', '?']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['fun', 'animals', 'info']
bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

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

