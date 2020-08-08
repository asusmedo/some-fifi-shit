from datetime import datetime, timedelta

from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions
import discord
from discord.ext  import commands
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from glob import glob


COGS = [path.split("\\")[-1][:-3] for path in glob("/cogs/*.py")]
# Here are all the number emotes.
# 0⃣ 1️⃣ 2⃣ 3⃣ 4⃣ 5⃣ 6⃣ 7⃣ 8⃣ 9⃣

numbers = ('\U0001f1e6', '\U0001f1e7', '\U0001f1e8', '\U0001f1e9', '\U0001f1ea',
		   '\U0001f1eb', '\U0001f1ec', '\U0001f1ed', '\U0001f1ee', '\U0001f1ef')





class Reactions(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.polls = []

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.colours = {
				"❤️": self.bot.guild.get_role(653940117680947232), # Red
				"💛": self.bot.guild.get_role(653940192780222515), # Yellow
				"💚": self.bot.guild.get_role(653940254293622794), # Green
				"💙": self.bot.guild.get_role(653940277761015809), # Blue
				"💜": self.bot.guild.get_role(653940305300815882), # Purple
				"🖤": self.bot.guild.get_role(653940328453373952), # Black
			}
			self.reaction_message = await self.bot.get_channel(723257328819896390).fetch_message(723258202090635285)
			self.starboard_channel = self.bot.get_channel(724367069004693591)
			self.bot.cogs_ready.ready_up("reactions")

	@command(name="createpoll", aliases=["mkpoll","poll"])
	@has_permissions(manage_guild=True)
	async def create_poll(self, ctx,  question: str, *options ):
		await ctx.message.delete()
		async with ctx.typing():
				
			if len(options) > 10:
				await ctx.send("You can only supply a maximum of 10 options.")
		
			else:
				embed = Embed(title= None ,
							description=None,
							colour=ctx.author.colour,
							
							timestamp=datetime.utcnow())

				fields = [( question , "\n\u200b".join([f"{numbers[idx]} {option}  \n\u200b \n\u200b" for idx, option in enumerate(options)]), False),
						("    ", "Vote ya 2lpi :heart:   "+"\u200B   "+" \u200B" +"          -- Fifi Poll V0.69 --                                                                    ", False)]
				
				for name, value, inline in fields:
					embed.add_field(name=name + "\n\u200b", value=value, inline=inline)

				message = await ctx.send(embed=embed)

				for emoji in numbers[:len(options)]:
					await message.add_reaction(emoji)

				self.polls.append((message.channel.id, message.id))

		

	

def setup(bot):
	bot.add_cog(Reactions(bot))