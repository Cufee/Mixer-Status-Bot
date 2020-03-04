import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle


import json
import os


class server_settings(commands.Cog):
#Cog for adding support for per server settings
    #Startup
    def __init__(self, client):
        self.client = client
        #self.client.FUNC.start()
        print('Cog server_settings was loaded')


    #Tasks
    #Tasks go here

    #Commands
    #Commands go here

#Setup
def setup(client):
    client.add_cog(server_settings(client))