import discord
from discord.ext import commands
import sys, traceback
import os
from discord.ext.commands import has_permissions
import youtube_dl
import ctypes
import ctypes.util

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
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command(aliases=['префікс'])
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Префікс бота успішно змінено!")

bot.remove_command("help")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def endSong(guild, path):
    os.remove(path)


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # link to your song on YouTube
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    file = ydl.extract_info(url, download=True)
    guild = "731885002165583912"  # id of your server which you can get by right clicking on server name and clicking "Copy ID" (developer mode must be on)
    path = str(file['title']) + "-" + str(file['id'] + ".mp3")

channel1 = client.get_channel(755738347644911673)  # id of your channel (you get it like server id, but by right clicking on channel)
voice_client = await channel1.connect()

voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

while voice_client.is_playing():  # waits until song ends
    await asyncio.sleep(1)
else:
    await voice_client.disconnect()  # and disconnects
    print("Disconnected")

bot.run(os.environ['DISCORD_TOKEN'])



