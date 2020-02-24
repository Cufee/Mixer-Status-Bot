import discord
from discord.ext import commands

# customize_bot cog

class user_commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'user_commands cog is ready.')


    #Commands
    @commands.command(aliases=['ping'])
    async def pulse(self, ctx):
        '''Test if the bot is alive, returns ping.'''
        await ctx.send(f'I live! My latency is {round(self.client.latency * 1000)}ms')
        print('Ran pulse')


def setup(client):
    client.add_cog(user_commands(client))