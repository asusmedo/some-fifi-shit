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

class  warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(pass_context=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            await ctx.send("you must enter a reason to warn")
        else:
            try:
                if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                    message = f"You have been warned from `` {ctx.guild.name} ``  by `` {ctx.message.author} `` for `` {reason} ``"
                    embed = discord.Embed(
                        colour=discord.Color.red()
                    )
                    embed.add_field(name="WARNED",
                                    value=f'You have been warned from `` {ctx.guild.name} ``  by `` {ctx.message.author} `` for `` {reason} ``',
                                    inline=False)
                    await member.send(embed=embed)
                    embed = discord.Embed(title="User was warned for {}".format(reason),
                                        description="**{}** has been warned!".format(member),
                                        color=discord.Color.green())
                    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Permission Denied.",
                                        description="You don't have permission to use this command.",
                                        color=discord.Color.red())
                    await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Permission Denied.",
                                    description="Bot doesn't have correct permissions, or bot can't ban this user.",
                                    color=discord.Color.red())
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(warn(bot))