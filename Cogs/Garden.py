import discord
import json
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import os
import time
import sqlite3
from datetime import datetime

# import chalk

# method: __init__
# param: bot
# purpose: to initialize the bot object in this class
# return type: void
def __init__(self, bot):
    self.bot = bot


class Garden:
    # method: __init__
    # param: bot
    # purpose: initializes the bot for this class
    # return type: void
    def __init__(self, bot):
        self.bot = bot

    # method: groundSB
    # param: weight
    # purpose: enters in coffee grounds into the Coffee_Grounds Table for Starbucks
    # return type:
    @commands.command(pass_context=True)
    async def groundsSB(self, ctx, weight):
        self.runGroundsInsert(ctx, weight, "SB", "Starbucks'")

    # method: groundsPOD
    # param: weight
    # purpose: enters in coffee grounds into the Coffee_Grounds Table for Pod Building A
    # return type: void
    @commands.command(pass_context=True)
    async def groundsPOD(self, ctx, weight):
        self.runGroundsInsert(ctx, weight, "Pod", "Pod Building A")

    # method: groundsEB
    # param: weight
    # purpose: enters in coffee grounds into the Coffee_Grounds Table for Einsteins Bros Bagels
    # return type: void
    @commands.command(pass_context=True)
    async def groundsEB(self, ctx, weight):
        self.runGroundsInsert(ctx, weight, "EB", "Einstein's Brothers Bagels")

    # method: runGroundsInsert
    # param: ctx, weight, vendor, statement
    # purpose: streamlines the insert into the Coffee_Grounds Table
    # return type: void
    async def runGroundsInsert(self, ctx, weight, vendor, statement):
        # Create a database in RAM
        db = sqlite3.connect('../Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        cursor.execute(
            "INSERT INTO Coffee_Grounds (vendor, name, weight, drop_time, discord_id) VALUES (?,?,?,?,?)",
            (vendor, ctx.message.server.id, weight, datetime.now(), ctx.message.author.id))

        db.commit()
        db.close()
        await self.bot.say(
            "Inserted Grounds for " + statement + "Weight: " + weight + " Insert time is: " + datetime.now())


    # method: collectSB
    # param: none
    # purpose: collects and exports the Coffee_Grounds by csv
    # return type: void
    @commands.command(pass_context=True)
    async def collectSB(self, ctx):
        # Create a database in RAM
        db = sqlite3.connect('Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        potato = []
        conn = sqlite3.connect('Databases/Garden.db')
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM ' + "Coffee_Grounds"):
            potato.append(str(row))
        for x in potato:
            print(x)

        db.commit()
        db.close()

    # method:
    # param:
    # purpose:
    # return type:
    @commands.command(pass_context=True)
    async def SBGroundsPrint(self, ctx):
        await self.printList(await self.queryList("Weapons"))

    # method:
    # param:
    # purpose:
    # return type:
    async def queryList(self, tableQuery):
        potato = []
        conn = sqlite3.connect('Databases/Garden.db')
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM ' + tableQuery):
            potato.append(str(row))
        return potato

    # method:
    # param:
    # purpose:
    # return type:
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


# method: setup
# param: bot
# purpose: to link this cog to discordbot launcher
# return type: void
def setup(bot):
    bot.add_cog(Garden(bot))
    print('Garden Cog has been loaded.')
