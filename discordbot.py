# StartBot by the Alcoholicorn
# essential package imports
import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
#import chalk


# packages that I decided to import
import random

# what the bot is listening for
bot = commands.Bot(command_prefix="!")

# where out lists are declared
sList = []
with open('C://Users//Eroc//Documents//ggc//Discord-Diamond-Dog//supportList.txt') as supportFile:
    for line in supportFile:
        sList.append(line)

mList = []
mList.append("")

@bot.event
async def on_ready():
	print ("Ret to go")
	print ("I am running on" + bot.user.name)
	print ("With the ID: "  + bot.user.id)
	
@bot.command(pass_context=True)
async def ping(ctx):
	"""To check if the bot is alive"""
	await bot.say(":ping_pong: ***SCREEEEEEEEEEEEECH***")
	print ("user has pinged")	
	
@bot.command(pass_context=True)
async def speak(ctx):
	"""To make bot speak"""
	await bot.say("<:reinbark:384084080578396160> *bork bork*")
	#await bot.say('Bork', tts=True)
	print ("bot has spoken")
	
@bot.command(pass_context=True)
async def pet(ctx):
	await bot.say(":heart::heart::heart: <:reinbark:384084080578396160> <:reinbark:384084080578396160>'wags tail enthusiastically'<:reinbark:384084080578396160> <:reinbark:384084080578396160>:heart::heart::heart:")

###################################################THIS IS THE SAMPLE CODE TO READ THE JSON FILE####################################################################
@bot.command(pass_context=True)
async def test(ctx):
	with open('C:/Users/jz326/Desktop/discord code/Discord-Diamond-Dog-master/Character/dbTest.json') as json_data:
		d = json.load(json_data)
		await bot.say(d['employees'][2]['firstName']) #Have to reference 

###########################################################################################################################################################

###################################################CHARACTER CREATION####################################################################
@bot.command(pass_context=True)
async def charCreate(ctx):

    # Waits for user response and spits out a confirmation message (for testing)
    # await bot.say("Enter your character's name: ")
    await bot.send_message(ctx.message.author, "Enter your character's name: ")
    name = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's age: ")
    age = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's race: " + "\n\n" + "Dragonborn" + "\n" + "Dwarf" + "\n" + "Elf" + "\n" + "Gnome" + "\n" + "Half-Elf" + "\n" + "Half-Orc" + "\n" + "Halfling" + "\n" + "Human" + "\n" + "Tiefling" + "\n\n" + "If you would like to choose another race for your character not listed above, please enter it now!") 
    race = await bot.wait_for_message(author=ctx.message.author, content=None)
   
    await bot.send_message(ctx.message.author, "Enter your character's class: ")
    charClass = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's alignment: ")
    alignment = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's height: ")
    height = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's weight: ")
    weight = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's hair color: ")
    hairColor = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's eye color: ")
    eyeColor = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "Enter your character's skin color: ")
    skinColor = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "We want to know more about your character. What's their backstory?")
    background = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "What are your character's traits?")
    traits = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "What are your character's ideals?")
    ideals = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "No one is without flaws. What are your character's?")
    flaws = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "What are your character's bonds?")
    bonds = await bot.wait_for_message(author=ctx.message.author, content=None)

    await bot.send_message(ctx.message.author, "What are your character's proficiencies?")
    proficiencies = await bot.wait_for_message(author=ctx.message.author, content=None)
    
    await bot.send_message(ctx.message.author, "All done, your character has been created.")

    # Writes response to JSON file
    data = {'Characters':[{'name': name.clean_content, 'age': age.clean_content, 'race': race.clean_content, 'class': charClass.clean_content, 'alignment': alignment.clean_content, 'height': height.clean_content, 'weight': weight.clean_content, 'hairColor': hairColor.clean_content, 'eyeColor': eyeColor.clean_content, 'skinColor': skinColor.clean_content, 'background': background.clean_content, 'traits': traits.clean_content, 'ideals': ideals.clean_content, 'flaws': flaws.clean_content, 'bonds': bonds.clean_content, 'proficiencies': proficiencies.clean_content}]}
    global loc
    loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(loc, 'dbTest.json'), 'a') as outfile:
      json.dump(data, outfile)
    
    #input(message.channel, message.content)

#########################################################################################################################################


@bot.command(pass_context=True)
async def support(ctx):
	'''Support Lines Yo'''
	await bot.say(sList[random.randint(0, len(sList) - 1)])
	
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	"""Retrieves info on a user"""
	embed = discord.Embed(title="{}'s info".format(user.name), description = "Here's what I could find.", color=0xff00ff)
	embed.add_field(name = "Name", value = user.name, inline = True)
	embed.add_field(name = "ID", value = user.id, inline = True)
	embed.add_field(name = "Status", value = user.status, inline = True)
	embed.add_field(name = "Highest Role", value = user.top_role, inline = True)
	embed.add_field(name = "Joined", value = user.joined_at, inline = True)
	embed.set_thumbnail(url = user.avatar_url)
	# await bot.say("The users name: {}".format(user.name))
	# await bot.say("The users ID is: {}".format(user.id))
	# await bot.say("The users status is: {}".format(user.status))
	# await bot.say("The users highest role is: {}".format(user.top_role))
	# await bot.say("The user joined at: {}".format(user.joined_at))
	await bot.say(embed = embed)
	
@bot.command(pass_context=True)
async def serverinfo(ctx):
	"""Displays server info"""
	embed = discord.Embed(name = "{}'s info".format(ctx.message.server), description = "Here's ur server info.", color = 0x00ff00)
	embed.set_author(name = "Coker")
	embed.add_field(name = "Name", value = ctx.message.server.name, inline = True)
	embed.add_field(name = "ID", value = ctx.message.server.id, inline = True)
	embed.add_field(name = "Roles", value = len(ctx.message.server.roles), inline = True)
	embed.add_field(name = "Members", value = len(ctx.message.server.members))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)	


@bot.command(pass_context=True)
@commands.has_role("On the TAP")
async def kick(ctx, user: discord.Member):
	await bot.say(":boot: {}. See ya heathen!".format(user.name))
	await bot.kick(user)

	
	

@bot.command(pass_context=True)
#@commands.has_role("On the TAP")
async def hello(ctx):
	await bot.say("/tts hello")

@bot.command(pass_context=True)
async def embed(ctx):
	embed = discord.Embed(title="test", description="my name Coker", color=0x00ff00)
	embed.set_footer(text = "this is a footer")
	embed.set_author(name = "Coker of Alcoholicorn Productions")
	embed.set_field(name = "This is a field", value = "no it isn't", inline = True)
	await bot.say(embed=embed)

	
@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

# This is where the authentication token is inserted
text_file = open("C://Users//Eroc//Documents//ggc//Discord-Diamond-Dog//authToken.txt", "r")
#lines = text_file.readlines()
token = text_file.readline()
text_file.close()

bot.run(token)