import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice()
    with open(f'images/mem1.jpeg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def animals(ctx):
    images = os.listdir('images')
    img_name = random.choice()
    with open(f'images/kot1.png', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run("token")