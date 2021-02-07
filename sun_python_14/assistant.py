import pyttsx3
import random
import webbrowser
from datetime import date, time, datetime
import pyautogui


# Настройки для бота
tts = pyttsx3.init()			# запуск движка
tts.setProperty('rate', 150)	# скорость разговора


# Команды для бота
def say_bot(msg):
	tts.say(msg)				 
	print(msg)
	tts.runAndWait()
	
def open_minecraft():
	pyautogui.click(527, 714, duration=1)


# Сообщения для ассистента
MESSAGE_ERROR = ['Я не знаю этой команды', '100100100', 'ERROR', 'Хьюстон у вас проблемы']


# запоминаем имя человека
say_bot('Привет я асистент бот. Какое твое имя?')
NAME = input('Введите имя? ')
say_bot('Бупм бип, ' + NAME)

#-----------ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ-------------------
while True:
	command = input('Введи слово или команду: ')
	if command == 'что ты умеешь?':
		say_bot('10001011101' + NAME)
	elif command == 'погода?':
		say_bot('да' + NAME)
	elif command == 'открой браузер':
		webbrowser.open('https://scratch.mit.edu/projects/181320882/editor/')
		say_bot('сайт открыт')
	elif command == 'время':
		time_check = datetime.now()	
		h = time_check.hour
		m = time_check.minute
		say_bot(str(h)+':'+str(m))
	elif command == 'оупен':
		open_minecraft()
		say_bot('маинкрафт старт')
	else:
		say_bot(random.choice(MESSAGE_ERROR))
