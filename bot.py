import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
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



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!time one':
        lower_bound = 5
        upper_bound = 20
    elif message.content == '!time two':
        lower_bound = 100
        upper_bound = 2000
    elif message.content == '!time three':
        lower_bound = 400
        upper_bound = 12000
    elif message.content == '!help':
        channel = client.get_channel(962670927970201663)
        await channel.send('!time one: 5 seconds to 20 seconds\n!time two: 100 secs to 2000 secs\n!time three: 400 secs to 12000 secs')
    

@task.loop(seconds=random.randrange(lower_bound,upper_bound,2))
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



