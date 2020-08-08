import discord
import os
from discord.ext import commands
import asyncio
import datetime
import logging
import redis
from time import gmtime, strftime
import colorama
from colorama import Fore, Back, Style
import random
import time
import requests
import nekos
from discord.ext.commands import has_permissions, CheckFailure
import sys
import io
import urllib
import json
import math
from bs4 import BeautifulSoup
import praw
from dotenv import load_dotenv
import asyncio
import random
import aiohttp
from io import BytesIO
from random import choice
import urllib.parse
from urllib.parse import quote
import requests
from discord import Game
import js
from typing import List
import discord
import colorsys
from discord.ext import commands
import operator
import utils
import traceback
client = discord.Client()
initialised = False

def rgb_to_colour(rgb):
    rgb = list(map(lambda x: int(x*255), rgb))
    return discord.Colour((256**2)*rgb[0] + 256*rgb[1] + rgb[2])

@client.event
async def on_ready():
    global initialised
    if not initialised:
        initialised = True
        flash_server = None
        flash_role = None

        for server in client.guilds:
            if server.id == "705495483707031583":
                flash_server = server
                break

        for role in flash_server.roles:
            if role.id == "707796490776608818":
                flash_role = role
                break

        colour_count = 20
        colours = [rgb_to_colour(colorsys.hsv_to_rgb(i/colour_count, 1, 1)) for i in range(colour_count)]
        colour_index = 0

        while True:
            time.sleep(1)
            colour_index = (colour_index + 1) % len(colours)
            await role.edit(flash_server, flash_role, colour=colours[colour_index])
            print(colour_index)

client.run('NzA3MDQ0MzQ1Mjk5MjA2MTQ0.XrYj-g.fmYsK38p8dhTVg26-mPsbjKUHXs')