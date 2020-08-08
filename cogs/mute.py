import discord
import asyncio
import re
from discord.ext import commands
import sys
import traceback


time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
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

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member:discord.Member, *, time:TimeConverter = None,reason='عارف ليه؟ عشان انت واد بضان'):
        """Mutes a member for the specified time- time in 2d 10h 3m 2s format ex:
        &mute @Someone 1d"""
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(("**   اتعملك ميوت يا روح امك {} for {}s {}, خف علوقيه بقى ** (Muted)" if time else "**Muted يا علق {}** ").format( member.mention, time , reason))
        if time:
            await asyncio.sleep(time)
            await member.remove_roles(role)
            await ctx.send("** {} unmuted  , Stop being 3el2 please **".format(member.mention))

    @mute.error
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
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                await ctx.send("** {} unmuted  , Stop being 3el2 please ** " .format(member.mention))
                return


def setup(bot):
    bot.add_cog(mute(bot))