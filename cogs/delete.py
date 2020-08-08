import discord
from discord.ext  import commands

class  bad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener("on_message")
    async def swear_listener(self, message:discord.Message):
        """Looks for swearing in the message and tells people off"""

        if message.author.bot:
            return

        content = set(message.content.lower().strip().split())
        swears = {"niger","Niger","nigge-r", "Nigger", "Nigge-r", "nigger", "blacknigga", "blacknigger", "n-igger", "NIGG-ER", "nigg-er", "NIGG-ER", "niggerr", "niggeer"}
        if content.intersection(swears):
            await message.delete()
            

def setup(bot):
    bot.add_cog(bad(bot))
   
   
   
   



















   