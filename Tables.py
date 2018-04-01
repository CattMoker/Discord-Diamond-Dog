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


class Tables:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def waterborne(self, ctx):
        from MasterEquipment.Implements import ImplementWaterborne
        potato = ImplementWaterborne.waterborneList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def weapons(self, ctx):
        from MasterEquipment.Implements import ImplementWeapons
        potato = ImplementWeapons.weaponList
        await self.printList(potato)

    async def printList(self, potato):
        wColumn = "Here's what I could find:"
        await self.bot.say(wColumn)
        rangeBot = 0
        rangeTop = 4
        endList = False
        while not endList:
            wFormat = ""
            for x in range(rangeBot, rangeTop):
                if x < potato.__len__():
                    wFormat += "```" + potato[x].botMessage() + "```"
                else:
                    endList = True
            await self.bot.say(wFormat)
            rangeBot += 4
            rangeTop += 4
        await self.bot.say("End of Table Reached")


def setup(bot):
    bot.add_cog(Tables(bot))
    print('Tables Cog has been loaded.')
