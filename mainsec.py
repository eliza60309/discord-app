import asyncio
from discord.ext.commands import Bot
import discord 
import discord.ext.commands as ext
import os

BOT_PREFIX = ('!')
bot = Bot(command_prefix = BOT_PREFIX)

from commands import hello
from commands import react
from commands import pewds
from commands import honey
from commands import payme
from commands import gambl
from commands import money
from commands import join
from commands import leave
from commands import cov19
from commands import lsuser
import discord_events
import keys

async def on_loop():
	await bot.wait_until_ready()
	hello.run(bot)
	pewds.run(bot)
	honey.run(bot)
	payme.run(bot)
	gambl.run(bot)
	money.run(bot)
	react.run(bot)
	join.run(bot)
	leave.run(bot)
	cov19.run(bot)
	lsuser.run(bot)

@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = '毛線'))
	print('[LOG] Logged in as ' + bot.user.name)
	print('[LOG] User ID: ' + str(bot.user.id))
	print('')
	discord_events.run(bot)

bot.loop.create_task(on_loop())
bot.run(keys.TOKEN)
