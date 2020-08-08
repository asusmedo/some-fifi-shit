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

class Commands(commands.Cog):
	def __init__(self, bot):
		super().__init__(bot)
            self.bot = bot
		self.cursor = bot.mysql.cursor
		self.escape = bot.escape

	@commands.group(pass_context=True, aliases=['setprefix', 'changeprefix'], invoke_without_command=True, no_pm=True)
	@checks.admin_or_perm(manage_server=True)
	async def prefix(self, ctx, *, txt:str=None):
		"""Change the Bots Prefix for the Server"""
		if txt is None:
			sql = "SELECT prefix FROM `prefix` WHERE server={0}"
			sql = sql.format(ctx.message.server.id)
			sql_channel = "SELECT prefix FROM `prefix_channel` WHERE server={0} AND channel={1}"
			sql_channel = sql_channel.format(ctx.message.server.id, ctx.message.channel.id)
			result = self.cursor.execute(sql).fetchall()
			result2 = self.cursor.execute(sql_channel).fetchall()
			if len(result) == 0:
				server_prefix = '.'
			else:
				server_prefix = result[0]['prefix']
			if len(result2) == 0:
				channel_prefix = None
			else:
				channel_prefix = result2[0]['prefix']
			msg = "Server Prefix: `{0}`\n".format(server_prefix)
			if channel_prefix != None:
				msg += "**Current** Channel Prefix: `{0}`".format(channel_prefix)
			await self.bot.say(msg)
			return
		sql = "INSERT INTO `prefix` (`server`, `prefix`, `id`) VALUES (%s, %s, %s)"
		update_sql = "UPDATE `prefix` SET prefix={0} WHERE server={1}"
		update_sql = update_sql.format(self.escape(txt), ctx.message.server.id)
		check = "SELECT server FROM `prefix` WHERE server={0}"
		check = check.format(ctx.message.server.id)
		result = self.cursor.execute(check).fetchall()
		if len(result) == 0:
			self.cursor.execute(sql, (ctx.message.server.id, txt, ctx.message.author.id))
			self.cursor.commit()
			await self.bot.say(":white_check_mark: Set bot prefix to \"{0}\" for the server\n".format(txt))
		else:
			self.cursor.execute(update_sql)
			self.cursor.commit()
			await self.bot.say(":white_check_mark: Updated bot prefix to \"{0}\" for the server".format(txt))

	@prefix.command(pass_context=True, name='channel', no_pm=True)
	@checks.admin_or_perm(manage_server=True)
	async def _prefix_channel(self, ctx, *, txt:str):
		"""Change the Bots Prefix for the current Channel"""
		channel = ctx.message.channel
		for c in ctx.message.channel_mentions:
			channel = c
			txt = txt.replace(channel.mention, '').replace('#'+channel.name, '')
		sql = "INSERT INTO `prefix_channel` (`server`, `prefix`, `channel`, `id`) VALUES (%s, %s, %s, %s)"
		update_sql = "UPDATE `prefix_channel` SET prefix={0} WHERE server={1} AND channel={2}"
		update_sql = update_sql.format(self.escape(txt), ctx.message.server.id, channel.id)
		check = "SELECT * FROM `prefix_channel` WHERE server={0} AND channel={1}"
		check = check.format(ctx.message.server.id, channel.id)
		result = self.cursor.execute(check).fetchall()
		if len(result) == 0:
			self.cursor.execute(sql, (ctx.message.server.id, txt, channel.id, ctx.message.author.id))
			self.cursor.commit()
			await self.bot.say(":white_check_mark: Set bot prefix to \"{0}\" for {1}".format(txt, channel.mention))
		else:
			self.cursor.execute(update_sql)
			self.cursor.commit()
			await self.bot.say(":white_check_mark: Updated bot prefix to \"{0}\" for {1}".format(txt, channel.mention))

	@prefix.command(pass_context=True, name='reset', no_pm=True)
	@checks.admin_or_perm(manage_server=True)
	async def _prefix_reset(self, ctx, what:str=None, channel:discord.Channel=None):
		"""Reset All Custom Set Prefixes For the Bot"""
		if what is None or what == "server":
			sql = "DELETE FROM `prefix` WHERE server={0}"
			sql = sql.format(ctx.message.server.id)
			check = "SELECT * FROM `prefix` WHERE server={0}"
			check = check.format(ctx.message.server.id)
			result = self.cursor.execute(check).fetchall()
			if len(result) == 0:
				await self.bot.say(":no_entry: Current server does **not** have a custom prefix set!")
				return
			else:
				self.cursor.execute(sql)
				self.cursor.commit()
				await self.bot.say(":exclamation: **Reset server prefix**\nThis does not reset channel prefixes, run \"all\" after reset to reset all prefixes *or* \"channels\" to reset all custom channel prefixes.")
		elif what == "channel":
			if channel is None:
				channel = ctx.message.channel
			sql = "DELETE FROM `prefix_channel` WHERE server={0} AND channel={1}"
			sql = sql.format(ctx.message.server.id, channel.id)
			check = "SELECT * FROM `prefix_channel` WHERE server={0} AND channel={1}"
			check = check.format(ctx.message.server.id, channel.id)
			result = self.cursor.execute(check).fetchall()
			if len(result) == 0:
				await self.bot.say(":no_entry: {0} does **not** have a custom prefix Set!\nMention the channel after \"reset channel\" for a specific channel.".format(channel.mention))
				return
			else:
				self.cursor.execute(sql)
				self.cursor.commit()
				await self.bot.say(":exclamation: Reset {0}'s prefix!\nThis does **not** reset all custom channel prefixes, \"reset channels\" to do so.".format(channel.mention))
				return
		elif what == "channels":
			sql = "DELETE FROM `prefix_channel` WHERE server={0}"
			sql = sql.format(ctx.message.server.id)
			check = "SELECT * FROM `prefix_channel` WHERE server={0}"
			check = check.format(ctx.message.server.id)
			result = self.cursor.execute(check).fetchall()
			if len(result) == 0:
				await self.bot.say(":no_entry: Server does **not** reset a custom prefix set for any channel!\nMention the channel after \"reset channel\" for a specific channel.")
				return
			else:
				self.cursor.execute(sql)
				self.cursor.commit()
				await self.bot.say(":exclamation: Reset all channels custom prefixes!")
				return
		elif what == "all" or what == "everything":
			sql = "DELETE FROM `prefix_channel` WHERE server={0}"
			sql = sql.format(ctx.message.server.id)
			sql2 = "DELETE FROM `prefix` WHERE server={0}"
			sql2 = sql2.format(ctx.message.server.id)
			self.cursor.execute(sql)
			self.cursor.execute(sql2)
			self.cursor.commit()
			await self.bot.say(":warning: Reset all custom server prefix settings!")
			return
		else:
			await self.bot.say(":no_entry: Invalid Option\nOptions: `server, channel, channels, all/everything`")

	
def setup(bot):
	bot.add_cog(Commands(bot))