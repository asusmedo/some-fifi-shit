
import os
import re
import time
from datetime import datetime
import random
import requests
import logging
import discord
import traceback
import redis
import math
import discord
import praw
import json
import random
from discord.ext  import commands
import asyncio
import urllib
import random
import random2
import discord
import requests
from discord.ext import commands
from discord import Game
from random import choice
import re
import sys
import os
import discord
import utils
import asyncio

client = discord.Client()




class dada(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author.bot:
            return;

        channel = message.channel

        

        words = message.content.split();

        for idx,word in enumerate(words):
            lwrcase = word.lower();
            if  lwrcase == "iam"  :
                await channel.send('Hi ' + words[idx+1] + ", I'm Fofa!");
            

    
def setup(bot):
    bot.add_cog(dada(bot))