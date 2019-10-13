def run(bot):
	LAPSE = 3600
	des = '領餉，一個小時可以領一次，每次100ST'
	brf = '領餉，一個小時可以領一次，每次100ST'
	als = ['pay', 'salary', '薪水', 'faucet']
	@bot.command(name = 'payme', description = des, brief = brf, pass_context = True, aliases = als)
	async def payme(context):
		import mysql.connector as sql
		import time
		import keys
		db = sql.connect(host = keys.MYSQL_HOST, user = keys.MYSQL_USER, password = keys.MYSQL_PASSWD, database = keys.MYSQL_DB)
		cursor = db.cursor()
		cursor.execute('select * from currency where user = %s' % str(context.message.author.id))
		result = cursor.fetchall()
		if(len(result) == 0):
			cursor.execute('insert into currency (user, currency, paytime) values (%s, %s, %s)' % (str(context.message.author.id), str(100), str(round(time.time()))))
			db.commit()
			await context.send('%s: 你領取了 100 ST的薪水，你的財產現在有 %s ST' % (context.message.author.mention, str(100)))
			print('[LOG] %s invoked !payme, initialize' % context.message.author.name)
		else:
			if(round(time.time()) > int(result[0][2]) + LAPSE):
				cursor.execute('update currency set currency = %s, paytime = %s where user = %s' % (str(int(result[0][1]) + 100), str(round(time.time())), str(context.message.author.id)))
				db.commit()
				await context.send('%s: 你領取了 100 ST的薪水，你的財產現在有 %s ST' % (context.message.author.mention, str(int(result[0][1]) + 100).replace('64', '||64||')))
				print('[LOG] %s invoked !payme, paid' % context.message.author.name)
			else:
				remain = int(result[0][2]) + LAPSE - round(time.time())
				remain_m = str(round(remain) // 60)
				remain_s = str(round(remain) % 60)
				await context.send('%s: 你還有 %s 分 %s 秒後才能再領下一次薪水唷！' % (context.message.author.mention, remain_m, remain_s))
				print('[LOG] %s invoked !payme, failed' % context.message.author.name)
