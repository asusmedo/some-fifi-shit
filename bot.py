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
from discord.utils import get
from asyncio import sleep
from datetime import datetime







client = commands.Bot(command_prefix ='*')
client.remove_command('help')

extensions = ['cogs.ban', 'cogs.CommandEvents', 'cogs.kickcmd', 'cogs.clears',
'cogs.ran', 'cogs.avatar', 'cogs.userinfo','cogs.errors', 'cogs.mute',
'cogs.Command','cogs.help', 'cogs.delete',   'cogs.warn', 'cogs.membercount', 'cogs.dada']



if __name__== '__main__':
    for ext in extensions:
        client.load_extension(ext)











@client.event
async def on_ready():
        print('Bot Logged in ')
        print('**************')
        
       
        client.load_extension('cogs.music')
        client.load_extension('cogs.polls')
        client.load_extension('cogs.admin')
        
        

        








@client.command()
async def info(ctx):
    

    embed = discord.Embed(
        colour=discord.Color.purple()
    )
    embed.set_author(name="Info")
    embed.add_field(name="Creator:", value='Mister Lister 69', inline=False)
    embed.add_field(name="version:", value='69.69', inline=False)
    embed.add_field(name="what is new ?", value='Fifi Music is now Early Access !!! Enjoy using it !  ' + ' , Added bugs to fix later', inline=False)
    await ctx.send(embed=embed)







    


@client.event
async def on_member_remove(member):
    print(f'{member} has left')


@client.command()
async def ping(ctx):
    await ctx.send(f"Surprise motherfucker in {round(client.latency * 1000)}ms")
    print(
        Fore.WHITE + "[" + Fore.YELLOW + '+' + Fore.WHITE + "]" + Fore.YELLOW + f"{ctx.author.name} executed command !ping result:{round(client.latency * 1000)}ms ")


# shit





# @client.command()
# async def kick(ctx, member : discord.Member, *, reason = None):
#   await ctx.member.name.send(f"kicked {member.name} for {reason} by {ctx.message.author} from {message.guild} ")
#  await member.kick(reason=reason)
# await ctx.channel.send(f"kicked {member.name} for {reason} by {ctx.message.author} ")


# @client.command()
# async def unban(ctx, *, member):
#   banned_users= await ctx.guild.bans()
#  member_name, member_discriminator = member.split("#")

# for ban_entry in banned_users:
#    user = ban_entry.user
#   if(user.name, user.discriminator) == (member_name, member_discriminator):
#   await ctx.guild.unban(user)
#  await ctx.channel.send(f"unbanned {user.name}")


####################################/////////////////////////////////////////////////////NSFW SHIT////////////////////////////////////////////////////####################################

@client.command()
async def feet(ctx):
    try:
        
        if not ctx.channel.is_nsfw():
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object

    except:
        print('bruh')
        print('bruh')

    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='feet doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    feet = nekos.img("feet")

    embed.set_image(url=feet)

    await ctx.send(embed=embed)


# print(Fore.WHITE + "["+ Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA+ f"{ctx.author.name} executed command !feet result: {feet}   time:{round(client.latency * 1000)}ms")

