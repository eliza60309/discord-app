def run(bot):
	des = 'Get information about Novel Coronavirus 2019'
	brf = 'Get information about Novel Coronavirus 2019'
	als = ['coronavirus', 'ncov', 'virus', 'ncov19', 'cov']
	@bot.command(name = 'cov19', description = des, brief = brf, pass_context = True, aliases = als)
	async def cov19(context):
		import requests

		#parse command
		arr = context.message.content.split(' ')
		query = ''
		
		#found subcommand
		if(len(arr) > 1):
			for token in arr[1:]:
				if(token != ''):
					query = token
					break
		
		#get request
		raw_text = requests.get('http://corona-stats.online/' + query).text
		raw_text = raw_text.split('</pre>')[0]
		raw_text = raw_text.split('<pre>')[1]
		#parse response
		if(len(raw_text) < 1950):
			await context.send('```\n' + raw_text + '\n```')
		else:
			pivot = 0
			while(pivot < len(raw_text) - 1):
				last = len(raw_text) - 1
				for i in range(pivot, min(pivot + 1950, len(raw_text) - 1)):
					if(raw_text[i] == '\n'):
						last = i
				await context.send('```\n' + raw_text[pivot: last + 1] + '\n```')
				pivot = last + 1
		print('[LOG] %s invoked !cov19' % context.message.author.name)
