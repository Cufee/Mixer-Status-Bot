import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle

import os
import json


#Startup
with open(f'{os.path.dirname(os.path.realpath(__file__))}/settings.json') as f:
    settings = json.load(f)    
TOKEN = settings["TOKEN"]
mode = settings["mode"]
prefix = settings["prefix"]
default_game = settings["default_game"]
client = commands.Bot(command_prefix = prefix, case_insensitive=True)


#Startup
@client.event
async def on_ready():
    print(f'{client.user.name} online!')
    for filename in os.listdir(f'{os.path.dirname(os.path.realpath(__file__))}/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


#Tasks
#Root tasks go here


#Root Commands
@client.command(hidden=True)
@commands.is_owner()
async def startupdate(ctx):
    print('Starting update')
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/cogs/mixer_status/img/update.jpg', 'rb') as img:
        await client.user.edit(avatar=img.read())
    client.close()


#Cog managment
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} extension.')

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension='null'):
    if extension == 'null':
        await ctx.send(f'No extension name specified.')
    else:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded {extension} extension.')

@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension='null'):
    if extension == 'null':
        await ctx.send(f'No extension name specified.')
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension} extension.')

@client.command(hidden=True)
@commands.is_owner()
async def listcogs(ctx):
    cogs = []
    for filename in os.listdir(f'{os.path.dirname(os.path.realpath(__file__))}/cogs'):
        if filename.endswith('.py'):
            cogs.append(f'{filename[:-3]}')
    await ctx.send(f'Found these cogs:\n{cogs}')


#Run
client.run(TOKEN)
