import discord;
from discord.ext import commands;
import requests;
import json;
import os;
from alive import alive;


client = commands.Bot(command_prefix="#")
@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")
@client.command()   # below the name of the function will be the name which we need to write after command_prefix in discord in order to make that function work
async def gif(ctx):  # need to add ctx parameter for ctx.reply         
# Since it is a async function we need to add it under client.command
    content = requests.get("api.giphy.com/v1/gifs/search").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)
my_secret = os.environ['TOKEN'] # .env file i which the TOKEN consists of token

alive()
client.run(my_secret)  