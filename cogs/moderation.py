import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle


class moderation(commands.Cog):
    #Startup
    def __init__(self, client):
        self.client = client
        print('Cog moderation was loaded')


    #Tasks

    #Commands
    @commands.command()
    async def comehere(self, ctx):
        await self.client.delete_message(ctx.message)
        channel = ctx.channel
        await ctx.send(channel, delete_after=30)

    @commands.command(pass_context = True)
    @commands.is_owner()
    #Clear messages in channel
    async def clear(self, ctx, number=1):
        await ctx.send(f'Deleting {number} messages')
        await ctx.channel.purge(limit=number)
        

#Setup
def setup(client):
    client.add_cog(moderation(client))