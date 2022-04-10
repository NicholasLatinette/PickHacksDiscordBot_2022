from email import message
import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks, commands
import random
import asyncio

random.seed()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

task = discord.ext.tasks

ready = True

lower_bound = 5
upper_bound = 20


bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message, lb=0, ub=0):
    channel = client.get_channel(962670927970201663)
    global lower_bound
    global upper_bound
    if message.author == client.user:
        return
    if message.content == '!time one':
        lower_bound = 5
        upper_bound = 20
        
        await channel.send('Posture checks will now be between 5 and 20 seconds. *not reccomended*')
    elif message.content == '!time two':
        lower_bound = 100
        upper_bound = 2000
        
        await channel.send('Posture checks will now be between 100 and 2000 seconds.')
    elif message.content == '!time three':
        lower_bound = 300
        upper_bound = 12000
        
        await channel.send('Posture checks will now be between 400 and 12000 seconds.')
   
    elif message.content == '!help':
        await channel.send('Configure when you get pinged by Posture Bot.\n!time one: 5 seconds to 20 seconds\n!time two: 100 secs to 2000 secs\n!time three: 400 secs to 12000 secs')    

    

@task.loop(seconds=random.randrange(lower_bound,upper_bound))
async def time():
    channel = client.get_channel(962670927970201663)
    await channel.send('@everyone Posture check!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    if ready == True:
        await time.start()
    print("not test")



client.run(TOKEN)



