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
    async def armors(self, ctx):
        from MasterEquipment.Implements import ImplementArmor
        potato = ImplementArmor.armorList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def drawnVehicles(self, ctx):
        from MasterEquipment.Implements import ImplementDrawnVehicles
        potato = ImplementDrawnVehicles.drawnVehiclesList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def expenses(self, ctx):
        from MasterEquipment.Implements import ImplementExpenses
        potato = ImplementExpenses.LifeExpenses
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def FDLodging(self, ctx):
        from MasterEquipment.Implements import ImplementFDLodging
        potato = ImplementFDLodging.lodgingList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def mounts(self, ctx):
        from MasterEquipment.Implements import ImplementMounts
        potato = ImplementMounts.mountsList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def adventuringGear(self, ctx):
        from MasterEquipment.Implements import ImplementsAdventuringGear
        potato = ImplementsAdventuringGear.adventuringGear
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def services(self, ctx):
        from MasterEquipment.Implements import ImplementServices
        potato = ImplementServices.servicesList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def tools(self, ctx):
        from MasterEquipment.Implements import ImplementTools
        potato = ImplementTools.toolsList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def tradeGoods(self, ctx):
        from MasterEquipment.Implements import ImplementTradeGoods
        potato = ImplementTradeGoods.tradeGoodList
        await self.printList(potato)

    @commands.command(pass_context=True)
    async def trinkets(self, ctx):
        from MasterEquipment.Implements import ImplementTrinkets
        potato = ImplementTrinkets.trinketsList
        await self.printList(potato)

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
