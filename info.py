import discord
from discord.ext import commands


class Info(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['who', 'user', 'користувач'])
    async def хто(self, ctx, *, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        embed = discord.Embed(color=0xff9900, title=':bust_in_silhouette: Інформаційна картка :bust_in_silhouette: ')
        embed.set_author(name=f"Інформація про учасника {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=":page_facing_up: Глобальний нік учасника: ", value=member.name)
        embed.add_field(name=":bookmark_tabs: Нік учасника на сервері: ", value=member.display_name)
        embed.add_field(name=":id: учасника: ", value=member.id)
        embed.add_field(name=":baby: Акаунт створено ", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"))
        embed.add_field(name=":baby_chick: Учасник приєднався до серверу ",
                        value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"))
        embed.add_field(name=f":newspaper2: Ролі учасника: ({len(roles)})",
                        value=" ".join([role.mention for role in roles]))
        embed.add_field(name=":card_index: Пріоритетна роль: ", value=member.top_role.mention)
        embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
        value = member.status
        if member.status == discord.Status.dnd:
            value = ":red_circle: не турбувати"
        elif member.status == discord.Status.online:
            value = ":green_circle: у мережі"
        elif member.status == discord.Status.idle:
            value = ":yellow_circle: відійшов"
        else:
            value = ":radio_button: не в мережі"
        embed.add_field(name=":mag: Статус користувача: ", value=value)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['who_info', 'user_info', 'користувач_інфо'])
    async def хто_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "хто" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить на екран користувача його інформаційну картку. Картка "
                              "містить інформацію про ID, нікнейми, статус, дати приєднання до серверу, ролі користувача "
                              "та інше",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>хто, <префікс>хто @нік_користувача", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="who, user, користувач", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command(pass_context=True, aliases=['server'])
    async def сервер(self, ctx):
        name = ctx.guild.name
        owner = ctx.guild.owner
        id = ctx.guild.id
        region = ctx.guild.region
        icon = ctx.guild.icon_url
        total_text_channels = len(ctx.guild.text_channels)
        total_voice_channels = len(ctx.guild.voice_channels)
        total_channels = total_text_channels  + total_voice_channels
        member_count = 0
        for member in ctx.guild.members:
            member_count += 1
        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        bot_count = member_count - true_member_count
        embed = discord.Embed(color=0xff9900, title='Інформація про сервер')
        embed.set_thumbnail(url=icon)
        embed.add_field(name=":bank: Назва серверу: ", value=name)
        embed.add_field(name=":detective: Власник серверу: ", value=owner)
        embed.add_field(name=":id: серверу: ", value=id)
        embed.add_field(name=":statue_of_liberty: Регіон серверу: ", value=region, inline=False)
        embed.add_field(name=":page_with_curl: Кількість усіх учасників серверу: ", value=member_count)
        embed.add_field(name=":page_facing_up: Кількість учасників: ", value=true_member_count)
        embed.add_field(name=":bookmark_tabs: Кількість ботів: ", value=bot_count)
        embed.add_field(name=":ticket: Кількість усіх каналів: ", value=total_channels)
        embed.add_field(name=":speaker: Голосових каналів: ", value=total_voice_channels)
        embed.add_field(name=":keyboard: Текстових каналів: ", value=total_text_channels)
        embed.set_footer(text=f"Викликано {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['commands', 'com', 'ком'])
    async def команди(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команди AeroBot v.0.1 alpha :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Наявні команди:",
                        value="команди, хто, лисичка, песик, котик, обійняти, погладити, оу",
                        inline=False)
        embed.add_field(name="Довідка по командах:", value="Для отримання детальних відомостей щодо команди "
                                                           "введіть **_**інфо після назви команди та префікса (=хто**_**інфо, наприклад)", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True)
    async def бот(self, ctx):
        embed = discord.Embed(color=0xff9900, title='Звіт про створення бота за 24.09.2020')
        embed.add_field(name="За сьогодні зроблено наступне:",
                        value="додано нові можливості для команди 'заглушити'. Зокрема, тепер можна заглушити користувача на певний проміжок часу з плином якого бот сам розблокує користувача.",
                        inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context = True , aliases=['commands_info', 'com_info', 'ком_інфо'])
    async def команди_інфо(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':satellite: Інформація про команду "команди" :satellite: ')
        embed.set_thumbnail(url="https://i.ibb.co/5cNn5cL/1.png")
        embed.add_field(name="Опис команди:",
                        value="Ця команда виводить на екран користувача перелік усіх доступних команд",
                        inline=False)
        embed.add_field(name="Синтаксис команди:", value="<префікс>команди", inline=False)
        embed.add_field(name="Альтернативний виклик команди:", value="commands, com, ком", inline=False)
        embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # @commands.Cog.listener()
    # async def on_member_join(member):
    #     embed = discord.Embed(color=0x63ff52, title=':confetti_ball: Новий користувач долучився до серверу :confetti_ball:')
    #     # embed.set_thumbnail(url=member.avatar_url)
    #     embed.add_field(name=f"Вітаю тебе, {member} на славетному сервері Славенія.", value="Сподіваюсь ти станеш частинкою даної спільноти. Перш ніж перейти до ближчого знайомства, пропоную тобі переглянути інформацію про даний сервер та правила у #славетний-закон та #славетні правила. Уважно прочитай усе, лише уважні отримають доступ до усіх каналів :)", inline=False)
    #     embed.set_footer(text=f"Приємного спілкування {member}", icon_url=member.avatar_url)
    #     await channel.send(755473910115336192, embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        for channel in member.guild.channels:
            if str(channel) == "test-bot":
                await channel.send(f"Welcome to the {member.guild.name} discord server, {member.mention}")


def setup(bot):
    bot.add_cog(Info(bot))