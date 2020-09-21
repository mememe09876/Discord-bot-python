#pip install discord
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='')

#import ở file client vài hàm code
@bot.event
async def on_ready():
    print('Bruh')


@bot.event
async def on_message(message):
    #Rút gọn message.content,message.channel.send,message.author,message.author.send
    content = message.content #message.content là nội dung câu chat của bạn
    global say
    say = message.channel.send
    author = message.author
    inbox = message.author.send
    #Khi người chat có id bằng id bot thì những code đằng sau không được dùng tới
    if message.author.id == bot.user.id:
        return
    #Nếu Bruh hoặc Cheems trong nội dung chat của bạn
    if 'Bruh' or 'Cheems' in content:
        await bruh(message)#liên kết tới hàm bruh(message)
async def bruh(message):
    await say('Bruh')
bot.run('Token bot của bạn')

