import discord
from discord.ext  import commands

class  clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def clear(self, ctx, amount=5):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
            await ctx.channel.purge(limit=amount + 1)
            



def setup(bot):
    bot.add_cog(clear(bot))