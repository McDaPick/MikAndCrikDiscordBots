import discord
import random
import os

from dotenv import load_dotenv
from discord.ext import commands
from helpers import checkVoiceChannelforUsers

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

    list_of_channels = []

    # the text channel we want the bot to respond in
    bot_text_channel = discord_bot.get_channel(824498666781933589)

    # gets the voice_channel you want to get the list from
    video_gem_channel = discord_bot.get_channel(775501785103466527)
    civ_channel = discord_bot.get_channel(953034810408960000)
    hangout_space_channel = discord_bot.get_channel(704502327419076622)
    movie_stream_channel = discord_bot.get_channel(837476701780574208)

    # there is a better way to do this but I wanted to see if the concept worked
    list_of_channels.append(checkVoiceChannelforUsers(video_gem_channel))
    list_of_channels.append(checkVoiceChannelforUsers(civ_channel))
    list_of_channels.append(checkVoiceChannelforUsers(hangout_space_channel))
    list_of_channels.append(checkVoiceChannelforUsers(movie_stream_channel))

    # format string so that it looks nice in Discord
    members_in_voicechat = f"Video Gems : {*list_of_channels[0],} \n Civ : {*list_of_channels[1],} \n Hangout Space : {*list_of_channels[2],} \n Movie Stream : {*list_of_channels[3],} \n "

    await bot_text_channel.send(members_in_voicechat)

discord_bot.run(TOKEN)
