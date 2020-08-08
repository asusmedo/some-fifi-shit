import discord
from discord.ext  import commands

class  av(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def av(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        show_avatar = discord.Embed(

            colour = discord.Color.dark_blue()

        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)

def setup(bot):
    bot.add_cog(av(bot))