import discord
import os
import json
import discord
from discord.ext import commands, tasks

#Startup
with open(f'{os.path.dirname(os.path.realpath(__file__))}/settings.json') as f:
    settings = json.load(f)    
TOKEN = settings["TOKEN"]
mode = settings["mode"]
prefix = settings["prefix"]
default_game = settings["default_game"]
client = commands.Bot(command_prefix = prefix)

#Startup
@client.event
async def on_ready():
    print(f'{client.user.name} online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(default_game))


#Tasks
#Some task goes here

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

for filename in os.listdir(f'{os.path.dirname(os.path.realpath(__file__))}/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#Run
client.run(TOKEN)