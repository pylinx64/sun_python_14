import discord

TOKEN = 'ODM1ODA5NjI2NTY0ODUzNzcx.YIU2Xw.eoMjdURfpNGeq2ac_2LpHTa6Hb8'

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
	
	# отправляет сообщения
	await message.channel.send(message.content)

# запускаем бота
client.run(TOKEN)
