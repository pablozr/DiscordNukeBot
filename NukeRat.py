import discord
from discord.ext import commands

token = "Put Your Bot Token Here"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', case_insensitive= True, help_command=None, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Its me"))
    print("""
        
             _..----.._    _
            .'  .--.    "-.(0)_
'-.__.-'"'=:|   ,  _)_ \__ . c\'-..
             '''------'---''---'-"
    
    [*] Online
    """ + f'[*] Logged as: {bot.user}')

@bot.command(pass_context=True, aliases=["n"])
@commands.has_permissions(administrator = True)
async def nuke(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()
    await ctx.guild.create_text_channel(name='chat')
    await ctx.guild.create_voice_channel(name='voice')

bot.run(token)    