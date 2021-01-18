import telebot
import bs4
import requests
import random

def gif_robot():
	'''Подключается к сайту и собирает ссылки на гифки'''
	res = requests.get('https://tenor.com/search/robots-gifs')
	# проверка 404 - ошибка, 200 - ОК
	res.raise_for_status()
	# скачиваем сайт и находим <img>
	soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    
    # заполняем list с гифками
	for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
        
    print(gif_list)

    
	

bot = telebot.TeleBot('1497537520:AAFIuecYC71rm68ZsJiItPw-c5Y-w5reJdY') # сюда токен


@bot.message_handler(commands=['start'])
def start_message(message):
	'''Принимает команду и отвечает на нее'''
	keyboard = telebot.types.ReplyKeyboardMarkup(True)
	keyboard.row('Привет', '🧱')
	bot.send_message(message.chat.id, 'Привет, я 😺котобот!', reply_markup=keyboard)
	print(message)


@bot.message_handler(content_types=['text'])
def send_text(message):
	if 'привет' in message.text:
		bot.send_message(message.chat.id, 'Приветики')

	elif 'пока' in message.text:
		bot.send_message(message.chat.id, 'Пока')

	elif 'дела' in message.text:
		bot.send_message(message.chat.id, '....')
	
	elif 'гиф' in message.text:
		bot.send_message(message.chat.id, random.choice(gif_robot()))
		
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю!')
				
bot.polling()

