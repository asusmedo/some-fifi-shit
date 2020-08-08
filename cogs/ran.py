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
from discord.ext import commands
import operator
import utils
import traceback


class  ran(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[])
    async def ask(self,ctx, *, question):
        responses =["As I see it, yes ",
                    "It is decidedly so ",
                    "Without a doubt ",
                    "Yes definitely ",
                    "You may rely on it ",
                    "As I see it yes ",
                    "Most likely ",
                    "She'll be right mate ",
                    "Yes ",
                    "You have a therapist for this ",
                    "I can’t be bothered answering that ",
                    "Ask again later ",
                    "Better not tell you now ",
                    "Get me a Maccas Burger and ask me again ",
                    "Concentrate and ask again ",
                    "Don't count on it ",
                    "My reply is no ",
                    "My sources say no ",
                    "I'm on the piss, gimme a few seconds and ask again ",
                    "Very doubtful ",
                    "I’ve heard just about enough out of you mate, you’d best pull your head in.",
                    "Hey, no one said I knew everything.",
                    "Ask again never ",
                    "Shut up you're drunk ",
                    "Ask ya mum ",
                    "Out of over 7 billion people on this planet, you decided to ask me? ",
                    "Without a doubt. Nah, I’m just messing with you, you’re definitely going to die alone. ",
                    "My sources say no. They also tell me they hate you and hope you burn in hell. ",
                    "Yes, definitely. Unless it doesn’t happen. Listen it’s not my fault your father didn’t love you. Get off my back! ",
                    "All signs point to yes. But on second thought, go fuck yourself. ",
                    "Take a wild guess...",
                    "Without a doubt",
                    "Might be possible",
                    "no... (╯°□°）╯︵ ┻━┻"]
        await ctx.send(f'{random.choice(responses)}')


    





    
    
  
def setup(bot):
    bot.add_cog(ran(bot))