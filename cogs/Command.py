import discord
import praw
import json
import random
from discord.ext  import commands
import asyncio
import urllib
import random
import random2
import discord
import requests
from discord.ext import commands
from discord import Game
from random import choice
import re
from discord import TextChannel, VoiceChannel
from discord.ext import commands

import discord




client = discord.Client()



ADMIN_ROLES = ['fifi']
MOD_ROLES = [*ADMIN_ROLES, 'fifi']

# 0xRRGGBB aka HEX
MAIN_COLOR = 0x091A4C
ERROR_COLOR = 0xD86156
OFF_COLOR_1 = 0xF2B53C
OFF_COLOR_2 = 0x5F6662
INFO_COLOR = 0x3BCCB3

NATIVE_COLOR = 0x0070BB
FLUENT_COLOR = 0x765A9F
LEARNING_COLOR = 0xC54b8C
YELLOW_ROLE_COLOR = 0xFFC40C
ORANGE_ROLE_COLOR = 0xFF7518
BLACK_ROLE_COLOR = 0x000001

LANGUAGE_ROLES = [NATIVE_COLOR, FLUENT_COLOR, LEARNING_COLOR]
ASSIGNABLE_ROLE_COLORS = [*LANGUAGE_ROLES, YELLOW_ROLE_COLOR, ORANGE_ROLE_COLOR, BLACK_ROLE_COLOR]

YES_EMOJI = '✅'
NO_EMOJI = '❌'


text_lines = {
    ##############  IMPORTANT  ###############
    # Hierarchy: Cog (Class) -> Method -> Line
   

    'server_info': {
        'titles': {
            'id': 'Id',
            'owner': 'Owner',
            'region': 'Region',
            'roles': 'Roles: ',  # Amount of roles
            'features': 'Features',
            'default_channel': 'Default channel',
            'channels': 'Channels: {}',  # Amount of channels
            'created_at': 'Created at',
            'members': 'Members: {}',  # Amount of members
            'emojis': 'Emojis: {}'  # Amount of emojis
        },
        'members_line': '{} tagged, {} normies',  # In total, Without roles
        'roles': '{} language, {} other',  # Amount of language roles, Amount of other roles
        'channel_line': '{} text, {} voice'  # Text channels, Voice channels
    },

    'technical': {
        'forbidden': 'I don\'t have access to write to #{} on {}',  # Channel name, Server name
        'cant_do_in_pm': 'I can\'t perform this command in DMs',
        'none': 'None',
        'unknown_error': 'An unknown error has happened, pls report this line to the bot devs. arigato'
                         '\n\n**Copy and paste this**\n`{}`'  # Error line
    },

   
}


