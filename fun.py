import discord
from discord.ext import commands
import json
import requests


class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['hug_info'])
    async def обійняти_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "обійняти" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить анімоване анімешне зображення обіймів. За допомогою "
                              "цієї команди користувачі можуть віртуально обійняти один одного",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>обійняти @нік_користувача", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="hug", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['hug'])
    async def обійняти(self, ctx, *, member: discord.Member = None):
        response = requests.get('https://some-random-api.ml/animu/hug')
        json_data = json.loads(response.text)

        author = ctx.message.author
        await ctx.send(f'{author.mention} обіймає {member.mention}')

        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #--------------------------------------------------------------------#

    @commands.command(pass_context=True, aliases=['put_info', 'гладити_інфо'])
    async def погладити_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "погладити" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить анімоване анімешне зображення погладжування по голові. За допомогою "
                              "цієї команди користувачі можуть віртуально підтримати один одного",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>погладити @нік_користувача", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="put, гладити", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['put', 'гладити'])
    async def погладити(self, ctx, *, member: discord.Member = None):
        response = requests.get('https://some-random-api.ml/animu/pat')
        json_data = json.loads(response.text)

        author = ctx.message.author
        await ctx.send(f'{author.mention} гладить по голові {member.mention}')

        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(bot):
    bot.add_cog(Fun(bot))