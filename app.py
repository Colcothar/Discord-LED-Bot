import discord 
from discord.ext import commands
from magichome import MagicHomeApi
import datetime

hostname = "" #Ip of the LEDS
token = "" #Token of the discord bot

client = commands.Bot(command_prefix=">")

def check(num):
    if num<256 and num>-1:
        return True
    else:
        return False


@client.event
async def on_ready():
    print("Bot ready")
    
@client.command()
async def status(ctx):
    await ctx.send("@everyone If you hate the bot owner, change the colour of the lights in their room? \nCall it with >LED and provide the RGB colours. Simple eh? ie *>LED 255 255 255* ")
    
@client.command()
async def LED(ctx, arg, arg1, arg2):
    controller = MagicHomeApi(hostname, 0)
    print(round(int(arg)), round(int(arg1)), round(int(arg2)))
    if(check(round(int(arg))) and check(round(int(arg1))) and check(round(int(arg2)))):
        controller.update_device(round(int(arg)), round(int(arg1)), round(int(arg2)))
        await ctx.send('Lights set!')
    else:
         await ctx.send('They are not rgb values?')
  





    
client.run(token)
