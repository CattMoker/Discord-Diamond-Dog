# StartBot by the Alcoholicorn
# essential package imports
from datetime import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import threading, time, os, json

# packages that I decided to import
import random

# what the bot is listening for
startup_extensions = ["Cogs.Music", "Cogs.DnD", "Cogs.Tables", "Cogs.Garden"]
bot = commands.Bot(command_prefix="!")

loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# where out lists are declared
sList = []
with open(os.path.join(loc, 'supportList.txt')) as supportFile:
    for line in supportFile:
        sList.append(line)

mList = []
mList.append("")

#import binascii
#filename = 'test.jpg'
#ith open(filename, 'rb') as f:
#    content = f.read()
#print(binascii.hexlify(content))

# method: on_ready
# param: none
# purpose: meant to print out to the console with standard identification
# return type: void
@bot.event
async def on_ready():
    print("Ret to go")
    print("I am running on" + bot.user.name)
    print("With the ID: " + bot.user.id)

# method: ping
# param: none
# purpose: the user will call this command to ping the bot to make sure its working
# return type: void
@bot.command(pass_context=True)
async def ping(ctx):
    """To check if the bot is alive"""
    await bot.say(":ping_pong: ***SCREEEEEEEEEEEEECH***")
    print("user has pinged")

# method: speak
# param: none
# purpose: to make the bot bark
# return type: void
@bot.command(pass_context=True)
async def speak(ctx):
    """To make bot speak"""
    await bot.say("<:reinbark:384084080578396160> *bork bork*")
    # await bot.say('Bork', tts=True)
    print("bot has spoken")

# method: pet
# param: none
# purpose: a response to the bot being called upon the pet command
# return type: void
@bot.command(pass_context=True)
async def pet(ctx):
    await bot.say(
        ":heart::heart::heart: <:reinbark:384084080578396160> <:reinbark:384084080578396160>'wags tail enthusiastically'<:reinbark:384084080578396160> <:reinbark:384084080578396160>:heart::heart::heart:")


###################################################THIS IS THE SAMPLE CODE TO READ THE JSON FILE####################################################################
@bot.command(pass_context=True)
async def test(ctx):
    with open('C:/Users/jz326/Desktop/discord code/Discord-Diamond-Dog-master/Character/dbTest.json') as json_data:
        d = json.load(json_data)
        await bot.say(d['employees'][2]['firstName'])  # Have to reference


###########################################################################################################################################################

###################################################CHARACTER CREATION####################################################################


#########################################################################################################################################


######################################################### AUDIO MEDIC ###################################################################

# For loading cogs (essentially allowing the main file to access other files)
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))


#########################################################################################################################################

# method: support
# param: empty
# purpose: calls upon a local txt file that holds all the supportive lines in times of stress
# return type: void
@bot.command(pass_context=True)
async def support(ctx):
    '''Support Lines Yo'''
    await bot.say(sList[random.randint(0, len(sList) - 1)])

# method: info
# param: user: discord.Member
# purpose: gathers info on any user in the user's server
# return type: void
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """Retrieves info on a user"""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xff00ff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    # await bot.say("The users name: {}".format(user.name))
    # await bot.say("The users ID is: {}".format(user.id))
    # await bot.say("The users status is: {}".format(user.status))
    # await bot.say("The users highest role is: {}".format(user.top_role))
    # await bot.say("The user joined at: {}".format(user.joined_at))
    await bot.say(embed=embed)

# method: serverinfo
# param: none
# purpose: retrieves info on the user's server
# return type: void
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server info"""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server), description="Here's ur server info.",
                          color=0x00ff00)
    embed.set_author(name="Coker")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

# method: kick
# param: user: discord.Member
# purpose: to kick another member from the server,
# return type: void
@bot.command(pass_context=True)
@commands.has_role("On the TAP")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {}. See ya heathen!".format(user.name))
    await bot.kick(user)

# method: hello
# param: none
# purpose: the bot texts-to-speech hello
# return type: void
@bot.command(pass_context=True)
# @commands.has_role("On the TAP")
async def hello(ctx):
    await bot.say("/tts hello")

# method: embed
# param: none
# purpose: to send an embed of the first author's info in a very not fashion
# return type: void
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name Coker", color=0x00ff00)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Coker of Alcoholicorn Productions")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

# method: dateCall
# param: none
# purpose: this calls upon the birthdays.txt file, checks every 12 hours for the list
# return type: void
@bot.command(pass_context=True)
async def dateCall():
    potato = True
    with open("birthdays.txt") as f:
        content = f.readlines()
    birthdayList = []
    for x in content:
        birthdayList.append(x.split())

    while potato:

        for x in birthdayList:

            personDate = datetime(datetime.now().year, int(x[1]), int(x[2]))
            todayDate = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
            print("personMonth: " + str(personDate.month) + " personDay: " + str(personDate.day))
            print("todayMonth: " + str(todayDate.month) + " todayDay: " + str(todayDate.day))
            if personDate.month == todayDate.month and personDate.day == todayDate.day:
                try:
                    {
                        await bot.say("Happy Birthday <@" + x[3] + ">")
                    }
                except Exception as e:
                    {
                        e.with_traceback()
                    }

        await asyncio.sleep(43200)


# This is where the authentication token is inserted
text_file = open(os.path.join(loc, "authToken.txt"), "r")
# lines = text_file.readlines()
token = text_file.readline().strip()
text_file.close()

bot.run(token)
