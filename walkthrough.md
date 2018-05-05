#The Diamond Dog Project#

Thank you for your interest in our project. Please follow these rules so that you can use it!  

But first, **make sure you have a group server where you can put in your bot**!

##Installing Python##

1. One of the biggest things you need to use this project is Python. 
2. That can be done by downloading the most current Python from this link: https://www.python.org/downloads/
3. Follow the instructions until completion.

##Cloning the Repository##
1. If you don't have Git installed, please download / install it from this link: https://git-scm.com/downloads
2. Then once complete, run it and enter the following: 'git clone https://github.com/TheRealAlcoholicorn/Discord-Diamond-Dog.git' (Minus the single quotes).
**This will clone everything from our repo onto your computer. Just search Discord-Diamond-Dog on your computer**


##Importing the Packages##

1. On the IDE of your choice, open the 'discordbot.py' file from our GitHub (We suggest using PyCharm because it's Python based).
2. Once downloaded, type in the command line these following commands. They will import the necessary libraries for you:

    - import discord
    - from discord.ext import commands
    - from discord.ext.commands import Bot
    - from discord.voice_client import VoiceClient
    - import asyncio
    - import threading, time, os, json

3. Once all of that is installed, please continue to the next steps.

##Making the Bot##

1. Go to the following link: -	https://discordapp.com/developers/docs/intro
2. Click on 'Make a New App' and pick 'My Apps' on the left side
3. Name the bot whatever you want. You can even add a description and picture if you'd like! Click 'Create App' when you're ready. You will now reach a page that says 'Great Success'.
4. Copy the Client ID from the 'Great Success' page and go to: https://discordapp.com/oauth2/authorize?&client_id=CLIENT_ID_HERE&scope=bot&permissions=470019135
5. Delete where it says CLIENT_ID_HERE and paste your copied client ID and click enter. 
6. There will now be an option to pick which server you want your bot to be in. Choose your preferred server and you're almost done!

##Auth Token - IMPORTANT INSTRUCTIONS##
1. Go back to https://discordapp.com/developers/docs/intro and go to your bot
2. On this page, scroll down until you see Token under the bot section. Click it and it will reveal your SPECIFIC token! **DO NOT SHARE WITH ANYONE!!**
3. In the folder you have Discord-Diamond-Dog cloned, make a new text file called 'authToken.txt' and copy that code & save. 


YOU ARE NOW READY TO PLAY!