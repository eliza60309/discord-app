def run(bot):
	des = 'Say hi'
	brf = 'Say hi'
	als = ['hi', 'hey']
	@bot.command(name = 'hello', description = des, brief = brf, pass_context = True, aliases = als)
	async def hello(context):
		await context.send('Hello! %s' % context.message.author.mention)
		print('[LOG] %s invoked !hello' % context.message.author.name)
