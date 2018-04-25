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

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def armors(self, ctx):
        await self.printList(await self.queryList("Armor"))

    @commands.command(pass_context=True)
    async def drawnVehicles(self, ctx):
        await self.printList(await self.queryList("DrawnVehicles"))

    @commands.command(pass_context=True)
    async def expenses(self, ctx):
        await self.printList(await self.queryList("Expenses"))

    @commands.command(pass_context=True)
    async def FDLodging(self, ctx):
        await self.printList(await self.queryList("FDLodging"))

    @commands.command(pass_context=True)
    async def mounts(self, ctx):
        await self.printList(await self.queryList("Mounts"))

    @commands.command(pass_context=True)
    async def adventuringGear(self, ctx):
        await self.printList(await self.queryList("AdventuringGear"))

    @commands.command(pass_context=True)
    async def services(self, ctx):
        await self.printList(await self.queryList("Services"))

    @commands.command(pass_context=True)
    async def tools(self, ctx):
        await self.printList(await self.queryList("Tools"))

    @commands.command(pass_context=True)
    async def tradeGoods(self, ctx):
        await self.printList(await self.queryList("TradeGoods"))

    @commands.command(pass_context=True)
    async def trinkets(self, ctx):
        await self.printList(await self.queryList("Trinkets"))

    @commands.command(pass_context=True)
    async def waterborne(self, ctx):
        await self.printList(await self.queryList("Waterborne"))

    @commands.command(pass_context=True)
    async def weapons(self, ctx):
        await self.printList(await self.queryList("Weapons"))

    async def queryList(self, tableQuery):
        potato = []
        conn = sqlite3.connect('../Databases/Equipment.db')
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM ' + tableQuery):
            potato.append(str(row))
        return potato

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


def setup(bot):
    bot.add_cog(Tables(bot))
    print('Tables Cog has been loaded.')
