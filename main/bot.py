import discord
import testbot
from discord.ext import commands
from datetime import datetime

# กำหนดค่า Token ที่คุณคัดลอกมาจาก Developer Portal
TOKEN =''

# สร้างบอทเป็น Client ของ discord.py
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# เหตุการณ์เมื่อบอทเรียกพร้อมใช้งาน
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    # ตั้งค่าสถานะของบอท
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="เกมส์"))


# คำสั่ง !hello ที่บอทจะตอบกลับ
@bot.command()
async def test(ctx):
    await ctx.send('Hello, I am your Discord bot!')


@bot.command()
async def checkid(ctx):
    await ctx.send(f'your ID is : {ctx.author.id}')


@bot.command()
async def avatar(ctx):
    await ctx.send(f'{ctx.author.avatar}')


@bot.command()
async def profile(ctx):

    embed = discord.Embed(
        title=f"{ctx.author.display_name}",
        description=f"AKA : {ctx.author.name}",
        color=discord.Color.green()
    )
    embed.add_field(
        name='Name',
        value=f'{ctx.author.name}'
    )
    embed.add_field(
        name='Student ID',
        value='64015087'
    )
    embed.set_thumbnail(url=f'{ctx.author.avatar}')

    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f"The result of {a} + {b} is {result}")


@bot.command()
async def dev(ctx):
    devs = [
        {'FirstName': 'Piyarot', 'LastName': 'Khantichat', 'Student ID': '64015087', 'Color': discord.Color.green(
        ), 'ThumbnailURL': 'https://img.freepik.com/premium-photo/japanese-girl-cherry-blossom-tree-landscape-anime-manga-illustration_691560-7776.jpg?w=2000'},
        {'FirstName': 'John', 'LastName': 'Doe', 'Student ID': '12345678',
            'Color': discord.Color.blue(), 'ThumbnailURL': 'https://example.com/john.jpg'},
        {'FirstName': 'Jane', 'LastName': 'Smith', 'Student ID': '87654321',
            'Color': discord.Color.orange(), 'ThumbnailURL': 'https://example.com/jane.jpg'}
    ]

    for dev_info in devs:
        current_time = datetime.now().strftime('%H:%M น. %d/%m/%Y')

        embed = discord.Embed(
            title="Developer",
            description="",
            color=dev_info['Color']
        )

        name_field = f"{dev_info['FirstName']} {dev_info['LastName']}"
        embed.add_field(name='Name', value=name_field)

        student_id_field = f"\n{dev_info['Student ID']}"
        embed.add_field(name='Student ID', value=student_id_field)

        embed.set_thumbnail(url=dev_info['ThumbnailURL'])
        embed.set_footer(
            text=current_time, icon_url='https://encrypted-tbn2.gstatic.com/faviconV2?url=https://freepik.com&client=VFE&size=64&type=FAVICON&fallback_opts=TYPE,SIZE,URL&nfrp=2')

        await ctx.send(embed=embed)


# ตอบกลับข้อความ



@bot.event
async def on_message(message):
    if message.author == bot.user:  # ไม่ตอบกลับถ้าข้อความเป็นของบอทเอง
        return

    else:
        text = testbot.chattotalk(message.content)
        
        await message.channel.send(f'{message.author.mention} {text}')

    await bot.process_commands(message)


# รันบอทด้วย Token
bot.run(TOKEN)
