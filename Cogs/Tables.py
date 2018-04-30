import discord
import json
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import os
import sqlite3

# import chalk


def __init__(self, bot):
    self.bot = bot


class Tables:
    # method: __init__
    # param: bot
    # purpose: initializes the bot
    # return type: void
    def __init__(self, bot):
        self.bot = bot

    # method: armors
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def armors(self, ctx):
        await self.printList(await self.queryList("Armor"))

    # method: drawnVehicles
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def drawnVehicles(self, ctx):
        await self.printList(await self.queryList("DrawnVehicles"))

    # method: expenses
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def expenses(self, ctx):
        await self.printList(await self.queryList("Expenses"))

    # method: FDLodging
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def FDLodging(self, ctx):
        await self.printList(await self.queryList("FDLodging"))

    # method: mounts
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def mounts(self, ctx):
        await self.printList(await self.queryList("Mounts"))

    # method: adventuringGear
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def adventuringGear(self, ctx):
        await self.printList(await self.queryList("AdventuringGear"))

    # method: services
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def services(self, ctx):
        await self.printList(await self.queryList("Services"))

    # method: tools
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def tools(self, ctx):
        await self.printList(await self.queryList("Tools"))

    # method: tradeGoods
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def tradeGoods(self, ctx):
        await self.printList(await self.queryList("TradeGoods"))

    # method: trinkets
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def trinkets(self, ctx):
        await self.printList(await self.queryList("Trinkets"))

    # method: waterborne
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def waterborne(self, ctx):
        await self.printList(await self.queryList("Waterborne"))

    # method: weapons
    # param: none
    # purpose: queries from the equipment database and prints a table to discord
    # return type: void
    @commands.command(pass_context=True)
    async def weapons(self, ctx):
        await self.printList(await self.queryList("Weapons"))

    # method: queryList
    # param: none
    # purpose: this method helps the query from a database
    # return type: array
    async def queryList(self, tableQuery):
        potato = []
        conn = sqlite3.connect('Databases/Equipment.db')
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM ' + tableQuery):
            potato.append(str(row))
        return potato

    # method: printList
    # param: potato: array
    # purpose: this method assists the queryList method in printing all of that to discord
    # return type: void
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
                    wFormat += "```" + potato[x] + "```"
                else:
                    endList = True
            await self.bot.say(wFormat)
            rangeBot += 4
            rangeTop += 4
        await self.bot.say("End of Table Reached")

    # method: printList2
    # param: potato: array
    # purpose:
    # return type: void
    async def printList2(self, potato):
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

# method: setup
# param: bot
# purpose: to link the bot to the original launcher
# return type: void
def setup(bot):
    bot.add_cog(Tables(bot))
    print('Tables Cog has been loaded.')
