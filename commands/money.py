def run(bot):
	des = '查詢餘額'
	brf = '查詢餘額'
	als = ['cash', '餘額', 'account', 'bank']
	@bot.command(name = 'money', description = des, brief = brf, pass_context = True, aliases = als)
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
			await context.send('%s: 你的財產現在有 0 ST' % context.message.author.mention)
			print('[LOG] %s invoked !money, initialize' % context.message.author.name)
		else:
			await context.send('%s: 你的財產現在有 %s ST' % (context.message.author.mention, result[0][1].replace('64', '||64||')))
			print('[LOG] %s invoked !money' % context.message.author.name)
			
