# 툴을 불러와요, 툴은 README.md (을)를 참조하세요!
from nextcord.ext import commands
import nextcord

bot = commands.Bot(command_prefix='봇의 접두사 입력하기')
TOKEN = "봇의 토큰 입력하기"

@bot.event
async def on_ready():
    print("봇이 준비되었어요!")
    print(f"[!] 참가 중인 서버 : {len(bot.guilds)}개의 서버에 참여 중\n")
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game(f"{len(bot.guilds)}개의 서버에 참여 중이에요!"))

@bot.command()
async def 따라하기(message, text): # 명령어 지정
    # 뭘 할건지 정의
    await message.reply(embed=nextcord.Embed(title='따라하기', description=text, color=0x00ff00))

bot.run(TOKEN)