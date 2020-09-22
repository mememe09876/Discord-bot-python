#pip install discord
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print('Bruh')
    bot.add_cog(Greetings(bot))
    bot.get_cog('Greetings')
    if Greetings == None:
        print('Greetings chưa được hoạt động')
    if Greetings is not None:
        print('Greetings đang hoạt động')



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
    if 'test' in content:
        await say('bruh')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_ready(self):
        print('eyyo')

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'bruh' in content:
            await say('bruh')
bot.run('TOKEN')

