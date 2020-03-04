import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle


import json
import os


class status_alerts(commands.Cog):
#Sets a bot to monitor and reply in a specific channel.
    #Startup
    def __init__(self, client):
        self.client = client
        #self.client.FUNC.start()
        print('Cog status_alerts was loaded')


    #Tasks
    #Tasks go here


    #Commands
    @commands.command()
    async def comehere(self, ctx):
        global channel
        channel = self.client.get_channel()
        await channel.send('Channel saved')

    @commands.command()
    async def test(self, ctx):
        await channel.send('Test')


#Setup
def setup(client):
    client.add_cog(status_alerts(client))