insults = [
    ("Yo Mama so dumb I told her Christmas was around the corner and she went looking for it."),
    ("You're so dumb it took you 2 hours to watch 60 minutes."),
    ("Yo Mama so dumb she bought tickets to Xbox Live."),
    ("You're so dumb that you thought The Exorcist was a workout video."),
    ("You're so ugly that you went to the salon and it took 3 hours just to get an estimate."),
    ("You're so ugly that even Scooby Doo couldn't solve that mystery."),
    ("What is the weighted center between Planet X and Planet Y? Oh it's YOU!"),
    (":eggplant: :eggplant: :eggplant:"),
    ("Your birth certificate is an apology letter from the condom factory."),
    ("I wasn't born with enough middle fingers to let you know how I feel about you."),
    ("You must have been born on a highway because that's where most accidents happen."),
    ("I'm jealous of all the people that haven't met you."),
    ("I bet your brain feels as good as new, seeing that you never use it."),
    ("I'm not saying I hate you, but I would unplug your life support to charge my phone."),
    ("You're so ugly, when your mom dropped you off at school she got a fine for littering."),
    ("You bring everyone a lot of joy, when you leave the room."),
    ("What's the difference between you and eggs? Eggs get laid and you don't."),
    ("You're as bright as a black hole, and twice as dense."),
    ("I tried to see things from your perspective, but I couldn't seem to shove my head that far up my ass."),
    ("Two wrongs don't make a right, take your parents as an example."),
    ("You're the reason the gene pool needs a lifeguard."),
    ("If laughter is the best medicine, your face must be curing the world."),
    ("You're so ugly, when you popped out the doctor said \"Aww what a treasure\" and your mom said \"Yeah, lets bury it.\""),
    ("I have neither the time nor the crayons to explain this to you."),
    ("You have two brains cells, one is lost and the other is out looking for it."),
    ("How many times do I have to flush to get rid of you?"),
    ("I don't exactly hate you, but if you were on fire and I had water, I'd drink it."),
    ("You shouldn't play hide and seek, no one would look for you."),
    ("Some drink from the fountain of knowledge; you only gargled."),
    ("Roses are red violets are blue, God made me pretty, what happened to you?"),
    ("It's better to let someone think you are an Idiot than to open your mouth and prove it."),
    ("Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology."),
    ("The last time I saw a face like yours I fed it a banana."),
    ("The only way you'll ever get laid is if you crawl up a chicken's ass and wait."),
    ("Which sexual position produces the ugliest children? Ask your mother."),
    ("If you really want to know about mistakes, you should ask your parents."),
    ("At least when I do a handstand my stomach doesn't hit me in the face."),
    ("If I gave you a penny for your thoughts, I'd get change."),
    ("If I were to slap you, it would be considered animal abuse."),
    ("Do you know how long it takes for your mother to take a crap? Nine months."),
    ("What are you going to do for a face when the baboon wants his butt back?"),
    ("Well I could agree with you, but then we'd both be wrong."),
    ("You're so fat, you could sell shade."),
    ("It looks like your face caught on fire and someone tried to put it out with a hammer."),
    ("You're not funny, but your life, now that's a joke."),
    ("You're so fat the only letters of the alphabet you know are KFC."),
    ("Oh my God, look at you. Was anyone else hurt in the accident?"),
    ("What are you doing here? Did someone leave your cage open?"),
    ("You're so ugly, the only dates you get are on a calendar."),
    ("I can explain it to you, but I can't understand it for you."),
    ("You are proof that God has a sense of humor."),
    ("If you spoke your mind, you'd be speechless."),
    ("Why don't you check eBay and see if they have a life for sale."),
    ("If I wanted to hear from an asshole, I'd fart."),
    ("You're so fat you need cheat codes to play Wii Fit"),
    ("You're so ugly, when you got robbed, the robbers made you wear their masks."),
    ("Do you still love nature, despite what it did to you?"),
    ("You are proof that evolution CAN go in reverse."),
    ("I'll never forget the first time we met, although I'll keep trying."),
    ("Your parents hated you so much your bath toys were an iron and a toaster"),
    ("Don't feel sad, don't feel blue, Frankenstein was ugly too."),
    ("You're so ugly, you scared the crap out of the toilet."),
    ("It's kinda sad watching you attempt to fit your entire vocabulary into a sentence."),
    ("I fart to make you smell better."),
    ("You're so ugly you make blind kids cry."),
    ("You're a person of rare intelligence. It's rare when you show any."),
    ("You're so fat, when you wear a yellow rain coat people scream ''taxi''."),
    ("I heard you went to a haunted house and they offered you a job."),
    ("You look like a before picture."),
    ("If your brain was made of chocolate, it wouldn't fill an M&M."),
    ("Aww, it's so cute when you try to talk about things you don't understand."),
    ("I heard your parents took you to a dog show and you won."),
    ("You stare at frozen juice cans because they say, \"concentrate\"."),
    ("You're so stupid you tried to wake a sleeping bag."),
    ("Am I getting smart with you? How would you know?"),
    ("We all sprang from apes, but you didn't spring far enough."),
    ("I'm no proctologist, but I know an asshole when I see one."),
    ("When was the last time you could see your whole body in the mirror?"),
    ("You must have a very low opinion of people if you think they are your equals."),
    ("So, a thought crossed your mind? Must have been a long and lonely journey."),
    ("You're the best at all you do - and all you do is make people hate you."),
    ("Looks like you fell off the ugly tree and hit every branch on the way down."),
    ("Looks aren't everything; in your case, they aren't anything."),
    ("You have enough fat to make another human."),
    ("You're so ugly, when you threw a boomerang it didn't come back."),
    ("You're so fat a picture of you would fall off the wall!"),
    ("Your hockey team made you goalie so you'd have to wear a mask."),
    ("Ordinarily people live and learn. You just live."),
    ("Did your parents ever ask you to run away from home?"),
    ("I heard you took an IQ test and they said your results were negative."),
    ("You're so ugly, you had tinted windows on your incubator."),
    ("Don't you need a license to be that ugly?"),
    ("I'm not saying you're fat, but it looks like you were poured into your clothes and someone forgot to say \"when\""),
    ("I've seen people like you, but I had to pay admission!"),
    ("I hear the only place you're ever invited is outside."),
    ("Keep talking, someday you'll say something intelligent!"),
    ("You couldn't pour water out of a boot if the instructions were on the heel."),
    ("Even if you were twice as smart, you'd still be stupid!"),
    ("You're so fat, you have to use a mattress as a maxi-pad."),
    ("I may be fat, but you're ugly, and I can lose weight."),
    ("I was pro life before I met you."),
    ("What's the difference between you and Hitler? Hitler knew when to kill himself."),
    ("You're so fat, your double chin has a double chin."),
    ("If ignorance is bliss, you must be the happiest person on earth."),
    ("You're so stupid, it takes you an hour to cook minute rice."),
    ("Is that your face? Or did your neck just throw up?"),
    ("You're so ugly you have to trick or treat over the phone."),
    ("I'd hit you but we don't hit girls around here."),
    ("Dumbass."),
    ("Bitch."),
    ("I'd give you a nasty look but you've already got one."),
    ("If I wanted a bitch, I'd have bought a dog."),
    ("Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons."),
    ("Why is it acceptable for you to be an idiot but not for me to point it out?"),
    ("Did you know they used to be called \"Jumpolines\" until your mum jumped on one?"),
    ("You're not stupid; you just have bad luck when thinking."),
    ("I thought of you today. It reminded me to take the garbage out."),
    ("I'm sorry I didn't get that - I don't speak idiot."),
    ("Hey, your village called \u2013 they want their idiot back."),
    ("I just stepped in something that was smarter than you\u2026 and smelled better too."),
    ("If you were any less intelligent we'd have to water you three times a week.."),
    ("If your IQ was 3 points higher, you'd be a rock."),
    ("I would insult you but nature did a better job."),
    ("Does your ass get jealous of all the shit that comes out of your mouth?"),
    ("If I ate a bowl of alphabet soup, I could shit out a smarter sentence than any of yours."),
    ("You're not pretty enough to be this stupid."),
    ("That little voice in the back of your head, telling you you'll never be good enough? It's right."),
    ("You look like you're going to spend your life having one epiphany after another, always thinking you've finally figured out what's holding you back, and how you can finally be productive and creative and turn your life around. But nothing will ever change. That cycle of mediocrity isn't due to some obstacle. It's who you *are*. The thing standing in the way of your dreams is; that the person having them is *you*."),
    ("May your day and future be as pleasant as you are."),
    ("I would agree with you but then we would both be wrong."),
    ("I bite my thumb at you, sir."),
    ("I'd call you a tool, but that would imply you were useful in at least one way."),
    ("I hope you outlive your children."),
    ("Are you and your dick having a competition to see who can disappoint me the most?"),
    ("Yo mamma is so ugly her portraits hang themselves."),
    ("Your birth certificate is an apology from the abortion clinic."),
    ("If you were anymore inbred you'd be a sandwich."),
    ("Say hello to your wife and my kids for me."),
    ("You are thick-headed bastards with a bloated bureaucracy, designed to compensate for your small and poor self-esteem, cocksuckers. You have the brains to ban the person who has come to support channel your bot, accusing him of violating the ephemeral ephemeral rules, stupid morons. By the way i have one of the biggest server(5.5k  people, ~30 anytime voiceonline members), and i know something about managing, and of these rules - dont be an asshole. You are fucking asshole, maybe it is product of your life alone, or your life with your mom, anyway - you are retard and your soul is a fucking bunch of stupid self-esteems.")
]

