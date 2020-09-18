import discord
from discord.ext import commands
import json
import requests


class Animals(commands.Cog, name="Animals"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['fox', 'лис'])
    async def лисичка(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['fox_info', 'лис_інфо'])
    async def лисичка_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "лисичка" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить на екран користувача випадкову картинку із милою лисичкою",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>лисичка", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="лис, fox", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

        #------------------------------------------------------------------------------------------#

    @commands.command(pass_context = True , aliases=['dog', 'пес'])
    async def песик(self, ctx):
        response = requests.get('https://some-random-api.ml/img/dog')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['dog_info', 'пес_інфо'])
    async def песик_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "песик" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить на екран користувача випадкову картинку із милим песиком",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>песик", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="пес, dog", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

        #------------------------------------------------------------------------------#

    @commands.command(pass_context = True , aliases=['cat', 'кіт'])
    async def котик(self, ctx):
        response = requests.get('https://some-random-api.ml/img/cat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['cat_info', 'кіт_інфо'])
    async def котик_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "котик" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить на екран користувача випадкову картинку із милим котиком",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>котик", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="кіт, cat", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

        #------------------------------------------------------------------------------#




def setup(bot):
    bot.add_cog(Animals(bot))