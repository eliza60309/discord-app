def run(bot):
	des = 'Leaves the voice channel'
	brf = 'Leaves the voice channel'
	als = ['Leave', 'disconnect', 'Disconnect']
	@bot.command(name = 'leave', description = des, brief = brf, pass_context = True, aliases = als)
	async def leave(context):
		import discord
		import keys
		import re
		if(context.author.id != int(keys.MASTER_ID)):
			await context.send('%s is not allowed to command on state secretary' % context.message.author.mention)
			print('[LOG] %s invoked !leave, forbidden' % context.message.author.name)
			return
		try:
			if(bot.get_guild(keys.SERVER_ID).voice_client != None):
				await bot.get_guild(keys.SERVER_ID).voice_client.disconnect()
			else:
				await discord.VoiceChannel.connect(bot.get_guild(keys.SERVER_ID).get_member(bot.user.id).voice.channel)
				await bot.get_guild(keys.SERVER_ID).voice_client.disconnect()
		except:
			await context.send('%s, where to leave?' % context.message.author.mention)
			print('[LOG] %s invoked !leave, nowhere to leave' % context.message.author.name)
			return
		print('[LOG] %s invoked !leave' % context.message.author.name)
