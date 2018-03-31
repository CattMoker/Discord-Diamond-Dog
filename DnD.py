import discord
import json
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import os


# import chalk


def __init__(self, bot):
    self.bot = bot


class DnD:
    """Voice related commands.
    Works in multiple servers at once.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(pass_context=True)
    async def waterborne(self, ctx):
        from MasterEquipment.Implements import ImplementWaterborne
        newborne = ImplementWaterborne.ImplementWaterborne()
        newborne.readList()
        potato = []
        newborne.runList(potato)
        # wColumn = "Here's what I could find:\n Name \t Cost \t Weight \t Speed"
        wColumn = "Here's what I could find:"
        embed = discord.Embed(description=wColumn, color=0xff00ff)
        wName = ""
        wCost = ""
        wWeight = ""
        wSpeed = ""
        for x in potato:
            wName += x.getCategory() + "\n"
            wCost += x.getCost() + "\n"
            wWeight += x.getWeight() + "\n"
            wSpeed += x.getSpeed() + "\n"

        # embed.add_field(name="Name", value=wName, inline=False)
        embed.add_field(name="Name", value=wName, inline=True)
        embed.add_field(name="Cost", value=wCost, inline=True)
        embed.add_field(name="Weight", value=wWeight, inline=False)
        # embed.add_field(name="Speed", value=wSpeed, inline=False)
        # embed.add_field(name="Type of transport", value="potato", inline=True)
        toString = await self.bot.say(embed=embed)

        data = {'Waterborne': [{'toString': toString.clean_content}]}

    @commands.command(pass_context=True)
    async def charCreate(self, ctx):
        # Waits for user response and spits out a confirmation message (for testing)
        # await bot.say("Enter your character's name: ")
        await self.bot.send_message(ctx.message.author, "Enter your character's name: ")
        name = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's age: ")
        age = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author,
                                    "Enter your character's race: " + "\n\n" + "Dragonborn" + "\n" + "Dwarf" + "\n" + "Elf" + "\n" + "Gnome" + "\n" + "Half-Elf" + "\n" + "Half-Orc" + "\n" + "Halfling" + "\n" + "Human" + "\n" + "Tiefling" + "\n\n" + "If you would like to choose another race for your character not listed above, please enter it now!")
        race = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's class: ")
        charClass = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's alignment: ")
        alignment = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's height: ")
        height = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's weight: ")
        weight = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's hair color: ")
        hairColor = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's eye color: ")
        eyeColor = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "Enter your character's skin color: ")
        skinColor = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author,
                                    "We want to know more about your character. What's their backstory?")
        background = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "What are your character's traits?")
        traits = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "What are your character's ideals?")
        ideals = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "No one is without flaws. What are your character's?")
        flaws = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "What are your character's bonds?")
        bonds = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "What are your character's proficiencies?")
        proficiencies = await self.bot.wait_for_message(author=ctx.message.author, content=None)

        await self.bot.send_message(ctx.message.author, "All done, your character has been created.")

        # Writes response to JSON file
        data = {'Characters': [{'name': name.clean_content, 'age': age.clean_content, 'race': race.clean_content,
                                'class': charClass.clean_content, 'alignment': alignment.clean_content,
                                'height': height.clean_content, 'weight': weight.clean_content,
                                'hairColor': hairColor.clean_content, 'eyeColor': eyeColor.clean_content,
                                'skinColor': skinColor.clean_content, 'background': background.clean_content,
                                'traits': traits.clean_content, 'ideals': ideals.clean_content,
                                'flaws': flaws.clean_content, 'bonds': bonds.clean_content,
                                'proficiencies': proficiencies.clean_content}]}
        global loc
        with open(os.path.join(loc, 'dbTest.json'), 'a') as outfile:
            json.dump(data, outfile)

        # input(message.channel, message.content)


def setup(bot):
    bot.add_cog(DnD(bot))
    print('DnD Cog has been loaded.')
