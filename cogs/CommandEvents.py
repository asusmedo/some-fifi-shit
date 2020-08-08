import discord
from discord.ext  import commands
import asyncio
import random
import random2

class  CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} Wellcome, Come Take A Cup Of Tea !')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member}You Left , We Stay.')





def setup(bot):
    bot.add_cog(CommandEvents(bot))