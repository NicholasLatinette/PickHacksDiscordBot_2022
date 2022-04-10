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

time_chosen = 0
ready = True

def choose_time():
    time_chosen = 5.0
    #time = random.randrange(2400, 12000, 200)
    return time_chosen
    ready = False


@task.loop(seconds=10)
async def time():
    channel = client.get_channel(962122924893040714)
    await channel.send('@Pcheckers Posture check!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    if ready == True:
        time_chosen = choose_time()
        await time.start()
    print("not test")


    
client.run(TOKEN)



