from discord import Embed, FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
import asyncio
from youtube_dl import YoutubeDL
from asyncio import run_coroutine_threadsafe
import requests
import math

import discord
from discord.ext import commands
import ytdl
from asyncio import sleep
import voice



class Musicsound(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        """Returns or creates voice.VoiceState for the guild defined in the passed ctx"""
        state = self.voice_states.get(ctx.guild.id)
        if not state or not state.exists:
            state = voice.VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        """Unloads the music cog"""
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        """Prevent calling commands in DM's"""
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        #Set voice state for every command
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            print(f"{message.guild}/{message.channel}/{message.author.name}>{message.content}")
            if message.embeds:
                print(message.embeds[0].to_dict())

    @commands.command(name='fifi',aliases=['join'] ,invoke_without_subcommand=True)
    async def _fifi(self, ctx: commands.Context):
        """Joins a voice channel."""
        author = ctx.message.author
        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return
        await ctx.message.delete()
        ctx.voice_state.voice = await destination.connect()
        x= await ctx.send(content=f" {author.mention} أنا دخــــلت اهو ، ءأمرني يا قلبي")
        await asyncio.sleep(1)
        await x.edit(content=":heart:")
        await asyncio.sleep(0.5)
        await x.edit(content="ءأمرني يا قلبي")
        await asyncio.sleep(0.5)
        await x.edit(content=" :heart: ءأمرني يا قلبي ")

    @commands.command(name='summon',aliases=['summons'])
    @commands.has_permissions(manage_guild=True)
    async def _summons(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise voice.VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()
        await ctx.send(f"أنا دخــــلت اهو ، ءأمرني يا قلبي")

    @commands.command(name='leaves', aliases=['disconnect'])
    async def _leaves(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
        await ctx.send (f"Bye Bye :heart: ")

    @commands.command(name='byes')
    async def _byes(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
        await ctx.send (f"Bye Bye :heart: ")

    @commands.command(name='fuckoffsound')
 
    async def _fuckoffsound(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
        await ctx.send (f"Bye Bye :heart: ")

    @commands.command(name='volume')
    @commands.is_owner()
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['currents', 'playings','nps', 'nowplayings'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""
        embed = ctx.voice_state.current.create_embed()
        await ctx.send(embed=embed)

    

    @commands.command(aliases=['pauses'])
    @commands.has_permissions(manage_guild=True)
    async def _pausesound(self, ctx: commands.Context):
        """Pauses the currently playing song."""
        print(">>>Pause Command:")
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command( aliases=['resumes'])
    @commands.has_permissions(manage_guild=True)
    async def _resumesound(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(aliases=['stops','stopsound'])
    @commands.has_permissions(manage_guild=True)
    async def _stopsound(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if ctx.voice_state.autoplay:
            ctx.voice_state.autoplay = False
            

            
        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')
       
    @commands.command(name='autoplay')
    async def _autoplay(self, ctx: commands.Context):
        """Automatically queue a new song that is related to the song at the end of the queue.
        Invoke this command again to toggle autoplay the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.autoplay = not ctx.voice_state.autoplay
        await ctx.message.add_reaction('✅')
        await ctx.send('Autoplay after end of queue is now ' + ('on' if ctx.voice_state.autoplay else 'off') + ' Ya 2lpi :heart:' )

    @commands.command(aliases=['ss' ,'skipsound'])
    async def _skipsound(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('مفيش حاجه شغاله يا قلبي ')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 1:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command( aliases=['qs','queues'])
    async def _queuesound(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='history')
    async def _history(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's history.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.song_history) == 0:
            return await ctx.send('Empty history.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.song_history) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.song_history[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.song_history), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue. :heart: ')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(aliases=['removesound','rs'])
    async def _removes(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue. :heart: ')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(aliases=['ls','loopsound'])
    async def _loopsound(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('مفيش حاجه شغاله يا قلبي ')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')
        await ctx.send('Looping is now ' + ('on' if ctx.voice_state.loop else 'off') + ' Ya 2lpi :heart: ')

    

    @commands.command(aliases=['ps','plays'])
    async def _playsound(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        async with ctx.typing():
            try:
                source = await ytdl.YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except ytdl.YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                if not ctx.voice_state.voice:
                    await ctx.invoke(self._fifi)

            song = voice.Song(source)
            await ctx.voice_state.songs.put(song)
            await ctx.send('Done ya 7abibi - Enqueued :heart:  {}'.format(str(source)))

    @commands.command(name='search')
    async def _search(self, ctx: commands.Context, *, search: str):
        """Searches youtube.
        It returns an imbed of the first 10 results collected from youtube.
        Then the user can choose one of the titles by typing a number
        in chat or they can cancel by typing "cancel" in chat.
        Each title in the list can be clicked as a link.
        """
        async with ctx.typing():
            try:
                source = await ytdl.YTDLSource.search_source(self.bot, ctx, search, loop=self.bot.loop)
            except ytdl.YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                if source == 'sel_invalid':
                    await ctx.send('Invalid selection')
                elif source == 'cancel':
                    await ctx.send(':white_check_mark:')
                elif source == 'timeout':
                    await ctx.send(':alarm_clock: **Time\'s up bud**')
                else:
                    if not ctx.voice_state.voice:
                        await ctx.invoke(self._fifi)

                song = voice.Song(source)
                await ctx.voice_state.songs.put(song)
                await ctx.send('Done ya 7abibi - Enqueued :heart:  {}'.format(str(source)))
            
    @_fifi.before_invoke
    @_playsound.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

def setup(bot):
    bot.add_cog(Musicsound(bot))
   