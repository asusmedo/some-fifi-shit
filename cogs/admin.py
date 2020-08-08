import discord
import importlib
import os
import logging
import discord
import asyncio
import re
from discord.ext import commands
import sys
import traceback

from discord.ext import commands
import checks

log = logging.getLogger(__name__)


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @checks.is_admin()
    @commands.command()
    async def load(self, ctx, name: str):
        """Loads an extension."""
        try:
            self.bot.load_extension(f'cogs.{name}')
        except Exception as e:
            log.error(f'{name} couldn\'t be loaded.\n{e}')
        await ctx.send(f'Loaded extension **{name}.py**')

    @checks.is_admin()
    @commands.command()
    async def unload(self, ctx, name: str):
        """Unloads an extension."""
        try:
            self.bot.unload_extension(f'cogs.{name}')
        except Exception as e:
            log.error(f'{name} couldn\'t be unloaded.\n{e}')
        await ctx.send(f'Unloaded extension **{name}.py**')

    @checks.is_admin()
    @commands.command()
    async def reload(self, ctx, name: str):
        """Reloads an extension."""
        try:
            self.bot.reload_extension(f'cogs.{name}')
        except Exception as e:
            log.error(f'{name} couldn\'t be reloaded.\n{e}')
        await ctx.send(f'Reloaded extension **{name}.py**')
        await ctx.message.add_reaction('✅')

    @checks.is_admin()
    @commands.command()
    async def reloadall(self, ctx):
        """Reloads all extensions."""
        error_collection = []
        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                name = file[:-3]
                try:
                    self.bot.reload_extension(f'cogs.{name}')
                except Exception as e:
                    log.error(f'{name} couldn\'t be loaded.\n{e}')

        if error_collection:
            output = '\n'.join([f'**{g[0]}** ```diff\n- {g[1]}```' for g in error_collection])
            return await ctx.message.add_reaction('❌')

        await ctx.message.add_reaction('✅')

    @checks.is_admin()
    @commands.command()
    async def reloadutils(self, ctx, name: str):
        """ Reloads a utils module. """
        name_maker = f'utils/{name}.py'
        try:
            module_name = importlib.import_module(f'utils.{name}')
            importlib.reload(module_name)
        except ModuleNotFoundError:
            return await ctx.send(f'Couldn\'t find module named **{name_maker}**')
        except Exception as e:
            return await ctx.send(f'Module **{name_maker}** returned error and was not reloaded...\n{e}')
        await ctx.send(f'Reloaded module **{name_maker}**')

    @checks.is_admin()
    @commands.command()
    async def dm(self, ctx, user_id: int , *, message: str):
        """ DM the user of your choice """
        user = self.bot.get_user(user_id)
        if not user:
            return await ctx.send(f'Could not find any UserID matching **{user_id}**')

        try:
            await user.send(message)
            await ctx.send(f'✉️ Sent a DM to **{user_id}**')
        except discord.Forbidden:
            await ctx.send('This user might be having DMs blocked or it\'s a bot account...')

    
   
            

    
    @commands.command(hidden=True, aliases=['cp'])
    @commands.has_permissions(administrator=True)
    async def change_playing(self, ctx, *, text=''""''):
        if text:
            text = text.lower()
            if text.startswith('listening to' ):
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text[13:]))
                await ctx.message.add_reaction('✅')
            elif text.startswith('watching'):
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text[9:]))
                await ctx.message.add_reaction('✅')
            elif text.startswith('watch'):
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text[6:]))
                await ctx.message.add_reaction('✅')
            elif text.startswith('lis'):
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text[4:]))
                await ctx.message.add_reaction('✅')
            elif text == 'online':
                await self.bot.change_presence(status='online')
                await ctx.message.add_reaction('✅')
            elif text == 'idle':
                await self.bot.change_presence(status='idle')
                await ctx.message.add_reaction('✅')
            elif text == 'dnd':
                await self.bot.change_presence(status='dnd')
                await ctx.message.add_reaction('✅')
            elif text.startswith('lidnd'):
                await self.bot.change_presence(status='dnd', activity=discord.Activity(type=discord.ActivityType.listening, name=text[6:]))
                await ctx.message.add_reaction('✅')
            elif text.startswith('wadnd'):
                await self.bot.change_presence(status='dnd', activity=discord.Activity(type=discord.ActivityType.watching, name=text[6:]))
                await ctx.message.add_reaction('✅')
            elif text.startswith('playdnd'):
                await self.bot.change_presence(status='dnd', activity=discord.Activity(type=discord.ActivityType.playing, name=text[8:]))
                await ctx.message.add_reaction('✅')
            else:
                await self.bot.change_presence(activity=discord.Game(name=text))
                await ctx.message.add_reaction('✅')
        else:
            await self.bot.change_presence(activity=None, status='online')
            await ctx.message.add_reaction('✅')


    

def setup(bot):
    bot.add_cog(Admin(bot))