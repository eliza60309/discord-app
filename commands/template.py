def run(bot):
	des = ''
	brf = ''
	als = ['']
	@bot.command(name = '', description = des, brief = brf, pass_context = True, aliases = als)
	async def __(context):
		await context.send('Hello! %s' % context.message.author.mention)
		print('[LOG] %s invoked !hello' % context.message.author.name)
