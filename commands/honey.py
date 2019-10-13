def run(bot):
	des = '獻祭一顆哈密瓜'
	brf = '獻祭一顆哈密瓜'
	als = ['honeydew', '哈密瓜', '獻上哈密瓜', '獻祭哈密瓜']
	@bot.command(name = 'honey', description = des, brief = brf, pass_context = True, aliases = als)
	async def honey(context):
		import mysql.connector as sql
		import keys
		db = sql.connect(host = keys.MYSQL_HOST, user = keys.MYSQL_USER, password = keys.MYSQL_PASSWD, database = keys.MYSQL_DB)
		cursor = db.cursor()
		cursor.execute('select name, number from honeydew where name = \'honeydew\'')
		result = cursor.fetchall()
		number = result[0][1] + 1
		cursor.execute('update honeydew set number = %s where name = \'honeydew\'' % str(number))
		db.commit()
		await context.send('你恭敬的獻上一顆哈密瓜\n現在祭壇上有%s顆哈密瓜了!!\n:melon:\\\\(>w<)/:melon:' % str(number))
		print('[LOG] %s invoked !honey' % context.message.author.name)

