# StartBot by the Alcoholicorn
# essential package imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

# packages that I decided to import
import random

# what the bot is listening for
bot = commands.Bot(command_prefix="!")

# where out lists are declared
sList = []
sList.append("No matter who or what you support, I believe in supporting fairness first.")
sList.append("We can't help everyone, but everyone can help someone.")
sList.append("Encourage, lift and strengthen one another. For the positive energy spread to one will be felt by us all. For we are connected, one and all.")
sList.append("If you want to support others you have to stay upright yourself.")
sList.append("Your small support could accomplish a big dream.")
sList.append("He stands erect by bending over the fallen. He rises by lifting others.")
sList.append("It is a kingly act to assist the fallen.")
sList.append("It is an eternal obligation toward the human being not to let him suffer from hunger when one has a chance of coming to his assistance.")
sList.append("Never reach out your hand unless you're willing to extend an arm.")
sList.append("To keep a lamp burning we have to keep putting oil in it.")
sList.append("When a person is down in the world, an ounce of help is better than a pound of preaching.")
sList.append("The truest help we can render an afflicted man is not to take his burden from him, but to call out his best energy, that he may be able to bear the burden.")
sList.append("If you have much, give of your wealth; if you have little, give of your heart.")
sList.append("Support the strong, give courage to the timid, remind the indifferent, and warn the opposed.")
sList.append("Make a habit of two things: to help; or at least to do no harm.")
sList.append("Help others achieve their dreams and you will achieve yours.")
sList.append("Our prime purpose in this life is to help others. And if you can't help them, at least don't hurt them.")
sList.append("Sometimes the only thing you could do for people was to be there.")
sList.append("Helping others isn't a chore; it is one of the greatest gifts there is.")
sList.append("Helping someone is what life is all about.")
sList.append("Support the sick, but not the idle.")
sList.append("To give aid to every poor man is far beyond the reach and power of every man. Care of the poor is incumbent on society as a whole.")
sList.append("To aid life, leaving it free, however, that is the basic task of the educator.")
sList.append("Helping people getting a great start in life, a great foundation, is an investment.")
sList.append("Give, but give until it hurts.")
sList.append("No act of kindness, no matter how small, is ever wasted.")
sList.append("Look up and not down. Look forward and not back. Look out and not in, and lend a hand.")
sList.append("Never look down on anybody unless you helping him up.")
sList.append("When you cease to make a contribution, you begin to die.")
sList.append("Kind words can be short and easy to speak, but their echoes are truly endless.")

sList.append("Everybody can be great...because anybody can serve. You don't have to have a college degree to serve. You don't have to make your subject and verb agree to serve. You only need a heart full of grace. A soul generated by love.")
sList.append("You give but little when you give of your possessions. It is when you give of yourself that you truly give.")
sList.append("I am only one, but still I am one. I cannot do everything, but still I can do something; and because I cannot do everything, I will not refuse to do something I can do.")
sList.append("The greatest good you can do for another is not just share your riches, but reveal to them their own. ")
sList.append("No one can whistle a symphony. It takes a whole orchestra to play it.")
sList.append("It takes community to maintain a human.")
sList.append("It is not enough to help the feeble up, but to support him after.")
sList.append("Help one another; there's no time like the present and no present like the time.")
sList.append("A friend is the one who comes in when the whole world has gone out.")
sList.append("Never worry about numbers. Help one person at a time, and always start with the person nearest you.")
sList.append("No one is useless in this world who lightens the burdens of another.")
sList.append("If you're in the luckiest one per cent of humanity, you owe it to the rest of humanity to think about the other 99 per cent.")
sList.append("It is literally true that you can succeed best and quickest by helping others to succeed.")
sList.append("The best way to find yourself is to lose yourself in the service of others.")
sList.append("There is no use whatever trying to help people who do not help themselves. You cannot push anyone up a ladder unless he is willing to climb himself.")
sList.append("You can have everything you want in life if you just help enough people get what they want in life.")
sList.append("Life's most urgent questions is: What are you doing for others'")
sList.append("Those who are happiest are those who do the most for others.")
sList.append("Doing nothing for others is the undoing of ourselves.")
sList.append("There is no exercise better for the heart than reaching down and lifting people up.")

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
bot.run("")