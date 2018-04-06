import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio, os, sqlite3, random

# import chalk


def __init__(self, bot):
    self.bot = bot


class DnD:
    """Voice related commands.
    Works in multiple servers at once.
    """
    loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

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
    async def charCreate(self, ctx):
        # Waits for user response and spits out a confirmation message (for testing)
        # await bot.say("Enter your character's name: ")
        db = sqlite3.connect('../Discord-Diamond-Dog/Equipment.db')
        cursor = db.cursor()

        discId = ctx.message.author.id
        servId = ctx.message.server.id

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

        cursor.execute('''INSERT INTO Character (name, race, charClass, alignment, age, height, weight, hairColor, eyeColor, skinColor, background, traits, ideals, flaws, bonds, proficiencies, disc, serv) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (name.clean_content, race.clean_content, charClass.clean_content, alignment.clean_content,
                    age.clean_content, height.clean_content, weight.clean_content, hairColor.clean_content,
                    eyeColor.clean_content, skinColor.clean_content, background.clean_content, traits.clean_content,
                    ideals.clean_content, flaws.clean_content, bonds.clean_content, proficiencies.clean_content,
                    discId, servId))

        db.commit()
        db.close()

    @commands.command(pass_context=True)
    async def charList(self, ctx):
        db = sqlite3.connect('../Discord-Diamond-Dog/Equipment.db')
        cursor = db.cursor()
        table = "Character"
        col = "disc"
        discId = ctx.message.author.id

        for role in ctx.message.author.roles:
            if role.name != "Dungeon Master":
                cursor.execute('SELECT * FROM {tn} WHERE {cn}={cv}'. \
                  format(tn=table, cn=col, cv=discId))

            if role.name == "Dungeon Master":
                cursor.execute('SELECT * FROM {tn}'. \
                    format(tn=table))

            all_rows = cursor.fetchall()
            str1 = '\n'.join(''.join(str(x)) for x in all_rows)

        if (all_rows != []):
            await self.bot.send_message(ctx.message.author, "```" + str1 + "\n" + "```")
        if (all_rows == []):
            await self.bot.say ("Sorry, you don't have any characters. Create a new one with !charCreate.")



def setup(bot):
    bot.add_cog(DnD(bot))
    print('DnD Cog has been loaded.')
