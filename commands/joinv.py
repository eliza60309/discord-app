def run(bot):
	des = 'Joins the voice channel'
	brf = 'Joins the voice channel'
	als = ['join', 'Join']
	@bot.command(name = 'joinv', description = des, brief = brf, pass_context = True, aliases = als)
	async def joinv(context):
		import discord
		import keys
		import re
		if(context.author.id != int(keys.MASTER_ID)):
			await context.send('%s is not allowed to command on state secretary' % context.message.author.mention)
			print('[LOG] %s invoked !joinv, forbidden' % context.message.author.name)
			return
		arr = list(map(int, re.findall('\d+', context.message.content)))
		member = bot.get_guild(keys.SERVER_ID).get_member(context.message.author.id)
		bot_member = bot.get_guild(keys.SERVER_ID).get_member(bot.user.id)
		try:
			join_id = member.voice.channel.id
			if(len(arr) != 0):
				join_id = arr[0]
			channel = bot.get_guild(keys.SERVER_ID).get_channel(join_id)
			if(bot.get_guild(keys.SERVER_ID).voice_client != None):
				await bot.get_guild(keys.SERVER_ID).voice_client.move_to(channel)
			else:
				await discord.VoiceChannel.connect(channel)
		except:
			await context.send('%s, where to join?' % context.message.author.mention)
			print('[LOG] %s invoked !joinv, nowhere to join' % context.message.author.name)
			return
		print('[LOG] %s invoked !joinv' % context.message.author.name)
