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
    async def groundsSB(self, ctx):
        # Create a database in RAM
        db = sqlite3.connect('../Garden.db')
        # Creates or opens a file called mydb with a SQLite3 DB

        # Get a cursor object
        cursor = db.cursor()

        #######################IMPORTANT####################
        cursor.execute(
            "INSERT INTO Garden (vendor, name, weight, drop_time, discord_id) VALUES (?,?,?,?,?)",
            ("Starbucks", ctx.message.server.id, "19.21" + "lbs", datetime.now(), ctx.message.author.id))

        db.commit()
        db.close()


def setup(bot):
    bot.add_cog(Garden(bot))
    print('Tables Cog has been loaded.')
