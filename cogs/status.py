import discord
from discord.ext import commands

# customize_bot cog

class mixer_status(commands.Cog):

    def __init__(self, client):
        self.client = client


    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'mixer_status cog is ready.')


    #Commands
    @commands.command()
    @commands.is_owner()
    async def setgame(self, ctx, *, game=''):
        '''Set game playing status.'''
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(game))
        print(f'Ran setgame')


def setup(client):
    client.add_cog(mixer_status(client))