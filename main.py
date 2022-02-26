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
    key =KEY ;
    content = requests.get(f"http://api.giphy.com/v1/gifs/random?api_key={key}&limit=1").text
    data = json.loads(content)
    gif = discord.Embed(Color = discord.Color.random()).set_image(url=data["data"]["images"]["fixed_height_downsampled"]["url"])
    await ctx.reply(embed=gif)
my_secret = os.environ['TOKEN'] # .env file i which the TOKEN consists of token

alive()
client.run(my_secret)  