import discord
from discord.ext  import commands

class  error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
             print("You Don't Have permission To Do That!")
        raise error



def setup(bot):
    bot.add_cog(error(bot))