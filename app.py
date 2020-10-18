import discord 
from discord.ext import commands
from magichome import MagicHomeApi
import datetime
import os

hostname = "192.168.1.205"

client = commands.Bot(command_prefix=">")

def check(num):
    if num<256 and num>-1:
        return True
    else:
        return False
    

@client.command()
async def uptime(ctx):
	with open('/proc/uptime','r') as f:
		uptimeSeconds=float(f.readline().split()[0])
		uptimeString=str(datetime.timedelta(seconds=uptimeSeconds))
	await ctx.send(uptimeString)
    
@client.command()
async def status(ctx):
    await ctx.send("Call it with >LED and provide the RGB colours. Simple eh? ie *>LED 255 255 255* ")
    
@client.command()
async def LED(ctx, arg, arg1, arg2):
	print("here")
	controller = MagicHomeApi(hostname, 0)
	#print(round(int(arg)), round(int(arg1)), round(int(arg2)))
	if(check(round(int(arg))) and check(round(int(arg1))) and check(round(int(arg2)))):
		controller.update_device(round(int(arg)), round(int(arg1)), round(int(arg2)))
		await ctx.send('Lights set!')
	else:
		await ctx.send('Errrr they aint rgb values? ')
  
@client.command()
async def online(ctx):
	response = os.system("ping -c 1 -w 5 -t 5 " + hostname)
	if response ==0:
		await ctx.send("Lights online")
	else:
		await ctx.send("Lights offline")
	




    
client.run(token)
