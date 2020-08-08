import discord
from discord.ext import commands

import datetime
import requests
import json


import config
from u_mongo import Mongo

async def lang_text(guild_id):
    record = await Mongo.get_record('cfg_ser','guild_id',str(guild_id))
    final_lang= record['lang']
    with open('language.json','r', encoding='utf-8') as file:
        text = json.loads(file.read())
        return text[final_lang]

class Utillites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    #Lyrics
    @commands.command()
    async def lyrics(self, ctx, *, lyrics_name):
        """
        Lyrics music
        """
        lyrics_url = f"https://api.ksoft.si/lyrics/search?q={lyrics_name}&limit=1"
        r =requests.get(lyrics_url, headers={"Authorization":(config.ksoft_keys)})
        response_json= json.loads(r.text)

        text= (await lang_text(ctx.message.guild.id))['lyrics']

        try:
            text= response_json['data'][0]['lyrics']
        except IndexError:
            await ctx.send(text['error'])
            
        else:
            artist= response_json['data'][0]['artist']
            name_song= response_json['data'][0]['name']

            genuis_url= f'https://api.genius.com/search?q={artist}%20{name_song}'
            re= requests.get(genuis_url, headers={"Authorization":(config.Genius_key)})
            response_jsn= json.loads(re.text)
            image= response_jsn['response']['hits'][0]['result']['header_image_url']

            len_text= len(text)
            if len_text>2048:
                s= text[:2047]
                s1=text[2048:4095]
                em= discord.Embed(title=f"{artist} - {name_song}", description=(s), color= 0xd8a903)
                em.set_thumbnail(url =(image))
                em1= discord.Embed(title= '', description=(s1), color=0xd8a903)
                em1.set_footer(text= "Fifi Lyrics")
                await ctx.send(embed= em)
                await ctx.send(embed= em1)

            elif len_text<2047:
                em= discord.Embed(title=f'{artist} - {name_song}', description= (text), color= 0xd8a903)
                em.set_thumbnail(url= (image))
                em.set_footer(text= "Powered by kSoft/Genius")
                await ctx.send(embed= em)

def setup(bot):
    bot.add_cog(Utillites(bot))