def run(bot):
	des = '獻祭一顆哈密瓜'
	brf = '獻祭一顆哈密瓜'
	als = ['honeydew', '哈密瓜', '獻上哈密瓜', '獻祭哈密瓜']

	@bot.command(name = 'honey', description = des, brief = brf, pass_context = True, aliases = als)
	async def honey(context):
		import mysql.connector as sql
		import keys
		import time
		import random

		#connect to sql
		db = sql.connect(host = keys.MYSQL_HOST, user = keys.MYSQL_USER, password = keys.MYSQL_PASSWD, database = keys.MYSQL_DB)
		cursor = db.cursor()

		#get number of melon
		cursor.execute('select name, number from honeydew where name = \'honeydew\'')
		result = cursor.fetchall()

		#add one and push
		number = result[0][1] + 1
		cursor.execute('update honeydew set number = %s where name = \'honeydew\'' % str(number))
		db.commit()

		#get author's currency data
		cursor.execute('select * from currency where user = %s' % str(context.message.author.id))
		result = cursor.fetchall()
		
		#author's first invoke
		if(len(result) == 0):
			
			#init author's account
			cursor.execute('insert into currency (user, currency, paytime, luck, lucktime) values (%s, %s, %s, %s, %s)' % (str(context.message.author.id), str(0), str(round(time.time()) - 3600), str(random.randint(1, 10)), str(round(time.time()))))
			db.commit()
			print('[LOG] %s invoked !honey, initialize' % context.message.author.name)
		
		#not first invoke
		else:
			cursor.execute('update currency set luck = %s, lucktime = %s where user = %s' % (str(random.randint(1, 10)), str(round(time.time())), str(context.message.author.id)))
			db.commit()
			print('[LOG] %s invoked !honey' % context.message.author.name)

		#message
		await context.send('你恭敬的獻上一顆哈密瓜\n你感覺自己的運氣變好了一點點\n現在祭壇上有%s顆哈密瓜了!!\n:melon:\\\\(>w<)/:melon:' % str(number))

