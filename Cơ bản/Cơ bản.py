#pip install discord
#https://discordpy.readthedocs.io/en/latest/api.html
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="", case_insensitive=True)
GUILD_ID = int
CHANNEL_ID = int

@bot.event
async def on_ready():
    print('Bruh')
    print(f'{bot.user}')
    bot.add_cog(Greetings(bot))#tạo Cogs
    bot.get_cog('Greetings')#Nhận cogs vừa tạo
    print('Greetings đang hoạt động')
    await bot.get_channel(CHANNEL_ID).send('Bot đang online')

@bot.event
async def on_message(message):
    global content
    global say
    global author
    global inbox
    content = message.content
    say = message.channel.send
    author = message.author
    inbox = message.author.send
    guildsd = bot.get_guild(GUILD_ID)#Đôi khi bot không nhận biết được vị trí server hoặc channel cụ thể
    channelsd = bot.get_channel(CHANNEL_ID)#Vậy nên ta sẽ gán cho nó vị trí cụ thể bằng id của nó
    for member in guildsd.members:
        if author == bot.user:#bot luôn luôn đặt vị trí member của bot ở đầu tiên vậy nên code bot.user sẽ luôn bằng bot của bạn
            return
        if 'member' in content:
            await say(member)
        if 'test' in content:
            await say('s')
        if 'emoj' in content:
            await message.add_reaction('<:exreset:748753325222002769>')#thêm emoji vào câu vừa chat
            channel = message.channel
            await channel.send('Gửi tôi cái emoji <:exreset:748753325222002769>')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji.id) == '748753325222002769'

            try:
                reaction = await bot.wait_for('reaction_add', check=check)
            except AttributeError:
                await channel.send('👎')
            else:
                await channel.send('👍')
        if 'xóa' in content:
            xóa = int(content[4])
            try:
                if str(xóa) in content:
                    if str(int(content[5])) in content:
                        xóa = int(content[4:6])
                        if str(int(content[6])):
                            xóa = int(content[4:7])
                    await message.channel.purge(limit=xóa)
                    await say(f'Đã xóa {xóa} tin nhắn')
            except IndexError:
                await message.channel.purge(limit=xóa)
                await say(f'Đã xóa {xóa} tin nhắn')
            return
        
        
        if 'show' in content:#một số dòng code liên quan đến class guild
            if 'emojs' in content:
                await say(guildsd.emojis)#Hiển thị tất cả loại emoji của guild đó
            if 'region' in content:
                await say(guildsd.region)#Hiển thị quốc gia của guild đó
            if 'gicon' in content:
                await say(guildsd.icon)
            if 'features' in content:
                await say(guildsd.features)



#Cogs
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))
    @commands.Cog.listener()
    async def on_message(self, message):
        if author == self.bot.user:
            return
        if 'test' in content:
            await say('test')
        if 'fileee' in content:#gửi file trong máy(không quan trọng là file gì nhưng dung lượng file phải <= 8mb)
            await say(file=discord.File('bruh.py'))
        if 'del' in content:
            await message.delete(delay=2)#xóa tin nhắn sau delay
            await say('tes')
        if 'embed' in content:
            embed = discord.Embed(description='duh')#Gửi tin nhắn nhưng được nhúng
            await say(embed=embed)
bot.run('TOKEN')
