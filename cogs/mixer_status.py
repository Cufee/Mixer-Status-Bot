import discord
import discord
from discord.ext import commands, tasks
from itertools import cycle


import bs4 as bs
import urllib.request
import json
import os


#Parsing functions
def update_soup_cache():
    status_page_url = 'https://status.mixer.com/'
    sauce = urllib.request.urlopen(status_page_url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/mixer_status/status_cache.html", "w", encoding='utf-8') as cache:
        cache.write(str(soup))
    print('Cache saved')


def get_soup_from_cache():
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/mixer_status/status_cache.html", "r", encoding='utf-8') as cache:
        soup = bs.BeautifulSoup(cache, 'lxml')
    return(soup)


def get_status(soup):
    try:
        status = soup.find('span', class_='status')
        status = status.text.strip()
    except:
        incident = soup.find('div', class_='unresolved-incidents')
        status = incident.find(
            'div', class_='incident-title font-large').text.strip()
    return(status)


def get_status_bool(soup):
    try:
        status = soup.find('span', class_='status').text.strip()
        if 'All Systems Operational' in status:
            status_bool = True
        else:
            status_bool = False
    except:
        status_bool = False
    return(status_bool)


def get_detailed_status(soup):
    status_detailed = {}
    statuses = soup.find_all('div', class_='component-inner-container')
    for item in statuses:
        name = item.find('span', class_='name').text.strip()
        status = item.find('span', class_='component-status').text.strip()
        status_detailed.update({name: status})
    return(status_detailed)


def get_last_incident(soup):
    try:
        incident = soup.find('div', class_='unresolved-incidents')
        incident_updates_all = incident.find_all('div', class_='update')
        incident_updates = []
        for entry in incident_updates_all:
            incident_updates.append(entry.text.strip())
    except:
        incident_updates = 'Looks like there are no updates yet.'
    return(incident_updates)

def print_dict(dct):
    result = ''
    for resource, status in dct.items():
        result += ("\n{} - {}".format(resource, status))
    result = f'```{result}```'
    return(result)


#API lists
mixer_apis = ['Mixer API', 'Interactive API', 'Webhook Delivery']
mixer_web = ['Mixer Web Experience', 'Website Delivery', 'Chat', 'Skills (Sparks and Embers)', 'Dashboard', 'Interactive API', 'Webhook Delivery']
mixer_xbox = ['Mixer Xbox App', 'Skills (Sparks and Embers)', 'Chat', 'Xbox/Windows Notification Delivery']
mixer_video = ['FTL (Low Latency) Video Delivery', 'HLS (Fallback) Video Delivery', 'Video Ingestion', 'Video Distribution']
mixer_vod = ['VOD', 'VOD Uploads', 'VOD Playback']


class mixer_status(commands.Cog):
    #Startup
    def __init__(self, client):
        self.client = client
        self.client.save_cache.start()
        self.client.update_bot_status.start()
        print('Cog mixer_status was loaded')


    #Tasks
    @tasks.loop(minutes=10)
    async def save_cache(self):
        print('Updating local cache')
        update_soup_cache()

    @tasks.loop(minutes=10)
    async def update_bot_status(self):
        status_bool = get_status_bool(get_soup_from_cache())
        status = get_status(get_soup_from_cache())
        if status_bool == True:
            print('Everything is fine')
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(status))
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/mixer_status/img/green.jpg', 'rb') as img:
                await self.client.user.edit(avatar=img.read())
        else:
            print('Something is on fire')
            await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(status))
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/mixer_status/img/yellow.jpg', 'rb') as img:
                await self.client.user.edit(avatar=img.read())


    @commands.command()
    async def status(self, ctx, *, param='none'):
        '''Returns current Mixer status'''
        soup = get_soup_from_cache()
        status_bool = get_status_bool(soup)
        status = get_status(soup)
        status_ext = get_detailed_status(soup)
        result = ''
        if param == 'vod':
            for x in mixer_vod:
                result += ("\n{} - {}".format(x, status_ext[x]))
            result = f'```{result}```'
            await ctx.send(result)
        if param == 'video':
            for x in mixer_video:
                result += ("\n{} - {}".format(x, status_ext[x]))
            result = f'```{result}```'
            await ctx.send(result)
        if param == 'xbox':
            for x in mixer_xbox:
                result += ("\n{} - {}".format(x, status_ext[x]))
            result = f'```{result}```'
            await ctx.send(result)
        if param == 'web':
            for x in mixer_web:
                result += ("\n{} - {}".format(x, status_ext[x]))
            result = f'```{result}```'
            await ctx.send(result)
        if param == 'api':
            for x in mixer_apis:
                result += ("\n{} - {}".format(x, status_ext[x]))
            result = f'```{result}```'
            await ctx.send(result)
        if param == 'all': 
            await ctx.send(print_dict(status_ext))
        if param == 'none':
            if status_bool == False:
                incident_updates = get_last_incident(soup)
                for update in incident_updates:
                    status += f'```{update}```'
            await ctx.send(status)


#Setup
def setup(client):
    client.add_cog(mixer_status(client))