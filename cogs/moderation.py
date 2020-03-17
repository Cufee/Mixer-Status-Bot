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

    #Events


    #Tasks

    #Commands
    @commands.command()
    async def comehere(self, ctx):
        await ctx.message.delete()
        channel = f'I am in {ctx.channel} with ID {ctx.channel.id}'
        await ctx.send(channel, delete_after=10)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    #Clear messages in channel
    async def clear(self, ctx, number=0):
        await ctx.channel.purge(limit=number)
        await ctx.send(f'Deleting {number} messages', delete_after=10)

    @commands.command()
    async def round(self, ctx, number:float):
        number = round(number)
        await ctx.send(number)

#Setup
def setup(client):
    client.add_cog(moderation(client))
