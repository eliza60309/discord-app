def run(bot):
	des = '賭輪盤，50%機率可以獲取雙倍的賭注，50%機率沒收賭金'
	brf = '賭輪盤，50%機率可以獲取雙倍的賭注，50%機率沒收賭金'
	als = ['gamble', 'roulette', 'bet']
	@bot.command(name = 'gambl', description = des, brief = brf, pass_context = True, aliases = als)
	async def gambl(context):
		import mysql.connector as sql
		import random
		import re
		import time
		import keys
		db = sql.connect(host = keys.MYSQL_HOST, user = keys.MYSQL_USER, password = keys.MYSQL_PASSWD, database = keys.MYSQL_DB)
		cursor = db.cursor()
		cursor.execute('select * from currency where user = %s' % str(context.message.author.id))
		result = cursor.fetchall()
		if(len(result) == 0):
			cursor.execute('insert into currency (user, currency, paytime) values (%s, %s, %s)' % (str(context.message.author.id), str(0), str(round(time.time()) - 3600)))
			db.commit()
			print('[LOG] %s invoked !gambl, initialize' % context.message.author.name)
			cursor.execute('select * from currency where user = %s' % str(context.message.author.id))
			result = cursor.fetchall()
		arr = list(map(int, re.findall('\d+', context.message.content)))
		if(len(arr) == 0):
			await context.send('%s: 告訴我你要下注多少錢呀!' % context.message.author.mention)
			print('[LOG] %s invoked !gambl, forgetting the stake' % context.message.author.name)
			return
		stake = arr[0]
		if(stake <= 0):
			await context.send('%s: 賭注要大於 0 ST唷!' % context.message.author.mention)
			print('[LOG] %s invoked !gambl, the stake less then 0' % context.message.author.name)
			return
		if(stake > int(result[0][1])):
			await context.send('%s: 你的財產只有 %s ST，不夠下注唷!' % (context.message.author.mention, result[0][1].replace('64', '||64||')))
			print('[LOG] %s invoked !gambl, not enough to afford stake %s' % (context.message.author.name, stake))
			return
		if(random.randint(0, 1) == 0):
			cursor.execute('update currency set currency = %s where user = %s' % (str(int(result[0][1]) + stake), str(context.message.author.id)))
			db.commit()
			await context.send('%s: 耶～贏了 %s ST，開勳～\\\\(>w<)/\n餘額: %s ST' % (context.message.author.mention, str(stake).replace('64', '||64||'), str(int(result[0][1]) + stake).replace('64', '||64||')))
			print('[LOG] %s invoked !gambl, won %s' % (context.message.author.name, stake))
			return
		else:
			cursor.execute('update currency set currency = %s where user = %s' % (str(int(result[0][1]) - stake), str(context.message.author.id)))
			db.commit()
			await context.send('%s: 哭哭～輸了 %s ST，藍瘦香菇～(OwQ)\n餘額: %s ST' % (context.message.author.mention, str(stake).replace('64', '||64||'), str(int(result[0][1]) - stake).replace('64', '||64||')))
			print('[LOG] %s invoked !gambl, lost %s' % (context.message.author.name, stake))
			return
