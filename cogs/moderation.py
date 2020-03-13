import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio


class moderation(commands.Cog):
    #Startup
    def __init__(self, client):
        self.client = client
        print('Cog moderation was loaded')


    #Tasks

    #Commands
    @commands.command()
    async def comehere(self, ctx):
        await ctx.message.delete()
        channel = ctx.channel
        await ctx.send(channel, delete_after=10)

    @commands.command(pass_context = True)
    @commands.is_owner()
    #Clear messages in channel
    async def clear(self, ctx, number=1):
        await ctx.channel.purge(limit=number)
        await ctx.send(f'Deleting {number} messages', delete_after=10)
        

#Setup
def setup(client):
    client.add_cog(moderation(client))