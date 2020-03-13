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
    async def clear(self, ctx, number):
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in self.client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await self.client.delete_messages(mgs)

#Setup
def setup(client):
    client.add_cog(moderation(client))