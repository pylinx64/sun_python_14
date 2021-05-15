import discord

TOKEN = 'ODM1ODA5NjI2NTY0ODUzNzcx.YIU2Xw.2fzVEi9OxF_8_zJ9JjJWdNzxcws'

# хранится наш бот
client = discord.Client()

# отслеживает событие "сообщение"
@client.event
async def on_message(message):
	# не отвечает на сообщения ботов
	if message.author.bot == True:
		return
	
	# печатает в консоль сообщения
	print(f'--- автор: {message.author} | сообщение: {message.content} | канал: {message.guild} ---')
	
	if 'привет' in message.content.lower():
		# отправляет сообщения
		await message.channel.send('КУ-КУ')
		
	elif 'как дела' in message.content.lower():
		# отправляет сообщения
		await message.channel.send('норм')
		await message.channel.send('норм')
	else:
		await message.channel.send('Ошибка понимания сов...  404')

# запускаем бота
client.run(TOKEN)
