import discord
from discord.ext  import commands

class  say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command("on_message")
    async def say(self, message:discord.Message):
        """Looks for swearing in the message and tells people off"""
        if message.author.bot:
            return
        if message.content.lower() == 'tea':
            await message.delete()
            await message.channel.send('Drink And Pee!')





    @client.event
    async def on_member_join(member):
    mention = member.mention
    print(f'{member} has joined')
    channel = discord.utils.get(member.guild.channels, name="welcome")
    ch = client.get_channel(705510105285787728)
    ch2 = client.get_channel(705771335174979634)

    await channel.send(f"""Welcome to the Cathedral of Coffee {member.mention}! Please read the rules at {ch.mention} and go to {ch2.mention} in order to gain access to the rest of the server.
    Enjoy your stay!""")
                
                
            

    
        

       


def setup(bot):
    bot.add_cog(say(bot))