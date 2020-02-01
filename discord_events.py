import keys
def run(bot):
	
	@bot.event
	async def on_message(message):
		#if message.content.replace(' ', '').find(u'\U0001F4A9\U0001F4A9<:SS:612950702167293964>\U0001F4A9\U0001F4A9\U0001F437') != -1:
		#if message.author.id == int(keys.CAT_ID) and message.content.replace(' ', '').find(u'\u0001f4a9\U0001F4A9<:SS:612950702167293964>') != -1:
		pass
		if message.author.id == int(keys.CAT_ID) and message.content.replace(' ', '').find(u'<:SS:612950702167293964>') != -1:
			await message.delete()
			await message.channel.send(u'\U0001F4A9\U0001F4A9\U0001F431\U0001F431\U0001F4A9\U0001F4A9\U0001F437')
			'''if(message.content.find(u'\U0001F4A9') == -1):
				return
			try:
				await message.delete()
				await message.channel.send(u'\U0001F4A9\U0001F4A9\U0001F431\U0001F431\U0001F4A9\U0001F4A9\U0001F437')
				print("[LOG]: someone called you pig!")
			except:
				print("[LOG]: someone called you pig! Failed to stop him")
			'''
		await bot.process_commands(message)
	
	@bot.event
	async def on_member_update(before, after):
		if(after.id == keys.CAT_ID and after.nick != keys.CAT_NAME):
			await bot.get_guild(keys.SERVER_ID).get_member(keys.CAT_ID).edit(nick = keys.CAT_NAME)
			print("[LOG]: someone changed his/her name")
