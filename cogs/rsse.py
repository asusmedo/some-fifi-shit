import discord
from discord.ext  import commands
import time
from discord.utils import get
import asyncio


class  help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





@commands.command(pass_context=True)
async def emoji(self , bot , ctx):
    msg = await bot.say("working")
    reactions = ['dart']
    for emoji in reactions: 
        await bot.add_reaction(msg, emoji)

def setup(bot):
    bot.add_cog(help(bot))