reddit = praw.Reddit(client_id='707044345299206144',
                            client_secret='qQxJksGqaDUgzCpnwxT3NToFbilj2uPw',
                            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
bot = commands.Bot(command_prefix='*')
class  command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    client = commands.Bot(command_prefix ='.')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        if message.content.lower() == 'F' :
            await message.channel.send('F')
        if message.content.lower() == 'f' :
            await message.channel.send('F')
        if message.content.startswith('GG'):
            await message.channel.send('WP')        
        if message.content.startswith('gg'):
            await message.channel.send('wp')
        if message.content.startswith('Gg'):
            await message.channel.send('WP')        
        if message.content.startswith('gG'):
            await message.channel.send('wp')
        if message.content.startswith('Rip'):
            await message.channel.send('Rip')
        if message.content.startswith('rip'):
            await message.channel.send('rip')
        if message.content.startswith('RiP'):
            await message.channel.send('RiP')
        if message.content.startswith('RIP'):
            await message.channel.send('RIP')
        if message.content.startswith('riP'):
            await message.channel.send('riP')
        if message.content.startswith('owo'):
            await message.channel.send('owo')
        if message.content.startswith('OwO'):
            await message.channel.send('OwO')
        if message.content.startswith('oWo'):
            await message.channel.send('oWo')
        if message.content.startswith('Owo'):
            await message.channel.send('Owo')
        if message.content.startswith('owO'):
            await message.channel.send('owO')
        if message.content.startswith('OWO'):
            await message.channel.send('OWO')
        if message.content.startswith('0w0'):
            await message.channel.send('0w0')
        if message.content.startswith('OWo'):
            await message.channel.send('Owo')
        if message.content.startswith('saly 3la naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('saly 3ala naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('saly 3ala el naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('saly 3la el naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('SALY 3LA EL NABY'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('Saly 3la el naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('sly 3la el naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('Sly 3la el naby '):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('SLY 3LA EL NABY'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('sly 3ala el naby'):
            await message.channel.send('3aleh el salah w el salam')
        if message.content.startswith('ad7aky ya fifi'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('ad7ky ya fifi'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('AD7AKY YA FIFI'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('AD7KY YA FIFI'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('Ad7ky ya fifi'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('Ad7aky ya fifi'):
            await message.channel.send('Hehehehehehe')
        if message.content.startswith('ash5ory ya fifi'):
            await message.channel.send('555555555555555')
        if message.content.startswith('Ash5ory ya fifi'):
            await message.channel.send('555555555555555')
        if message.content.startswith('ASH5ORY YA FIFI'):
            await message.channel.send('555555555555555')
        if message.content.startswith('b7bk ya fifi'):
            await message.channel.send('Yalaahwwiiiii escooooz meeeee')
        if message.content.startswith('islam el marg'):
            await message.channel.send('Islam el marg')
        if message.content.startswith('Islam el marg'):
            await message.channel.send('Islam el marg')
        if message.content.startswith('ISLAM EL MARG'):
            await message.channel.send('Islam el marg')



        
        


        

    @commands.Cog.listener("on_message")
    async def swear_listener(self,message:discord.Message):
        """Looks for swearing in the message and tells people off"""

        if message.author.bot:
            return

        content = set(message.content.lower().strip().split())
        swears = {"kys"}
        if content.intersection(swears): 
            await message.channel.send(f'DO IT YOU PUSSY! {message.author.mention}   ')

    @commands.Cog.listener("on_message")
    async def swear_listen(self, message:discord.Message):
        """Looks for swearing in the message and tells people off"""

        if message.author.bot:
            return

        content = set(message.content.lower().strip().split())
        swears = {"7omos"}
        swearss = {"Tea","tea","teA","TEA","tEa"}
        bruh = {"Bruh","BRUH","bruh","BrUh","bRuH","BRuh"}
        takbeer = {"Takbeer","TAKBEER","takbeer"}
        ee = {"69"}
        test = {"besm", "Besm", "BESM"}
        fa ={"\U0001f351"}
        af ={"\U0001f346"}
        ass ={"Ass","ass","ASS"}
        author = message.author
        users = [342232703195676674, 693176581237244047 , 725032390791266355, 568844317297475605]
        if content.intersection(swears): 
            if author.id in users :
                await message.channel.send(f"Ent 2lp 7omos :heart: {message.author.mention} .")
            elif author.id==(290169006164279296):
                await message.channel.send(f"2lp Fifi Ya 7omos :heart: :heart:")
            elif author.id==(221343205394743306):
                await message.channel.send(f"55555 Kosomk don't mention My 7omos again {message.author.mention} .")
            else:
                await message.channel.send(f"Don't say my friend's name You Fucking Slut {message.author.mention} . 😡 ") 
        if content.intersection(swearss): 
            await message.channel.send(f"Drink And Pee!")     
        if content.intersection(bruh): 
            await message.channel.send(f"Bruh..")
        if content.intersection(takbeer): 
            await message.channel.send(f"ALLAHU AKBAAR! 💥")
        if content.intersection(ee): 
            await message.channel.send(f" Noice ") 
        if content.intersection(fa): 
            await message.channel.send(f" بسم الله ما شاء الله ")
        if content.intersection(af): 
            await message.channel.send(f" بـــســـم الــصـلــيـب ")  
            
        if content.intersection(test): 
            x = await message.channel.send(content="B")
            await asyncio.sleep(0.5)
            await x.edit(content='Be')
            await asyncio.sleep(0.5)
            await x.edit(content='Bes')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm.')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm..')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm...')
            await asyncio.sleep(0.5)
            await x.edit(content='Be')
            await asyncio.sleep(0.5)
            await x.edit(content='Bes')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm.')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm..')
            await asyncio.sleep(0.5)
            await x.edit(content='Besm...')

        if content.intersection(ass):
            await message.channel.send('\U0001f1e6 \U0001f1f8 \U0001f1f8')
    
            
    ###

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, channel: discord.TextChannel, *, content: str):
        await channel.send(content)

    ###
    @commands.command()
    async def ctf(self,ctx, c: float ):
        
        async with ctx.typing():
            await asyncio.sleep(.01)

            

            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author

            
            f = (c * (9/5)) + 32
          

            embed = discord.Embed(
                    colour=discord.Colour.gold()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= "Celsius to Fahrenheit Converter" , value= f , inline=False)

            await ctx.send(embed=embed)
            
            
    ###
    @commands.command()
    async def ftc(self,ctx,  f: float ):
        
        async with ctx.typing():
            await asyncio.sleep(.01)

            
            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author

            c = ((f - 32) * (5/9))
            
            embed = discord.Embed(
                    colour=discord.Colour.gold()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= "Fahrenheit to Celsius Converter" , value= c , inline=False)

            await ctx.send(embed=embed)
    ###        

    @commands.command()
    async def notfine(self,message):
            embed = discord.Embed()
            notfine = embed.set_image(url='https://cdn.discordapp.com/attachments/342216929982808066/347541935990374400/not_fine.gif')
            await message.channel.send(embed=notfine)

    @commands.command()
    async def waj(self,message):
            embed = discord.Embed()
            waj = embed.set_image(url='https://b.top4top.io/p_1588r9fsl1.jpg')
            await message.channel.send(embed=waj)  

    @commands.command(aliases=['ms'])
    async def music_sys(self,message):
            embed = discord.Embed()
            music = embed.set_image(url='https://a.top4top.io/p_1670fczeo2.png')
            await message.channel.send(embed=music) 
            await message.channel.send('`when you play a music with fifi it will show u the name and the Duration`')
            ga = embed.set_image(url='https://l.top4top.io/p_1670xl7vx1.png')   
            await message.channel.send(embed=ga)
            await message.channel.send('`when u add another song it will add it to fifi queue like what u see in the pic rn , u can remove the queue and u can skip it too , goodluck`')
    
    @commands.command()
    async def embedurl(self,ctx, url):
        await ctx.message.delete()
        embed = discord.Embed()
        test = embed.set_image(url=url)
        await ctx.channel.send(embed=test)

    @commands.command()
    async def embed(self, ctx, message):
        await ctx.message.delete()
        embed = discord.Embed()
        ga = embed.add_field(name='Fifi Embed', value=(f'`{message}'), inline=False)
        await ctx.channel.send(embed=ga)
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send("{}".format(msg))
    

    @commands.command()
    async def dong(self,ctx, user1: discord.Member):
        """Detects user's penis length"""
        async with ctx.typing():
            await asyncio.sleep(.01)

            if user1 is None:
                user1 = ctx.message.author

            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            length = ['=', '==', '===', '====', '=====', '======', '=======', '========', '']
            dong = "8" + (random.choice(length)) + "D"

            if user1.id == 342232703195676674 :
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + "8========================D", 
                    colour=discord.Colour.blurple()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name + "||Yes I HAVE BIG DONG|| ")

                await ctx.send(embed=embed)
            elif user1.id == 722720979247169547:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + "8========================D", 
                    colour=discord.Colour.dark_teal()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)
                return
            elif user1.id == 568844317297475605:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + "8========================D", 
                    colour=discord.Colour.dark_teal()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)
                return
            elif user1.id == 420647823407841281:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + "8========================D", 
                    colour=discord.Colour.dark_teal()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + dong, 
                    colour=discord.Colour.dark_teal()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)

    ####
    @commands.command()
    async def ran(self, ctx):
        score = random.randint(0, 100)
        if score==69:
            await ctx.send('ايوه يا عم 69 ')

        elif score==42:
            await ctx.send(score + '  , More like 420 ? :wink: ')

        else:
            await ctx.send(score)
        
    ####
    @commands.command(aliases=['mul','multiply'])
    async def multiplication(self, ctx,arg,arg1):
        result = float(arg) * float(arg1)
        phrase = "{} * {} = {} Ya 2lpi :heart: ".format(str(arg),str(arg1),result)
        await ctx.send(phrase)

    @commands.command(aliases=['sum','add'])
    async def addition(self, ctx,arg,arg1):
        result = float(arg)+float(arg1)
        phrase = "{} + {} = {} Ya 2lpi :heart: ".format(str(arg),str(arg1),result)
        await ctx.send(phrase)

    @commands.command(aliases=['div'])
    async def division(self, ctx,arg,arg1):
        result = float(arg) / float(arg1)
        phrase = "{} / {} = {} Ya 2lpi :heart: ".format(str(arg),str(arg1),result)
        await ctx.send(phrase)

    @commands.command(aliases=['sub'])
    async def subtraction(self, ctx,arg,arg1):
        result = float(arg) - float(arg1)
        phrase = "{} - {} = {} Ya 2lpi :heart:".format(str(arg),str(arg1),result)
        await ctx.send(phrase)
    
            

        
    ####
    @commands.command()
    async def howgay(self, ctx, user1: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user1 is None:
            user1 = ctx.message.author

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        
        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        empty_progbar = (10 - filled_progbar)
        counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

        if score < 30:
            message = "Aww shit looks like you aint gay, sad !"
        elif score < 60:
            message = "Huh....well you could be Bi, explore that!"
        elif score < 80:
            message = "Yeah you pretty gay mate! :gay_pride_flag: "
        elif score > 80:
            message = "Wow you so gay you probably fart glitter! :gay_pride_flag: "  

        embed = discord.Embed(
                    colour=discord.Colour.dark_purple()
                    )
        embed.set_author(name= 'Gay R8 machine')
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
        embed.add_field(name= ':gay_pride_flag:  Score percentage: :gay_pride_flag: ' , value= score , inline=False)
        embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
        embed.add_field(name=  ' ' + message , value= '\u200b' , inline=False)

        await ctx.send(embed=embed)
#################
    @commands.command()
    async def howlesbian(self, ctx, user1: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user1 is None:
            user1 = ctx.message.author

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        
        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        empty_progbar = (10 - filled_progbar)
        counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

        if score < 30:
            message = "Aww shit looks like you aint Lesbian, sad !"
        elif score < 60:
            message = "Huh....well you could be Bi, explore that!"
        elif score < 80:
            message = "Yeah you pretty Lesbian mate! :gay_pride_flag: "
        elif score > 80:
            message = "Wow you so Lesbian you probably fart glitter! :gay_pride_flag: "  

        embed = discord.Embed(
                    colour=discord.Colour.dark_purple()
                    )
        embed.set_author(name= 'lesbian R8 machine')
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
        embed.add_field(name= ':gay_pride_flag:  Score percentage: :gay_pride_flag: ' , value= score , inline=False)
        embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
        embed.add_field(name=  ' ' + message , value= '\u200b' , inline=False)

        await ctx.send(embed=embed)
#################
    @commands.command()
    async def howsimp(self, ctx, user1: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user1 is None:
            user1 = ctx.message.author

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        
        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        empty_progbar = (10 - filled_progbar)
        counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

        if score < 30:
            message = "Aww ... looks like you aint simp, Go learn how to simp !"
        elif score < 60:
            message = "Huh....well you could be simp, But Does this mean we're married now? :see_no_evil: !"
        elif score < 80:
            message = "Yeah you pretty simp mate! :hot_face: :sweat_drops: "
        elif score > 80:
            message = "WoW you must be donating 11K dollars to a female twitch streamer on a daily basis! :pig_nose: :regional_indicator_s: :regional_indicator_i: :regional_indicator_m: :regional_indicator_p: :sweat_drops: "  

        embed = discord.Embed(
                    colour=discord.Colour.green()
                    )
        embed.set_author(name= 'Simp machine')
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
        embed.add_field(name= ':pig_nose: :regional_indicator_s: :regional_indicator_i: :regional_indicator_m: :regional_indicator_p: :sweat_drops: Score percentage:     ' , value= score , inline=False)
        embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
        embed.add_field(name=  ' ' + message , value= '\u200b' , inline=False)

        await ctx.send(embed=embed)
#################
    @commands.command()
    async def howcringe(self, ctx, user1: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user1 is None:
            user1 = ctx.message.author

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author

        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        empty_progbar = (10 - filled_progbar)
        counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

        if score < 30:
            message = "Aww shit looks like you aint cringe, sad !"
        elif score < 60:
            message = "Huh....well you could be cringy, explore that!"
        elif score < 80:
            message = "Yeah you pretty cringy mate! :zany_face: "
        elif score > 80:
            message = "Wow you so cringy you probably fart cringe! :zany_face: "  

        embed = discord.Embed(
                    colour=discord.Colour.red()
                    )
        embed.set_author(name= 'Cringe  machine')
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
        embed.add_field(name= ':zany_face:  Score percentage: :zany_face: ' , value= score , inline=False)
        embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
        embed.add_field(name=  ' ' + message , value= '\u200b' , inline=False)

        await ctx.send(embed=embed)
###############

    @commands.command()
    async def insult(self, ctx, user1 : discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author

        if user1.id == 722720979247169547: #if bot is mentioned
            user = ctx.message.author
            msg = [("How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."), 
                    ("The fuck did ya just call me, cunt? I’ll have ya know I graduated top of me class at Sunshine TAFE, I’ve been involved in numerous beer skulling contests against Bob Hawke, and I have over 300 confirmed Cold Chisel albums. I am trained in vocal abuse towards umpires and I am the top snag eater in the entire city of Carlton. You are nothing to me but just another Collingwood fan. I will knock ya the fuck out with VB stubbies the likes of which have never been smashed before on this Earth, mark me fucken words. You reckon ya can get away with flapping ya beak to me over the Internet? Think again, cunt. As we speak I am contacting all me fucken lads across Western Sydney and ya IP is being traced right now so ya better prepare for the thunder, mate. The thunder that wipes out the pathetic little thing you call ya life. You’re fucking dead, prick. I can be anywhere, anytime, drinking anything, and I can glass you in over seven hundred ways, and that’s just with me smashed VB longneck. Not only am I extensively trained in smashing cunts, but I have access to the entire shed of cricket bats of the Melbourne Cricket Ground and I will use it to its full extent to hit ya for 6 and out, ya shitcunt. If only ya coulda known what bullshit your little “clever” backchat was about ta bring down upon ya, maybe ya woulda held your fucking tongue. But ya couldn’t, ya didn’t, and now you’re paying the price, mate. I will shit fury all over ya and you’re gonna drown in it, so ya better run, ya better take cover. You’re fucken dead, mate."),
                    ("I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                    ("Oi what the fuck cunt!"),
                    ("Scurry off cheeky bugger!"),
                    ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]
            
            message = choice(msg)
            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user.name , value= message , inline=False)
            await ctx.send(embed=embed)


        elif user1.id == 342232703195676674: ##bot owner ## hehehe
            user = ctx.message.author
            msg = [("You dare insult my creator, ya furking cunt!"), 
                    ("Another cunt that wants to insult my creator, oi guys look we got a smart ass over here!"),
                    ("You dare insult my creator, I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                    ("Oi what the fuck cunt! Dont try insult my creator"),
                    ("Scurry off cheeky bugger!"),
                    ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]

            message = choice(msg)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user.name , value= message , inline=False)
            await ctx.send(embed=embed)

        else:
            message = choice(insults)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user1.name , value= message , inline=False)
            await ctx.send(embed=embed)

#################


    @commands.command()
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user2 is None:
            user2 = ctx.message.author

        if user1 is ctx.message.author and user2 is ctx.message.author:
            await ctx.send("Are you really that alone ?")
        
        else:
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author

            score = random.randint(0, 100)
            filled_progbar = round(score / 100 * 10)
            empty_progbar = (10 - filled_progbar)
            counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

            if score < 30:
                message = "I don't know what to say about, they really don't seem to match..."
            elif score < 60:
                message = "Well... give it a shot but I wouldnt count on it working out"
            elif score < 80:
                message = "UWU ... what a Lovely Ship!"
            elif score > 80:
                message = "UWU!! strong candidate for ship of the year!"

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_author(name= "%s  ❤  %s" % (user1.name, user2.name,))
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= message , value= (counter_) , inline=False)
            embed.add_field(name= score , value= 'Percent' , inline=False)

            await ctx.send(embed=embed)

            
    @commands.command()
    async def rip(self, ctx, text: str):
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            # parse = urllib.parse.quote(text)
            await ctx.channel.trigger_typing()

            if text is None:
                await ctx.send("You have to say something to pay respects like E.g *rip {something here}")

            else:
                embed = discord.Embed(
                        description = 'RIP',
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.set_image(url="http://www.tombstonebuilder.com/generate.php?top1="+ urllib.parse.quote_plus((text), safe='', encoding=None, errors=None) +"&top2=&top3=&top4=&sp=")

                await ctx.send(embed=embed)
                return

    @commands.command(name='serverinfo', aliases=['server', 'si'])
    @commands.guild_only()
    async def server_info(self, ctx):
        server = ctx.message.guild

        # Get number of language roles on the server
        

        # Get number of users without any roles on the server
        # Every user is implicitly in `@everyone`, which is why we check if `len(member.roles) == 1`
        roleless_user_count = len(list(filter(lambda member: len(member.roles) == 1, server.members)))

        

        bots= (len([m for m in ctx.guild.members if m.bot]))
        

        # TODO: Determine if guilds can be without a default channel
        default_channel = server.system_channel.mention if server.system_channel else text_lines['technical']['none']

        total_members = len(server.members)
        member_info = text_lines['server_info']['members_line'].format(total_members  - bots - roleless_user_count,
                                                                       roleless_user_count)

        emoji_count = len(server.emojis)
        # This is a string of *all* custom emojis in the server
        # Using map here is slightly faster than a list comprehension, but also looks a lot prettier
        emoji_preview = "".join(map(str, server.emojis))

        # Counts the number of text and voice channels in the server
        text_channel_count = len(list(filter(lambda channel: isinstance(channel, TextChannel), server.channels)))
        voice_channel_count = len(list(filter(lambda channel: isinstance(channel, VoiceChannel), server.channels)))
        channel_info = text_lines['server_info']['channel_line'].format(text_channel_count, voice_channel_count)

        # Create table for server info
        embed = discord.Embed(colour=discord.Colour(INFO_COLOR))
        embed.set_thumbnail(url=server.icon_url)
        embed.set_author(name=server.name, icon_url=server.icon_url)
        embed.add_field(name=text_lines['server_info']['titles']['id'],
                        value=server.id,
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['owner'],
                        value='Fifi Aboud ya ro7 omk',
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['created_at'],
                        value=server.created_at.strftime("%H:%M:%S at %d %b %Y"),
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['region'],
                        value=server.region,
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['channels'].format(voice_channel_count +
                                                                                    text_channel_count),
                        value=channel_info,
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['default_channel'],
                        value=default_channel,
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['roles'],
                        value="69(lmao)",
                        inline=True)
        embed.add_field(name=text_lines['server_info']['titles']['members'].format(total_members - bots),
                        value=member_info,
                        inline=True)

        # The max length for content in an embed is 1024 characters, and the minimum length is 1 character
        # If the emoji preview string is empty, or greater than 1024 characters, discord will reject our content
        # So, we only show emoji information if the preview string is within those bounds
        if 0 < len(emoji_preview) <= 1024:
            embed.add_field(name=text_lines['server_info']['titles']['emojis'].format(emoji_count),
                            value=emoji_preview)

        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(command(bot))






