# YURI
@client.command()
async def yuri(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='yuri doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    yur1 = nekos.img("yuri")

    embed.set_image(url=yur1)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !yuri result: {yur1}   time:{round(client.latency * 1000)}ms")


# traps (gay)
@client.command()
async def trap(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        embed = discord.Embed(
            title='traps are gay',
            description='',
            colour=discord.Colour.from_rgb(r , g, b)
        )
    trap = nekos.img("trap")

    embed.set_image(url=trap)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !trap result: {trap}   time:{round(client.latency * 1000)}ms")


# futanari {tbh dont know what this is}
@client.command()
async def futanari(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        embed = discord.Embed(
            title='futanari doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    futanari = nekos.img("futanari")

    embed.set_image(url=futanari)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !futanari result: {futanari}   time:{round(client.latency * 1000)}ms")


# holowed {dk what this is either}
@client.command()
async def hololewd(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        embed = discord.Embed(
            title='hololewd doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r , g, b)
        )
    hololewd = nekos.img("hololewd")

    embed.set_image(url=hololewd)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hololewd result: {hololewd}   time:{round(client.latency * 1000)}ms")


@client.command()
async def lewdkemo(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='lewdkemo doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    lewdkemo = nekos.img("lewdkemo")

    embed.set_image(url=lewdkemo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewdkemo result: {lewdkemo}   time:{round(client.latency * 1000)}ms")


##################
@client.command()
async def solo_gif(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=':flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    solog = nekos.img("solog")

    embed.set_image(url=solog)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !solog result: {solog}   time:{round(client.latency * 1000)}ms")


#######################
@client.command()
async def feet_gif(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='feet :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    feetg = nekos.img("feetg")

    embed.set_image(url=feetg)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !feetg result: {feetg}   time:{round(client.latency * 1000)}ms")


#####################
@client.command()
async def cum(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='cum :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    cum = nekos.img("cum")

    embed.set_image(url=cum)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !cum result: {cum}   time:{round(client.latency * 1000)}ms")


##################################
@client.command()
async def erokemo(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='erokemo :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    erokemo = nekos.img("erokemo")

    embed.set_image(url=erokemo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !erokemo result: {erokemo}   time:{round(client.latency * 1000)}ms")


#########################################
@client.command()
async def les(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='les :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    les = nekos.img("les")

    embed.set_image(url=les)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !les result: {les}   time:{round(client.latency * 1000)}ms")


######################################
@client.command()
async def wallpaper(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='wallpaper :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    wallpaper = nekos.img("wallpaper")

    embed.set_image(url=wallpaper)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !wallpaper result: {wallpaper}   time:{round(client.latency * 1000)}ms")


###############################################################

@client.command()
async def lewdk(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='lewdk :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    lewdk = nekos.img("lewdk")

    embed.set_image(url=lewdk)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewdk result: {lewdk}   time:{round(client.latency * 1000)}ms")


############################################################
@client.command()
async def neko_gif(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='ngif :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g ,b)
    )
    ngif = nekos.img("ngif")

    embed.set_image(url=ngif)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !ngif result: {ngif}   time:{round(client.latency * 1000)}ms")


############################################################
@client.command()
async def meow(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='meow :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    meow = nekos.img("meow")

    embed.set_image(url=meow)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !meow result: {meow}   time:{round(client.latency * 1000)}ms")


###########################################################
@client.command()
async def tickle(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} tickled {member.name} because {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    tickle = nekos.img("tickle")

    embed.set_image(url=tickle)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !tickle result: {tickle}   time:{round(client.latency * 1000)}ms")


###########################################################

@client.command()
async def lewd(ctx):
    if not ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        embed = discord.Embed(
            title='lewd doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    lewd = nekos.img("lewd")

    embed.set_image(url=lewd)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewd result: {lewd}   time:{round(client.latency * 1000)}ms")


###################################################################
@client.command()
async def feed(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} fed {member.name} because {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    feed = nekos.img("feed")

    embed.set_image(url=feed)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !feed result: {feed}   time:{round(client.latency * 1000)}ms")


################################################################
@client.command()
async def gecg(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='gecg :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    gecg = nekos.img("gecg")

    embed.set_image(url=gecg)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !gecg result: {gecg}   time:{round(client.latency * 1000)}ms")


##############################################################
@client.command()
async def eroyuri(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='eroyuri :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    eroyuri = nekos.img("eroyuri")

    embed.set_image(url=eroyuri)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !eroyuri result: {eroyuri}   time:{round(client.latency * 1000)}ms")


###############################################################
@client.command()
async def eron(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='eron :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    eron = nekos.img("eron")

    embed.set_image(url=eron)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !eron result: {eron}   time:{round(client.latency * 1000)}ms")


############################################################
@client.command()
async def bj(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='bj :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    bj = nekos.img("bj")

    embed.set_image(url=bj)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !bj result: {bj}   time:{round(client.latency * 1000)}ms")


@client.command()
async def nsfw_neko_gif(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    nsfw_neko_gif = nekos.img("nsfw_neko_gif")

    embed.set_image(url=nsfw_neko_gif)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !nsfw_neko_gif result: {nsfw_neko_gif}   time:{round(client.latency * 1000)}ms")


###########################################################################
@client.command()
async def solo(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    solo = nekos.img("solo")

    embed.set_image(url=solo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !solo result: {solo}   time:{round(client.latency * 1000)}ms")


############################################################################
@client.command()
async def kemonomimi(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    kemonomimi = nekos.img("kemonomimi")

    embed.set_image(url=kemonomimi)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !kemonomimi result: {kemonomimi}   time:{round(client.latency * 1000)}ms")


###################################################################

@client.command()
async def gasm(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} is in awe with {member.name} because {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g ,b)
    )
    gasm = nekos.img("gasm")

    embed.set_image(url=gasm)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !gasm result: {gasm}   time:{round(client.latency * 1000)}ms")


####################################################################
@client.command()
async def nsfw_avatar(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    nsfw_avatar = nekos.img("nsfw_avatar")

    embed.set_image(url=nsfw_avatar)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !nsfw_avatar result: {nsfw_avatar}   time:{round(client.latency * 1000)}ms")


#######################################################################
@client.command()
async def poke(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} poked {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    poke = nekos.img("poke")

    embed.set_image(url=poke)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !poke result: {poke}   time:{round(client.latency * 1000)}ms")

######################################################################

######################################################################
@client.command()
async def anal(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    anal = nekos.img("anal")

    embed.set_image(url=anal)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !anal result: {anal}   time:{round(client.latency * 1000)}ms")


####################################################################################################################################
@client.command()
async def slap(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} slapped {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    slap = nekos.img("slap")

    embed.set_image(url=slap)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !slap result: {slap}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def hentai(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    hentai = nekos.img("hentai")

    embed.set_image(url=hentai)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hentai result: {hentai}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def avatar(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    avatar = nekos.img("avatar")

    embed.set_image(url=avatar)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hentai result: {avatar}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def erofeet(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    erofeet = nekos.img("erofeet")

    embed.set_image(url=erofeet)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !erofeet result: {erofeet}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def pussy(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    pussy = nekos.img("pussy")

    embed.set_image(url=pussy)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !pussy result: {pussy}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def tits(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    tits = nekos.img("tits")

    embed.set_image(url=tits)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !tits result: {tits}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def waifu(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    waifu = nekos.img("waifu")

    embed.set_image(url=waifu)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !waifu result: {waifu}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def boobs(ctx):
    if not ctx.channel.is_nsfw():
        
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    boobs = nekos.img("boobs")

    embed.set_image(url=boobs)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !boobs result: {boobs}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def smallboobs(ctx):
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.blurple()
    )
    smallboobs = nekos.img("smallboobs")

    embed.set_image(url=smallboobs)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !smallboobs result: {smallboobs}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def pat(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} petted {member.name}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    pat = nekos.img("pat")

    embed.set_image(url=pat)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !pat result: {pat}   time:{round(client.latency * 1000)}ms")


#####################################################################################################################################
@client.command()
async def kiss(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} kissed {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    kiss = nekos.img("kiss")

    embed.set_image(url=kiss)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !kiss result: {kiss}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def spank(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} spanked {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    spank = nekos.img("spank")

    embed.set_image(url=spank)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !spank result: {spank}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def cuddle(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} cuddled {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    cuddle = nekos.img("cuddle")

    embed.set_image(url=cuddle)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !cuddle result: {cuddle}   time:{round(client.latency * 1000)}ms")


########################################################################################################################################
@client.command()
async def hugs(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} hugged {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    hug = nekos.img("hug")

    embed.set_image(url=hug)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hug result: {hug}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def fox_girl(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    fox_girl = nekos.img("fox_girl")

    embed.set_image(url=fox_girl)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !fox_girl result: {fox_girl}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def neko(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' nekos:flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.img("neko")

    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")


@client.command()
async def contribute(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='contributon',
        description='you may contribute to the project on our github page. the current features on our add list are: ``music playing, sound playing, and further implemantation of the api``',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.img("neko")

    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")

@client.command()
async def wordsfromgod(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    word_site = "https://www.wordgenerator.net/application/p.php?id=dictionary_words&type=1&spaceflag=true"

    response = requests.get(word_site)
    wordy = response.content.decode()
    bruh = wordy.replace(",", " ")


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    embed.set_author(name="God says:")
    embed.add_field(name=bruh[0:256], value=None, inline=False)
    await ctx.send(embed=embed)




@client.command()
async def cv(ctx, reason="None"):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    r = requests.get('https://corona-stats.online/' + reason + '?format=json')
    
    embed.set_author(name=r.json()['data'][0]['country'])
    embed.add_field(value='cases:', name="===========================", inline=False)
    embed.add_field(value='cases today:', name=r.json()['data'][0]['cases'], inline=False)
    embed.add_field(value="recovered:", name=r.json()['data'][0]['todayCases'], inline=False)
    embed.add_field(value="deaths:", name=r.json()['data'][0]['recovered'], inline=False)
    embed.add_field(value="died today:", name=r.json()['data'][0]['deaths'], inline=False)
    embed.add_field(value="active:", name=r.json()['data'][0]['todayDeaths'], inline=False)
    embed.add_field(value="critical condition:", name=r.json()['data'][0]['active'], inline=False)
    world = "-=worldwide=- cases:" , r.json()['worldStats']['cases'] , " cases today: " , r.json()['worldStats']['todayCases'] , " deaths: " , r.json()['worldStats']['deaths'] , " died today" , r.json()['worldStats']['todayDeaths'] , " recovered: " , r.json()['worldStats']['recovered'] , " critical: " , r.json()['worldStats']['critical'] , " cases per one million: " , r.json()['worldStats']['casesPerOneMillion']
    embed.add_field(value=world, name=r.json()['data'][0]['critical'], inline=False)
    embed.set_author(name=r.json()['data'][0]['country'], icon_url=r.json()['data'][0]['countryInfo']['flag'])
    await ctx.send(embed=embed)
# dummy token in here, well its a dummy now. appearantly discord has a web crawler that found my bots token in here. pretty damn cool.





####Comliments##### add Compliments to a json file later
compliments = [
    ("You look beautiful today ❤️"),
    ("That smile suits your style. Keep it!"),
    ("You're the best you I've ever met"),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You deserve a promotion."),
    ("Every other country is super jealous you're a citizen in this country."),
    ("I appreciate all of your opinions."),
    ("I like your style."),
    ("Your pet loves you too much to ever run away."),
    ("I love what you've done with the place."),
    ("You are like a spring flower; beautiful and vivacious."),
    ("I am utterly disarmed by your wit."),
    ("The kid you passed on the street today wants to grow up to be like you."),
    ("You complete me."),
    ("Well done!"),
    ("Your prom date still thinks about you all the time."),
    ("You pick the best radio stations when you're riding shotgun."),
    ("Your cousins refer to you as 'the cool cousin'."),
    ("You have a good taste in websites."),
    ("Your mouse told me that you have very soft hands."),
    ("You are full of youth."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You have a good web-surfing stance."),
    ("You should be a poster child for poster children."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("I appreciate you more than Santa appreciates chimney grease."),
    ("I wish I was your mirror."),
    ("I find you to be a fountain of inspiration."),
    ("You have perfect bone structure."),
    ("I disagree with anyone who disagrees with you."),
    ("Way to go!"),
    ("Have you been working out?"),
    ("With your creative wit, I'm sure you could come up with better compliments than me."),
    ("I wish I was your mirror."),
    ("You are so charming."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You're tremendous!"),
    ("You deserve a compliment!"),
    ("Hello, good looking."),
    ("Your cousins refer to you as 'the cool cousin'."),
    ("You deserve a compliment!"),
    ("You are quite strapping."),
    ("I am grateful to be blessed by your presence."),
    ("Say, aren't you that famous model from TV?"),
    ("Take a break; you've earned it."),
    ("Your life is so interesting!"),
    ("You deserve a compliment!"),
    ("I would enjoy spending time with you."),
    ("I would share my dessert with you."),
    ("If I had a nickel for everytime you did something stupid, I'd be broke!"),
    ("You deserve a compliment!"),
    ("I would love to visit you, but I live on the Internet."),
    ("I love the way you click."),
    ("You're invited to my birthday party."),
    ("All of your ideas are brilliant!"),
    ("If I freeze, it's not a computer virus.  I was just stunned by your beauty."),
    ("You're spontaneous, and I love it!"),
    ("You should try out for everything."),
    ("You make my data circuits skip a beat."),
    ("You are the gravy to my mashed potatoes."),
    ("You get an A.!"),
    ("I'm jealous of the other websites you visit, because I enjoy seeing you so much!"),
    ("I would enjoy a roadtrip with you."),
    ("If I had to choose between you or Mr. Rogers, it would be you."),
    ("I like you more than the smell of Grandma's home-made apple pies."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("I would trust you to pick out a pet fish for me."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You're so smart!"),
    ("We should start a band."),
    ("You're cooler than ice-skating Fonzi."),
    ("I heard you make really good French Toast."),
    ("You deserve a compliment!"),
    ("You're pretty groovy, dude."),
    ("When I grow up, I want to be just like you."),
    ("I told all my friends about how cool you are."),
    ("You're #1 in my book!"),
    ("You're sweeter than than a bucket of bon-bons!"),
    ("You're pretty high on my list of people with whom I would want to be stranded on an island."),
    ("You're a beautiful person!"),
    ("You are well groomed."),
    ("You could probably lead a rebellion."),
    ("Is it hot in here or is it just you?"),
    ("<3"),
    ("You are more fun than a Japanese steakhouse."),
    ("You're so beautiful, you make me walk into things when I look at you. "),
    ("I support all of your decisions. "),
    ("You are as fun as a hot tub full of chocolate pudding."),
    ("I support all of your decisions. "),
    ("I don't speak much English, but with you all I really need to say is beautiful."),
    ("Being awesome is hard, but you'll manage."),
    ("Your skin is radiant. "),
    ("You will still be beautiful when you get older. "),
    ("You could survive a zombie apocalypse. "),
    ("You make me :) "),
    ("I wish I could move your furniture."),
    ("I think about you while I'm on the toilet. "),
    ("You're so rad."),
    ("You're more fun than a barrel of monkeys. "),
    ("You're nicer than a day on the beach. "),
    ("Your glass is the fullest. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("You look so perfect. "),
    ("The only difference between exceptional and amazing is you. "),
    ("Last night I had the hiccups, and the only thing that comforted me to sleep was repeating your name over and over. "),
    ("Shall I compare thee to a summer's day?  Thou art more lovely and more temperate. "),
    ("Your eyebrows really make your pretty eyes stand out."),
    ("Shall I compare thee to a summer's day?  Thou art more lovely and more temperate."),
    ("I love you more than bacon! "),
    ("You intrigue me. "),
    ("You make me think of beautiful things, like strawberries. "),
    ("I would share my seat with you. "),
    ("Being awesome is hard, but you'll manage."),
    ("Even though this goes against everything I know, I think I'm in love with you. "),
    ("You're more fun than bubble wrap. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("You make babies smile. "),
    ("You make the gloomy days a little less gloomy. "),
    ("You are warmer than a Snuggie."),
    ("You make me feel like I am on top of the world."),
    ("Playing video games with you would be fun."),
    ("You're more cuddly than the Downy Bear."),
    ("I would do your taxes any day."),
    ("You are a bucket of awesome."),
    ("You are the star of my daydreams. "),
    ("If you really wanted to, you could probably get a bird to land on your shoulder and hang out with you. "),
    ("My mom always asks me why I can't be more like you. "),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You listen to the coolest music. "),
    ("Your every thought and motion contributes to the beauty of the universe. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("If we were playing kickball, I'd pick you first."),
    ("You're cooler than ice on the rocks."),
    ("You're the bee's knees. "),
    ("There isn't a thing about you that I don't like."),
    ("You have good taste."),
    ("I named all my appliances after you."),
    ("Your mind is a maze of amazing!"),
    ("Don't worry about procrastinating on your studies, I know you'll do great!"),
    ("I like your style!"),
    ("Hi, I'd like to know why you're so beautiful."),
    ("If I could count the seconds I think about you, I will die in the process!"),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("If you broke your arm, I would carry your books for you. "),
    ("I love the way your eyes crinkle at the corners when you smile."),
    ("You make me want to be the person I am capable of being."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("You are the rare catalyst to my volatile compound."),
    ("You're a tall glass of water!"),
    ("I'd like to kiss you. Often."),
    ("You are the wind beneath my wings."),
    ("Looking at you makes my foot cramps go away instantaneously."),
    ("I like your face."),
    ("You are a champ!"),
    ("You are infatuating."),
    ("Even my cat likes you. "),
    ("You're so cool, that on a scale of from 1-2, you're elevendyseven."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You have the best laugh ever."),
    ("I love you more than a drunk college student loves tacos."),
    ("My camera isn't worthy to take your picture."),
    ("You are the sugar on my rice krispies."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("I could hang out with you for a solid year and never get tired of you."),
    ("You're real happening in a far out way."),
    ("I bet you could take a punch from Mike Tyson."),
    ("Can you teach me how to be as awesome as you?"),
    ("Don't worry about anything in life. You'll do great."),
    ("I enjoy you more than a good sneeze. A GOOD one."),
    ("You could invent words and people would use them."),
    ("You have powerful sweaters."),
    ("If you were around, I would enjoy doing my taxes."),
    ("You look like you like to rock."),
    ("You are better than unicorns and sparkles combined!"),
    ("You are the watermelon in my fruit salad. Yum!"),
    ("I dig you."),
    ("You look better whether the lights are on or off."),
    ("I bet even your farts smell good."),
    ("I would trust my children with you."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("Your smile makes me smile."),
    ("I'd wake up for an  a.m. class just so I could sit next to you."),
    ("You have the moves like Jagger."),
    ("You're so hot that you denature my proteins."),
    ("All I want for Christmas is you!"),
    ("You are the world's greatest hugger."),
    ("You have a perfectly symmetrical face."),
    ("If you were in a movie you wouldn't get killed off."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("I Love you!"),
    ("They should name an ice cream flavor after you."),
    ("You're the salsa to my tortilla chips. You spice up my life!"),
    ("You smell nice."),
    ("You don't need make-up, make-up needs you."),
    ("Me without you is like a nerd without braces, a shoe with out laces, asentencewithoutspaces."),
    ("Just knowing someone as cool as you will read this makes me smile."),
    ("I would volunteer to take your place in the Hunger Games."),
    ("If I had a nickel for everytime you did something stupid, I'd be broke!"),
    ("I'd trust you to perform open heart surgery on me... blindfolded!"),
    ("Nice butt! - According to your toilet seat"),
    ("Perfume strives to smell like you."),
    ("I've had the time of my life, and I owe it all to you!"),
    ("The Force is strong with you."),
    ("I like the way your nostrils are placed on your nose."),
    ("I would hold the elevator doors open for you if they were closing."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You make me want to frolic in a field."),

    ("Your smile is contagious."),
    ("You look great today."),
    ("You're a smart cookie."),
    ("I bet you make babies smile."),
    ("You have impeccable manners."),
    ("I like your style."),
    ("You have the best laugh."),
    ("I appreciate you."),
    ("You are the most perfect you there is."),
    ("You are enough."),
    ("You're strong."),
    ("Your perspective is refreshing."),
    ("You're an awesome friend."),
    ("You light up the room."),
    ("You deserve a hug right now."),
    ("You should be proud of yourself."),
    ("You're more helpful than you realize."),
    ("You have a great sense of humor."),
    ("You've got all the right moves!"),
    ('Is that your picture next to "charming" in the dictionary?'),
    ("Your kindness is a balm to all who encounter it."),
    ("You're all that and a super-size bag of chips."),
    ("On a scale from 1 to 10, you're an 11."),
    ("You are brave."),
    ("You're even more beautiful on the inside than you are on the outside."),
    ("You have the courage of your convictions."),
    ("Your eyes are breathtaking."),
    ("If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now."),
    ("You are making a difference."),
    ("You're like sunshine on a rainy day."),
    ("You bring out the best in other people."),
    ("Your ability to recall random factoids at just the right time is impressive."),
    ("You're a great listener."),
    ("How is it that you always look great, even in sweatpants?"),
    ("Everything would be better if more people were like you!"),
    ("I bet you sweat glitter."),
    ("You were cool way before hipsters were cool."),
    ("That color is perfect on you."),
    ("Hanging out with you is always a blast."),
    ("You always know -- and say -- exactly what I need to hear when I need to hear it."),
    ("You smell really good."),
    ("You may dance like no one's watching, but everyone's watching because you're an amazing dancer!"),
    ("Being around you makes everything better!"),
    ('When you say, "I meant to do that," I totally believe you.'),
    ("When you're not afraid to be yourself is when you're most incredible."),
    ("Colors seem brighter when you're around."),
    ("You're more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)"),
    ("That thing you don't like about yourself is what makes you so interesting."),
    ("You're wonderful."),
    ("You have cute elbows. For reals! (You're halfway through the list. Don't stop now! You should be giving at least one awesome compliment every day!)"),
    ("Jokes are funnier when you tell them."),
    ("You're better than a triple-scoop ice cream cone. With sprinkles."),
    ("Your hair looks stunning."),
    ("You're one of a kind!"),
    ("You're inspiring."),
    ("If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener."),
    ("You should be thanked more often. So thank you!!"),
    ("Our community is better because you're in it."),
    ("Someone is getting through something hard right now because you've got their back."),
    ("You have the best ideas."),
    ("You always know how to find that silver lining."),
    ("Everyone gets knocked down sometimes, but you always get back up and keep going."),
    ("You're a candle in the darkness."),
    ("You're a great example to others."),
    ("Being around you is like being on a happy little vacation."),
    ("You always know just what to say."),
    ("You're always learning new things and trying to better yourself, which is awesome."),
    ("If someone based an Internet meme on you, it would have impeccable grammar."),
    ("You could survive a Zombie apocalypse."),
    ("You're more fun than bubble wrap."),
    ("When you make a mistake, you fix it."),
    ("Who raised you? They deserve a medal for a job well done."),
    ("You're great at figuring stuff out."),
    ("Your voice is magnificent."),
    ("The people you love are lucky to have you in their lives."),
    ("You're like a breath of fresh air."),
    ("You're gorgeous -- and that's the least interesting thing about you, too."),
    ("You're so thoughtful."),
    ("Your creative potential seems limitless."),
    ("Your name suits you to a T."),
    ("You're irresistible when you blush."),
    ("Actions speak louder than words, and yours tell an incredible story."),
    ("Somehow you make time stop and fly at the same time."),
    ("When you make up your mind about something, nothing stands in your way."),
    ("You seem to really know who you are."),
    ("Any team would be lucky to have you on it."),
    ('In high school I bet you were voted "most likely to keep being awesome."'),
    ("I bet you do the crossword puzzle in ink."),
    ("Babies and small animals probably love you."),
    ("If you were a scented candle they'd call it Perfectly Imperfect (and it would smell like summer)."),
    ("There's ordinary, and then there's you."),
    ("You're someone's reason to smile."),
    ("You're even better than a unicorn, because you're real."),
    ("How do you keep being so funny and making everyone laugh?"),
    ("You have a good head on your shoulders."),
    ("Has anyone ever told you that you have great posture?"),
    ("The way you treasure your loved ones is incredible."),
    ("You're really something special."),
    ("You're a gift to those around you.")
]

#rekt list
rektlist = [
    ("☑ Rekt"),
    ("☑ Tyrannosaurus Rekt"),
    ("☑ sudo apt-get Rekt"),
    ("☑ e=mRekt²"),
    ("☑ Rekt and Morty"),
    ("☑ Really Rekt"),
    ("☑ Cash4Rekt.com"),
    ("☑ Grapes of Rekt"),
    ("☑ Ship Rekt"),
    ("☑ Rektavoir Dogs"),
    ("☑ Raiders of the Rekt Ark _("),
    ("☑ Indiana Jones and the Temple of Rekt"),
    ("☑ Rekt markes the spot"),
    ("☑ Caught rekt handed"),
    ("☑ The Rekt Side Story"),
    ("☑ Singin' In The Rekt"),
    ("☑ Painting The Roses Rekt"),
    ("☑ Rekt Van Winkle"),
    ("☑ Parks and Rekt"),
    ("☑ Lord of the Rekts: The Reking of the King"),
    ("☑ Star Trekt"),
    ("☑ The Rekt Prince of Bel-Air"),
    ("☑ A Game of Rekt"),
    ("☑ Rektflix"),
    ("☑ Rekt it like it's hot"),
    ("☑ RektBox 360"),
    ("☑ The Rekt-men"),
    ("☑ School Of Rekt"),
    ("☑ I am Fire, I am Rekt"),
    ("☑ Rekt and Roll"),
    ("☑ Professor Rekt"),
    ("☑ Catcher in the Rekt"),
    ("☑ Rekt-22"),
    ("☑ Harry Potter: The Half-Rekt Prince"),
    ("☑ Great Rektspectations"),
    ("☑ Paper Scissors Rekt"),
    ("☑ RektCraft"),
    ("☑ Grand Rekt Auto V"),
    ("☑ Call of Rekt: Modern Reking 2"),
    ("☑ Legend Of Zelda: Ocarina of Rekt"),
    ("☑ Rekt It Ralph"),
    ("☑ Left 4 Rekt"),
    ("☑ www.rekkit.com"),
    ("☑ Pokemon: Fire Rekt"),
    ("☑ The Shawshank Rektemption"),
    ("☑ The Rektfather"),
    ("☑ The Rekt Knight"),
    ("☑ Fiddler on the Rekt"),
    ("☑ The Rekt Files"),
    ("☑ The Good, the Bad, and The Rekt"),
    ("☑ Forrekt Gump"),
    ("☑ The Silence of the Rekts"),
    ("☑ The Green Rekt"),
    ("☑ Gladirekt"),
    ("☑ Spirekted Away"),
    ("☑ Terminator 2: Rektment Day"),
    ("☑ The Rekt Knight Rises"),
    ("☑ The Rekt King"),
    ("☑ REKT-E"),
    ("☑ Citizen Rekt"),
    ("☑ Requiem for a Rekt"),
    ("☑ REKT TO REKT ass to ass"),
    ("☑ Star Wars: Episode VI - Return of the Rekt"),
    ("☑ Braverekt"),
    ("☑ Batrekt Begins"),
    ("☑ 2001: A Rekt Odyssey"),
    ("☑ The Wolf of Rekt Street"),
    ("☑ Rekt's Labyrinth"),
    ("☑ 12 Years a Rekt"),
    ("☑ Gravirekt"),
    ("☑ Finding Rekt"),
    ("☑ The Arekters"),
    ("☑ There Will Be Rekt"),
    ("☑ Christopher Rektellston"),
    ("☑ Hachi: A Rekt Tale"),
    ("☑ The Rekt Ultimatum"),
    ("☑ Shrekt"),
    ("☑ Rektal Exam"),
    ("☑ Rektium for a Dream"),
    ("☑ www.Trekt.tv"),
    ("☑ Erektile Dysfunction"),
    ("☑ Jesus, stepping out the grave: 'Get ressurekt'"),
]

simpwords = [
    ("Are you a bank loan? Because you have my interest!"),
    ("I just saw the best upsexy ever."),
    ("Does this mean we're married now?"),
    ("If you were a triangle, you'd be acute one!"),
    ("What's a smart, attractive man like myself doing without your phone number?"),
    ("Are you a good cuddler? I might let you join my gang."),
    ("Sorry it took me so long to message, I was at Whole Foods trying to figure out what you like for breakfast."),
    ("I like your style."),
    ("On a scale of 1 to 10, you’re a 9 and I’m the 1 you lack."),
    ("Do you like Harry Potter? Because I adumbledore you."),
    ("Did I tell you I'm writing a book? It's a phone book and it's missing your number."),
    ("My mom told me not to talk to strangers online, but I’ll make an exception for you."),
    ("Your phone has GPS, right? Because I’m totally going to get lost in those  eyes."),
    (" :sunflower: :white_flower: :wilted_rose:  Here, I brought you flowers."),
    ("Roses are red. Violets are fine. You be the 6. I'll be the 9."),
    ("Is there an airport nearby; or is that just my heart taking off?"),
    ("Hi I’m Mr Right, somebody said you were looking for me?"),
    ("Do you have a map? I keep getting lost in your eyes."),
    ("Am I dead? Because I think I just met an angel.."),
    ("Nice legs, what time do they open? :flushed: "),
    ("Did it hurt when you fell out of heaven?"),
    ("I’ve lost that loving feeling, will you help me find it again?"),
    ("Hi the voices in my head told me to come talk to you."),
    ("There must be something wrong with my phone, because it doesn’t have your number in it."),
    ("Is your father a thief? Because someone stole the stars from the sky and put them in your eyes"),
    ("You must be tired, because you’ve been running through my mind all night!"),
    ("I wish I was your mirror."),
    ("Are you a parking ticket? Because you have fine written all over you!"),
    ("You know, I’m not really this tall. I’m just sitting on my wallet")
]
################
@client.command()
async def simp( ctx, user1 : discord.Member):
    async with ctx.channel.typing():

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        message = random.choice(simpwords)

        embed = discord.Embed(
                colour=discord.Colour.blurple()
                )
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name + ', make sure you appreciate them!')
        embed.add_field(name= user1.name , value= message , inline=False)
        await ctx.send(embed=embed)
        return
    return

###############


@client.command()
async def hug( ctx, user1 : discord.Member):
        async with ctx.channel.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            message = random.choice(compliments)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name + ', make sure you appreciate them!')
            embed.add_field(name= user1.name , value= message , inline=False)
            await ctx.send(embed=embed)
            return
        return
@client.command()
async def flip(ctx):
        x = await ctx.send(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await asyncio.sleep(1)
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await asyncio.sleep(1)
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(0.5)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await asyncio.sleep(1)
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await asyncio.sleep(1)
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
        await asyncio.sleep(1)
        await x.edit(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(0.2)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')




@client.command()
async def rekt( ctx, user1 : discord.Member):
    async with ctx.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            not_rekt = "⬜ Not Rekt"

            output = ['rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' , 'notrekt']
            random_output = choice(output)

            rekt_message = choice(rektlist)

            if random_output == 'notrekt':
                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.add_field(name= user1.name , value= not_rekt , inline=False)
                await ctx.send(embed=embed)
                return

            if random_output == 'rekt':
                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='You got served by: ' + author.name)
                embed.add_field(name= user1.name , value= rekt_message , inline=False)
                await ctx.send(embed=embed)
                return
    return





















client.run('كسمك go get a life')
while True:
    print("died")
    time.sleep(1)
    print("\n" * 50)
    print("died.")
    time.sleep(1)
    print("\n" * 50)
    print("died..")
    time.sleep(1)
    print("\n" * 50)
    print("died...")
    time.sleep(1)
    print("\n" * 50)
    print("died..")
    time.sleep(1)
    print("\n" * 50)
    print("died.")
    time.sleep(1)
    print("\n" * 50)




