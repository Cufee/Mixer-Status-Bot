import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle


import json
import os


class set_channel(commands.Cog):
#Sets a bot to monitor and reply in a specific channel.
    #Startup
    def __init__(self, client):
        self.client = client
        #self.client.FUNC.start()
        print('Cog set_channel was loaded')


    #Tasks
    #Tasks go here


    #Commands
    #Commands go here

#Setup
def setup(client):
    client.add_cog(set_channel(client))