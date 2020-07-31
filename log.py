import asyncio
from discord.ext.commands import Bot
import discord 
import discord.ext.commands as ext
import os

BOT_PREFIX = ('!')
bot = Bot(command_prefix = BOT_PREFIX)

import keys


@bot.event
async def on_ready():
	print('[LOG] Logged in as ' + bot.user.name)
	print('[LOG] User ID: ' + str(bot.user.id))
	print('')
	#await bot.get_user(keys.MASTER_ID).create_dm()
	#dm = bot.get_user(keys.MASTER_ID).dm_channel
	#async for i in dm.history():
	#	print(i.content)
	for channel in bot.private_channels:
		print(channel.recipient.name)

@bot.event
async def on_message(message):
	if(isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user):
		print(message.author.name + ': ' + message.content)
		if(bot.get_user(keys.MASTER_ID).dm_channel == None):
			await bot.get_user(keys.MASTER_ID).create_dm()
		await bot.get_user(keys.MASTER_ID).dm_channel.send(message.author.name + ': ' + message.content)



	
bot.run(keys.TOKEN)
