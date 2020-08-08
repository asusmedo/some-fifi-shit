import discord
from discord.ext  import commands
import time
from discord.utils import get
import asyncio

class  help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(pass_context=True)
    async def help(self,ctx):
        

        embed = discord.Embed(
            colour=discord.Color.purple()
        )

       
        
        embed = discord.Embed(title="Commands:", description="Need commands? Here you go!   ",)
        embed.add_field(name="```*help_nsfw```", value="Hahaha we all need that command :wink: ", inline=True)
        embed.add_field(name='```*help_mod```', value='commands for mod', inline=True)
        embed.add_field(name='```*help_music 1 ```', value='commands for music', inline=True)
        embed.add_field(name='```*help_music 2 ```', value='commands for music (plays from antoher websites)', inline=True)
        embed.add_field(name='```*embedurl```', value='send a photo as embed', inline=True)
        embed.add_field(name='```*embed```', value='send message as embed', inline=True)
        embed.add_field(name='```*fun```', value='commands for fun', inline=True)
        embed.add_field(name='```*ctf```', value='Converting Celsius to Fahrenheit', inline=True)
        embed.add_field(name='```*ftc```', value='Converting Fahrenheit to Celsius', inline=True)
        embed.add_field(name="```*ping```", value="Shows Bot Latency", inline=True)
        embed.add_field(name="```*ask```", value="ask bot a question", inline=True)
        embed.add_field(name="```*userinfo```", value="Gets info about the user.", inline=True)
        embed.add_field(name="```*av```", value="shows avatar", inline=True)
        embed.add_field(name="```*notfine```", value="Why are we still here? Just to suffer?", inline=True)
        embed.add_field(name="*```waj```", value="Try it , It's An Order! ", inline=True)
        embed.add_field(name="```*membercount```", value="shows how many member on the server (and bots) ", inline=True)
        embed.add_field(name="```*wordsfromgod```", value='gives you a list of random words, which are the words of god. inspired by terry a davis, RIP.')
        embed.add_field(name="```*cv```", value = 'usage: *cv <country>. gives you the current world stats of the pandemic')
        embed.add_field(name="```*help```", value="Brings you Here!", inline=True)
        
        await ctx.author.send(embed=embed)
        


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def help_mod(self,ctx):
        

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.add_field(name='```*reloadall ```', value='Reloads the bot if there is an error ', inline=True)
        embed.add_field(name='```*dm (member.id) (text)```', value='dm the member with fifi abdou ex. *dm 3252352523 hi ', inline=True)
        embed.add_field(name='```*clear **n**```', value='clear messages **n=number** ', inline=True)
        embed.add_field(name='```*ban @member reason```', value='ban a member', inline=True)
        embed.add_field(name='```*kick @member reason```', value='kick a member', inline=True)
        embed.add_field(name='```*mute @member nd nh nm ns```', value='mute member for a period of time ( ** nd= number of days,etc)', inline=True)
        embed.add_field(name="```*warn @member reason```",value='usage: .warn @user [reason] (this will send them a dm notifying them that theyve been warned for a reason u specify)',
                        inline=True)
        embed.add_field(name='```*cp listening to /lis ```', value='turn the bot status to listing  ex. *cp listening to fifi abdou', inline=True)
        embed.add_field(name='```*cp watching  /watch ```', value='turn the bot status to watching  ex. *cp watching  Teto', inline=True)
        embed.add_field(name='```*cp online ```', value='turn the bot status to online  ex. *cp online ', inline=True)
        embed.add_field(name='```*cp idle  ```', value='turn the bot status to idle  ex. *cp idle', inline=True)
        embed.add_field(name='```*cp dnd ```', value='turn the bot status to dnd  ex. *cp dnd ', inline=True)
        embed.add_field(name='```*cp lidnd ```', value='turn the bot status to listening while dnd  ex. *cp lidnd to fifi abdou ', inline=True)
        embed.add_field(name='```*cp wadnd ```', value='turn the bot status to watching while dnd  ex. *cp wadnd teto ', inline=True)
        embed.add_field(name='```*cp playdnd ```', value='turn the bot status to playing while dnd  ex. *cp playdnd fortnite ', inline=True)
        embed.add_field(name='```*cp (text) ```', value='turn the bot status to playing  ex. *cp fortnite ', inline=True)
        embed.add_field(name='```*cp  ```', value='turn the bot status to online  ex. *cp  ', inline=True)
        embed.add_field(name='```*ms  ```', value='musicsys  ', inline=True)
        
        await ctx.author.send(embed=embed)
        



    @commands.command(pass_context=True)
        
    async def help_nsfw(self,ctx):
        if  ctx.channel.is_nsfw():
                author = ctx.message.author

                embed = discord.Embed(
                colour = discord.Colour.green()
                )

                embed.set_author(name="Misc")
                embed.set_author(name="Available NSFW commands")
                embed.add_field(name="*feet", value='NSFW feet pics', inline=True)
                embed.add_field(name="*yuri", value='NSFW yuri pics', inline=True)
                embed.add_field(name="*trap", value='NSFW trap pics', inline=True)
                embed.add_field(name="*futanari", value='NSFW futanari pics', inline=True)
                embed.add_field(name="*hololewd", value='NSFW hololewd pics', inline=True)
                embed.add_field(name="*lewdkemo", value='NSFW lewdkemo pics', inline=True)
                embed.add_field(name="*solo_gif", value='NSFW solo gifs', inline=True)
                embed.add_field(name="*feet_gif", value='NSFW feet gif', inline=True)
                embed.add_field(name="*cum", value='NSFW cum on catgirls pics', inline=True)
                embed.add_field(name="*erokemo", value='NSFW erokemo pics', inline=True)
                embed.add_field(name="*les", value='NSFW les pics', inline=True)
                embed.add_field(name="*wallpaper", value='cute wallpapers', inline=True)
                embed.add_field(name="*lewdk", value='NSFW lewdk pics', inline=True)
                embed.add_field(name="*neko_gif", value='cute neko pics :flushed:', inline=True)
                embed.add_field(name="*meow", value='cute cat pics', inline=True)
                embed.add_field(name="*tickle", value='usage: .tickle @user tickle tickle', inline=True)
                embed.add_field(name="*lewd", value='lewd catgirls', inline=True)
                embed.add_field(name="*feed", value='usage: .feed @user eat up fatty', inline=True)
                embed.add_field(name="*gegc", value='genetically engineerd catgirl memes', inline=True)
                embed.add_field(name="*eroyuri", value='NSFW eroyuri', inline=True)
                embed.add_field(name="*eron", value='NSFW eron', inline=True)
                embed.add_field(name="*bj", value='NSFW bj', inline=True)
                embed.add_field(name="*nsfw_neko_gif", value='NSFW neko gif', inline=True)
                embed.add_field(name="*solo", value='NSFW solo pic', inline=True)
                embed.add_field(name="*kemonomimi", value='NSFW kemonomimi pic', inline=True)
                embed.add_field(name="*nsfw_avatar", value='NSFW avatar pic for u horny virgins', inline=True)
                embed.add_field(name="*gasm", value='usage: .gasm @user no way dude', inline=True)
                embed.add_field(name="*poke", value='usage: .poke @user beep', inline=True)
                embed.add_field(name="*slap", value='usage: .slap @user u cunt', inline=True)
                embed.add_field(name="*anal", value='NSFW anal pic', inline=True)
                embed.add_field(name="*hentai", value='NSFW hentai pic', inline=True)
                embed.add_field(name="*avatar", value='generates a dope avatar pic', inline=True)
                embed.add_field(name="*erofeet", value='NSFW erofeet', inline=True)
                embed.add_field(name="*pussy", value='NSFW pussy', inline=True)
                embed.add_field(name="*tits", value='NSFW tits', inline=True)
                embed.add_field(name="*waifu", value='waifu. self explanotory you weeb', inline=True)
                embed.add_field(name="*boobs", value='boobs', inline=True)
                embed.add_field(name="*smallboobs", value='smallboobies ', inline=True)
                embed.add_field(name="*pat", value='usage: .pet @user u cutie', inline=True)
                embed.add_field(name="*kiss", value='usage: .kiss @user muah (no homo)', inline=True)
                embed.add_field(name="*spank", value='usage: .spank @user BRUH', inline=True)
                embed.add_field(name="*cuddle", value='usage: .cuddle @user u cutie', inline=True)
                embed.add_field(name="*hug", value='usage: .hug @user u cutie', inline=True)
                embed.add_field(name="*hugs", value='usage: .hugs @user u cutie', inline=True)                
                embed.add_field(name="*fox_girl", value='fox girl pics', inline=True)
                embed.add_field(name="*neko", value='neko pics', inline=True)
                
                await ctx.send(author.mention, embed=embed)

        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")



    @commands.command(pass_context=True)
    async def fun(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.green()
        )
        
        embed.add_field(name='```*ship```', value='OwO relation ship between two people (must mention)' , inline=True)
        embed.add_field(name='```*insult```', value='insulting people ( must mention)' , inline=True)
        embed.add_field(name='```*hug```', value='hugs people ( must mention)', inline=True)
        embed.add_field(name='```*hugs```', value='hugs people again ( must mention)', inline=True)
        embed.add_field(name='```*flip```', value='Flip Flip Flop', inline=True)
        embed.add_field(name='```*rekt```', value='rekt or not (must mention) ', inline=True)
        embed.add_field(name='```*howgay```', value='gay calculator (must mention) ', inline=True)
        embed.add_field(name='```*howsimp```', value='simp calculator (must mention) ', inline=True)
        embed.add_field(name='```*howlesbian```', value='lesbian calculator (must mention) ', inline=True)
        embed.add_field(name='```*howcringe```', value='cringe calculator (must mention) ', inline=True)
        embed.add_field(name='```*simp```', value='simping on people  (must mention) ', inline=True)
        embed.add_field(name='```*dong```', value='dong calculator (must mention) ', inline=True)
       
        
        
        await ctx.send(author.mention, embed=embed)
    

    @commands.command(pass_context=True)
    async def help_music(self,ctx):

        
        author = ctx.message.author

        
        embed = discord.Embed(title="Fofa Music", description="v 0.3 ",
            colour = discord.Colour.green()
        )
        
        embed.add_field(name='```supported sites```', value='youtube / soundcloud / alot of webistes / spotify( `soon` )' , inline=True)
        embed.add_field(name='```*ly / lyrics```', value='get the music lyrics' , inline=True)
        embed.add_field(name='```*ml / musiclyrics```', value='search for  lyrics (ex: *ml bad guy)' , inline=True)
        embed.add_field(name='```*fifi / join```', value='fifi join the voice channel' , inline=True)
        embed.add_field(name='```*np / nowplaying / current / playing ```', value='shows what is playing ' , inline=True)
        embed.add_field(name='```*p /play ```', value='plays your  music', inline=True)
        embed.add_field(name='```*search ```', value='search  engine for music', inline=True)
        embed.add_field(name='```*pause / pp```', value='pause the music', inline=True)
        embed.add_field(name='```*resume / r```', value='resume the music', inline=True)
        embed.add_field(name='```*loop / l```', value='Looping music ( not working rn)', inline=True)
        embed.add_field(name='```*queue /q```', value='shows what is is the queue ', inline=True)
        embed.add_field(name='```*skip```', value='skips the  music', inline=True)
        embed.add_field(name='```*bye / leave / fuckoff ```', value='fifi leaves the voice channel ', inline=True)

        await ctx.send(author.mention, embed=embed)
        



       
        
        
        
       

    
def setup(bot):
    bot.add_cog(help(bot))








        