import discord
import os 
import re

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

CHANNEL_BOT_SPAM_ID = 403045420625952778
CHANNEL_MAGGIE_NANCY_ID = 788259241064136726


client = discord.Client()


class CustomClient(discord.Client):
    def __init__(self, loop=None, options=None):
        super(CustomClient, self).__init__()
        self.channel_bot_spam = None
        self.channel_maggie_nancy = None
        self.guild = None

    async def on_ready(self):
        self.guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{self.guild.name}(id: {self.guild.id})'
        )
        self.channel_bot_spam = self.guild.get_channel(CHANNEL_BOT_SPAM_ID)
        self.channel_maggie_nancy = self.guild.get_channel(CHANNEL_MAGGIE_NANCY_ID)


    async def on_message(self, message):
        if message.author == client.user:
            return

        if (
            message.channel == self.channel_bot_spam 
            or message.channel == self.channel_maggie_nancy
        ):
            total_bans = countBans(''.join(message.content.lower().split()))
            
            if total_bans > 1:
                await message.channel.send(f'[{total_bans}x Banned!]')
            elif total_bans == 1:
                await message.channel.send(f'[Banned!]')


BAN_PATTERN = re.compile('(n+a+n+c+y+)|(m+a+g+i+e+)|(n+y+a+n+c+y+)|(n+y+a+g+i+e+)')
def countBans(message: str) -> int:
    return len(BAN_PATTERN.findall(message))


def makeRandImage(data_stream):
    return discord.File(fp=data_stream, filename="RandomImage")
    

if __name__ == '__main__':
    print('starting bot...')
    client = CustomClient()
    client.run(TOKEN)