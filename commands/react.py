def run(bot):

	des = 'Reacts'
	brf = 'Reacts'
	als = ['YO', 'Yo', 'Yo!', 'YO!', 'yo!']
	@bot.command(name = 'yo', description = des, brief = brf, pass_context = True, aliases = als)
	async def yo___(context):
		await context.send('MIC CHECK!')
		print('[LOG] %s invoked !yo___' % context.message.author.name)
	
	als = ['JK', 'jk!', 'JK!']
	@bot.command(name = 'jk', description = des, brief = brf, pass_context = True, aliases = als)
	async def jk___(context):
		await context.send('WA WA WA WA WA!')
		print('[LOG] %s invoked !jk___' % context.message.author.name)
	
	als = ['WA', 'Wa!', 'Wa', 'WA!']
	@bot.command(name = 'wa', description = des, brief = brf, pass_context = True, aliases = als)
	async def wa___(context):
		await context.send('WA MOON DASS CRY!')
		print('[LOG] %s invoked !wa___' % context.message.author.name)
