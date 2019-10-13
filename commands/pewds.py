def run(bot):
	des = 'Show status of Pewdiepie vs T-series campaign'
	brf = 'Show status of Pewdiepie vs T-series campaign'
	als = ['pewdiepie', 'pew']
	@bot.command(name = 'pewds', description = des, brief = brf, pass_context = True, aliases = als)
	async def pewdiepie(context):
		import requests as rq
		import json
		import keys
		P_ID = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
		T_ID = 'UCq-Fj5jknLsUf-MWSy4_brA'
		url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics'
		url_p = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC-lHJZR3Gqxm24_Vd_AJ5Yw&key=AIzaSyBU_oWEIULi3-n96vWKETYCMsldYDAlz2M'
		url_t = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCq-Fj5jknLsUf-MWSy4_brA&key=AIzaSyBU_oWEIULi3-n96vWKETYCMsldYDAlz2M'
		res_p = rq.get(url + '&id=' + P_ID + '&key=' + keys.YT_API).text
		res_t = rq.get(url + '&id=' + T_ID + '&key=' + keys.YT_API).text
		count_p = int(json.loads(res_p)['items'][0]['statistics']['subscriberCount'])
		count_t = int(json.loads(res_t)['items'][0]['statistics']['subscriberCount'])
		if(count_p > count_t):
			msg = 'Pewdiepie is winning T-series by `' + str(count_p - count_t) + '` subscribers!\n'
		elif(count_p == count_t):
			msg = 'Pewdiepie has same number of subscribers with T-series!\n'
		else:
			msg = 'Pewdiepie is losing T-series by `' + str(count_p - count_t) + '` subscribers!\n'
		msg += 'Subscribe to Pewdiepie to save him!\n'
		msg += 'https://www.youtube.com/user/PewDiePie?sub_confirmation=1'
		await context.send(msg)
		print('[LOG] %s invoked !pewdiepie' % context.message.author.name)
