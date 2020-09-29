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
        embed = discord.Embed(color=0xff9900, title='Звіт про створення бота за 25.09.2020')
        embed.add_field(name="За сьогодні зроблено наступне:",
                        value="перепрацьовано візуальне оормоення команд 'вигнати' та 'заблокувати'. Бот відтепер інформуватиме про приєднання та вихід користувачів на сервері.",
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

    @commands.command(pass_context = True , aliases=['rules'])
    async def правила(self, ctx):
        embed = discord.Embed(color=0xff9900, title=':clipboard: Правила серверу :clipboard:')
        embed.set_thumbnail(url="https://i.ibb.co/4spmQyj/MTS-Info-icon-svg.png")
        embed.add_field(name="Загальні положення:",
                        value="Ласкаво просимо до серверу Славетного Славенія. Перш ніж ви поринете у спілкування, пропонуємо вам ознайомитись із призначеннями каналів та інформацією про їхнє використання!",inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Кожен новий учасник на сервері може отримати початкову роль '@Новоприбулий'. Дана роль надає вам можливість спілкуватись в основних текстових каналах. Щоб підвищувати свою роль вам необхідно активно спілкуватись, адже пункти досвіду надаються за написані повідомлення. Після досягнення рівня '@Незнайомець' ви отримаєте доступ до деяких інших каналів.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Канал '#славетний-плей-лист'  доступний користувачам, які досягли рівня '@Незнайомець'. За допомогою цього каналу ви можете задавати пісні, які хочете послухати у голосовому каналі '#славетні-пісні' . Варто зазначити, що доступ до каналу 'славетні-пісні' мають усі користувачі. Тобто, слухати музику можуть усі, але пропонувати свою лише користувачі, що мають певний рівень на сервері. Детальніше про команди музичного бота шукайте у закріплених повідомленнях каналу '#славетний-плей-лист'.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Канали '#ганебна-сральня' (політичний канал) та '#славетний-бордель' (еротичний канал) є специфічними та орієнтованими на аудиторію 18+. Тому, якщо вам менше років, не заходьте на ці канали. Щоб отримати доступ до цих каналів прочитайте інформацію, що подана нижче. Вам буде видана роль та доступ. Доступ до каналу можуть отримати користувачі із рівнем '@Незнайомець' та вище.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Канали '#славетні-ігромани'  та '#граємо-разом' створені для обговорення різних ігор, кооперації у команди. Доступ до каналу мають усі користувачі, але для цього потрібно отримати відповідну роль. Детальніше про це шукайте нижче.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Голосовий канал '#славетний-кінотеатр' створений для перегляду фільмів.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value= "Голосовий канал '#славетні-базіки' створений для спілкування учасників серверу із рівнем вищим за '@Незнайомець'.",inline=False)
        embed.add_field(name=":red_circle: **Увага** :red_circle:", value="**Адміністрація може видалити вас із каналу із дорослим контентом, якщо запідозрить, що ваш вік не відповідає 18+**", inline=False)
        embed.add_field(name="Опис каналів", value="Текстові канали:", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетна-вітальня' — сповіщення про новачків.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'анонси' — сповіщення про стріми.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні-боти' — команди ботів.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетний-закон' — закон серверу.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні-правила' — правила серверу.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетна флудильня' — буденне спілкування.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'ганебна сральня' — політичні обговорення.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні-ігромани' — ігрова балаканина.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетний бордель' — 18+ контент.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетна-ігрова-галерея' — ігрові знятки (скріншоти).", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетна кімната сміху' — меми, приколи, жарти.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні відясики' — поширення відеороликів.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'клюб' — поширення музики.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетна-історія' — найкращі повідомлення на сервері.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетний-плей-лист” — стіл замовлень музичному боту.", inline=False)
        embed.add_field(name="Опис каналів", value="Голосові канали:", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетний-кінотеатр' — спільний перегляд кіно.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні-базіки' — буденне спілкування.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'граємо разом' — кооперативні ігри.", inline=False)
        embed.add_field(name=":small_red_triangle_down:", value="'славетні-пісні' — спільне прослуховування пісень.", inline=False)

        # embed.add_field(name="Дозволені канали:", value="#славетні-боги, #флудильня", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_member_join(self,member):
        for channel in member.guild.channels:
            if str(channel) == "славетна-вітальня":
                embed = discord.Embed(color=0x88fc03, title=':confetti_ball: Новий користувач долучився до серверу :confetti_ball:')
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name=f"Вітаю тебе, @{member} на славетному сервері Славенія.", value="Сподіваюсь ти станеш частинкою даної спільноти. Перш ніж перейти до ближчого знайомства, пропоную тобі переглянути інформацію про даний сервер та правила у #славетний-закон та #славетні правила. Уважно прочитай усе, лише уважні отримають доступ до усіх каналів :)", inline=False)
                embed.set_footer(text=f"Приємного спілкування {member}", icon_url='https://i.ibb.co/PMKLn81/hi.png')
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        for channel in member.guild.channels:
            if str(channel) == "славетна-вітальня":
                embed = discord.Embed(color=0x097db8, title=':disappointed_relieved: Користувач покинув сервер :disappointed_relieved: ')
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name=f"Користувач, @{member} покинув сервер Славенія.", value="Сподіваємось він запам'ятає час проведений на цьому сервері", inline=False)
                embed.set_footer(text=f"Бувай, {member}", icon_url='https://i.ibb.co/3Ft4mCB/buy.png')
                await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Info(bot))