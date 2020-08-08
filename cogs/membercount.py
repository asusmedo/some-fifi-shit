from typing import List
import discord
from discord.ext import commands
import operator
import utils
import traceback



class MemberCount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        

    @commands.command(aliases=['members','mc'])
    async def membercount(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(
            color=ctx.author.color
        ).set_author(
            name=ctx.guild.name,
            icon_url=str(ctx.guild.icon_url)
        ).add_field(
            name='Total',
            value=format(len(ctx.guild.members), ',d'),
            inline=False
        ).add_field(
            name='Humans',
            value=format(len([m for m in ctx.guild.members if not m.bot]), ',d'),
            inline=False
        ).add_field(
            name='Bots',
            value=format(len([m for m in ctx.guild.members if m.bot]), ',d'),
            inline=False
        ))

    @commands.command(aliases=['femalescount'])
    async def fc(self, ctx):
        guild = ctx.guild
        specific_role = discord.utils.get(guild.roles, name="Female")
        global member_count
        member_count = specific_role.members
        Female = str(len(member_count))

        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(
            color=ctx.author.color
        ).set_author(
            name=ctx.guild.name,
            icon_url=str(ctx.guild.icon_url)
        ).add_field(
            name='Females',
            value=Female,
            inline=False
        ))

def setup(bot: commands.Bot):
    bot.add_cog(MemberCount(bot))