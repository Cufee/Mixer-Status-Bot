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
    status_page_url = 'https://beta.support.xbox.com/xbox-live-status?xr=shellnav'
    sauce = urllib.request.urlopen(status_page_url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/xbox_status/status_cache.html", "w", encoding='utf-8') as cache:
        cache.write(str(soup))
    print('[XBOX]Cache saved')


def get_soup_from_cache():
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/xbox_status/status_cache.html", "r", encoding='utf-8') as cache:
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


class xbox_status(commands.Cog):
    #Startup
    def __init__(self, client):
        self.client = client
        print('Cog xbox_status was loaded')


    #Tasks


    #Commands


#Setup
def setup(client):
    client.add_cog(xbox_status(client))