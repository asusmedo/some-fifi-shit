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

load_dotenv()
TOKEN = os.getenv('NzA3MDQ0MzQ1Mjk5MjA2MTQ0.XrUYJg.rOo2Spq4dpLIw00NuM67ERTzf3o')
client = discord.Client()
parsed_json = (json.loads(open("url.json", "r").read()))

BOT_PREFIX = ("?", "!", ".")
class  nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    

    


    @commands.Cog.listener()
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.bot:
            return

        

            if message.mentions is not None and len(message.mentions) > 0 and message.channel.nsfw:
                args = message.content[1:].split(' ');
                action = args[0]
                if action.endswith("ss"):
                    action = action + "es"
                else:
                    action = action + "s"

                if args[1] != "<@!" + str(message.mentions[0].id) + ">":
                    embed = discord.Embed(
                        description=message.author.name + " " + action + " the " + args[1] + " of " + message.mentions[
                            0].mention)
                    embed.set_image(url=random.choice(parsed_json[args[0]][args[1]]))
                else:
                    embed = discord.Embed(
                        description=message.author.name + " " + action + " " + message.mentions[0].mention)
                    embed.set_image(url=random.choice(parsed_json[args[0]]["main"]))

                await message.channel.send(embed=embed)
            #else:
                    #embed = discord.Embed(description="Please make shure that you are in a NSFW Channel and you enter the command like this:\n```!command @Mention\nor\n!command command @Mention```")
                    #await message.channel.send(embed=embed)














                               


def setup(bot):
    bot.add_cog(nsfw(bot))