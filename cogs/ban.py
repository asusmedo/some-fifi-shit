import discord
import asyncio
import re
from discord.ext import commands
import sys
import traceback


time_regex = re.compile("(?:(\d{1,5})(h|s|m|d)).?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, time:TimeConverter = None,reason=None):

        banned_users = await ctx.guild.bans()
        
        
        await member.ban(reason=reason)
        await ctx.send(("**Banned {} for {}s** " if time else "**Banned {}, Bye Bye** ").format(member.mention, time))
        await member.send(("**Banned {} for {}s** " if time else "**Banned {}, Bye Bye** ").format(member.mention, time))
        for ban_entry in banned_users:
            user = ban_entry.user
        if time:
            member_name, member_discriminator = member.split('#')
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await asyncio.sleep(time)
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


    @ban.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            pass
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
        else:
            error = getattr(error, 'original', error)
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


def setup(bot):
    bot.add_cog(ban(bot))