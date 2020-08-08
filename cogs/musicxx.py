from discord import Embed, FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
import asyncio
from youtube_dl import YoutubeDL
from asyncio import run_coroutine_threadsafe
import requests
import math
import lyricsgenius
import discord
from discord.ext import commands
import ytdl
from asyncio import sleep
import voice

genius = lyricsgenius.Genius("r_eahP4j5tNj34CGAI48kSVYCHyJ0YCCDG70kmmHrVnYElyuqjnULP0lk9tvxKlT")

sauce = ''

class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }
class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        global sauce
        embed = (discord.Embed(
            title='Now playing: {}'.format(self.source.title),
            color=discord.Color.from_rgb(97, 0, 215)
        )
                 .set_footer(text='Commands at .music')
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value=self.source.uploader)
                 .set_thumbnail(url=self.source.thumbnail))

        sauce = str(self.source.title)

        return embed

class Music(commands.Cog):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.song_queue = {}
        self.message = {}
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
        await print('An error occurred: {}'.format(str(error)))

    
    @staticmethod
    def parse_duration(duration):
        
        m, s = divmod(duration, 60)
        h, m = divmod(m, 60)
        return f'{h:d}:{m:02d}:{s:02d}'

    @staticmethod
    def search(author, arg):
        with YoutubeDL(Music.YDL_OPTIONS) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)

        embed = (Embed(description=f"[{info['title']}]({info['webpage_url']})", color=0x3498db)
                .add_field(name='Duration', value=Music.parse_duration(info['duration']))
                .add_field(name='Requested by', value=author)
                .add_field(name='Uploader', value=f"[{info['uploader']}]({info['channel_url']})")
                .set_thumbnail(url=info['thumbnail']))

        return {'embed': embed, 'source': info['formats'][0]['url'], 'title': info['title']}

    async def edit_message(self, ctx):
        embed = self.song_queue[ctx.guild][0]['embed']
        content = "\n".join([f"({self.song_queue[ctx.guild].index(i)}) {i['title']}" for i in self.song_queue[ctx.guild][1:]]) if len(self.song_queue[ctx.guild]) > 1 else "No song queued"
        embed.set_field_at(index=1, name="Fifi queue :", value=content, inline=False)
        await self.message[ctx.guild].edit(embed=embed)

    def play_next(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if len(self.song_queue[ctx.guild]) > 1:
            del self.song_queue[ctx.guild][0]
            run_coroutine_threadsafe(self.edit_message(ctx), self.bot.loop)
            voice.play(FFmpegPCMAudio(self.song_queue[ctx.guild][0]['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)
            run_coroutine_threadsafe(self.message[ctx.guild].delete(), self.bot.loop)

    


    @commands.command(aliases=['p'])
    async def play(self, ctx, *, video: str):
        async with ctx.typing():
            channel = ctx.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            song = Music.search(ctx.author.mention, video)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()     

            if not voice.is_playing():
                self.song_queue[ctx.guild] = [song]
                self.message[ctx.guild] = await ctx.send(embed=song['embed'])
                await ctx.message.delete()
                voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
                voice.is_playing()
            else:
                
                self.song_queue[ctx.guild].append(song)
                await ctx.message.delete()
                await self.edit_message(ctx)
    

    @commands.command(aliases=['resume'])
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            if voice.is_playing():
                await ctx.message.add_reaction('⏸️')
                voice.pause()
                
            else:
                await ctx.message.add_reaction('⏸️')
                voice.resume()

    @commands.command(aliases=['pass'], brief='!skip')
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            await ctx.message.add_reaction('⏭')
            voice.stop()

    @commands.command(brief='!remove')
    async def remove(self, ctx, *, num: int):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            del self.song_queue[ctx.guild][num]
            await self.edit_message(ctx)
            await ctx.message.add_reaction('✅')
    
    @commands.command(name='fuckoff', aliases=['bye','leave'])
 
    async def _fuckoff(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            if voice.is_playing():
                await ctx.message.add_reaction('👋')
                voice.stop()
                voice.disconnect()
                
         
    @commands.command(name='queue', aliases=['q','np','nowplay','playing','current'])
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        await ctx.message.delete()
        embed = self.song_queue[ctx.guild][0]['embed']
        content = "\n".join([f"({self.song_queue[ctx.guild].index(i)}) {i['title']}" for i in self.song_queue[ctx.guild][1:]]) if len(self.song_queue[ctx.guild]) > 1 else "No song queued"
        embed.set_field_at(index=1, name="Fifi queue :", value=content, inline=False)
        await ctx.send(embed=embed , delete_after=20.0)
    
    @commands.command(aliases=['ly'])
    async def lyrics(self, ctx: commands.Context, *, sauce):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            return await ctx.send('Nothing being played at the moment.')

        else:
            try:
                song = genius.search_song(sauce)
                lyrics_embed = discord.Embed(
                    title='Fifi Lyrics for **{}**'.format(sauce),
                    description=song.lyrics,
                    colour=discord.Colour.from_rgb(97, 0, 215)
                    )
                lyrics_embed.set_footer(text='Fifi Lyrics')
                lyrics_embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/356779184393158657/729351510974267513/plane-travel-icon-rebound2.gif')
                await ctx.send(embed=lyrics_embed)
            except AttributeError:
                await ctx.send('Could not find a match for {}'.format(sauce))
                print('Same error')

def setup(bot):
    bot.add_cog(Music(bot))