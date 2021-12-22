#discord.py
import bot
import os
import json
from discord.ext.commands.core import check 
import requests
from dotenv import load_dotenv



from urllib.request import urlopen
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready( ):
    print ("Bot ready")

@client.command(help = "Find a summoner, type this and the summoners IGN to search.")
async def tester(ctx):
    await ctx.send("Im working")




client.run(TOKEN)