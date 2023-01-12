import discord
import random
import os
import apscheduler

#async scheduler so it does not block other events
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from dotenv import load_dotenv
from discord.ext import commands
from helpers import *

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
intents.members = True

discord_bot = commands.Bot(command_prefix='!', intents=intents)

# set bot event listener
@discord_bot.event
async def on_ready():
    startup()
    sched()

# server info on startup of bot
def startup():
    # get guild name
    for guild in discord_bot.guilds:
        if guild.name == GUILD:
            break

    # print everyone online
    print(
        f'{discord_bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# 420 Listener
async def smonk_warning():
    smonk = discord_bot.get_channel(907710087857049661)
    await smonk.send("!! FIVE MINUTES UNTIL 420 !!")

# set and start scheduler
def sched():
    #initializing scheduler
    scheduler = AsyncIOScheduler()
    #sends "message" to the channel when time hits 10/20/30/40/50/60 seconds, like 12:04:20 PM
    scheduler.add_job(smonk_warning, CronTrigger(hour="15", minute="49", second="0"))
    #starting the scheduler
    scheduler.start()

# send nice moringquote
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

# when you stub your toe
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

# posts in bot-commands everyone in our voice channels
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
