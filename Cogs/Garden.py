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


def __init__(self, bot):
    self.bot = bot


class Garden:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def groundsSB(self, ctx, weight):
        # Create a database in RAM
        db = sqlite3.connect('../Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        cursor.execute(
            "INSERT INTO Coffee_Grounds (vendor, name, weight, drop_time, discord_id) VALUES (?,?,?,?,?)",
            ("Starbucks", ctx.message.server.id, weight, datetime.now(), ctx.message.author.id))

        db.commit()
        db.close()
        await self.bot.say(
            "Inserted Grounds for Starbucks Weight: " + weight + " Insert time is: " + str(datetime.now()))

    @commands.command(pass_context=True)
    async def groundsPOD(self, ctx, weight):
        # Create a database in RAM
        db = sqlite3.connect('../Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        cursor.execute(
            "INSERT INTO Coffee_Grounds (vendor, name, weight, drop_time, discord_id) VALUES (?,?,?,?,?)",
            ("Pod Building A", ctx.message.server.id, weight, datetime.now(), ctx.message.author.id))

        db.commit()
        db.close()
        await self.bot.say(
            "Inserted Grounds for Pod Building A Weight: " + weight + " Insert time is: " + datetime.now())

    @commands.command(pass_context=True)
    async def groundsEB(self, ctx, weight):
        # Create a database in RAM
        db = sqlite3.connect('../Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        cursor.execute(
            "INSERT INTO Coffee_Grounds (vendor, name, weight, drop_time, discord_id) VALUES (?,?,?,?,?)",
            ("Einstein's Brothers Bagels", ctx.message.server.id, weight, datetime.now(), ctx.message.author.id))

        db.commit()
        db.close()
        await self.bot.say(
            "Inserted Grounds for Einstein's Brothers Bagels Weight: " + weight + " Insert time is: " + datetime.now())

    @commands.command(pass_context=True)
    async def collectSB(self, ctx):
        # Create a database in RAM
        db = sqlite3.connect('../Databases/Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        potato = []
        conn = sqlite3.connect('../Databases/Garden.db')
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM ' + "Coffee_Grounds"):
            potato.append(str(row))
        for x in potato:
            print(x)

        db.commit()
        db.close()



def setup(bot):
    bot.add_cog(Garden(bot))
    print('Garden Cog has been loaded.')
