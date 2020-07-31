def run(bot):
	des = 'List all user and their user id'
	brf = 'List all user and their user id'
	als = ['ls', 'list']
	@bot.command(name = 'lsuser', description = des, brief = brf, pass_context = True, aliases = als)
	async def lsuser(context):
		import keys
		if(context.author.id != int(keys.MASTER_ID)):
			await context.send('%s is not allowed to list all user' % context.message.author.mention)
			print('[LOG] %s invoked !ls, forbidden' % context.message.author.name)
			return
		for i in bot.get_guild(keys.SERVER_ID).members:
			print(i.name, i.id)
		await context.send('Done!')	
