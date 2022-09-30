import discord
import random
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
intents.members = True

discord_bot = commands.Bot(command_prefix='!', intents=intents)


@discord_bot.event
async def on_ready():
    for guild in discord_bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{discord_bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    #message channel
    # channel = discord_bot.get_channel(704502327419076621)
    # await channel.send('KEK MY PEEPEE')

    # DM user
    # user = await client.fetch_user(638429509984583680)
    # await user.send('hey bb (; ')


@discord_bot.command(name='morningquote')
async def msg(ctx):
    quotes = [
        "It's a new day",
        (
            "Be positive"
        ),
    ]
    response = random.choice(quotes)
    await ctx.send(response)

@discord_bot.command(name='kmsquote')
async def msg(ctx):
    quotes = [
        "DO IT PUSSY",
    (
        "KEK"
    ),
    ]

    response = random.choice(quotes)
    await ctx.send(response)

@discord_bot.command(name='whoshere')
async def msg(ctx):
    voice_channel = discord_bot.get_channel(775501785103466527) #gets the text_channel you want to get the list from
    text_channel = discord_bot.get_channel(704502327419076621)

    members = voice_channel.members #finds members connected to the text_channel

    memids = [] #(list)
    for member in members:
        memids.append(member.id)

    print(memids) #print info

    await text_channel.send(memids)
    await ctx.send(response)

discord_bot.run(TOKEN)