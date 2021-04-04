# -*- coding: utf-8 -*-

import socket
import threading
import colorama

from colorama import Fore
colorama.init()

def receving (name, sock, switch):
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print(addr)
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass

# вкл/выкл чат
join = False

# ваш ip, ваш порт
host = socket.gethostbyname(socket.gethostname())
port = 0

# ip сервера и порт
server = ("192.168.1.206", 11719)

# сокет 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input('name -> ')
name = Fore.CYAN + name + Fore.RESET
# отправляет сообщение на сервер
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)

shutdown = False
rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

while shutdown == False:
	try:
		message = input("["+name+"] > ")
		message = Fore.YELLOW + message + Fore.RESET
		if message != '':
			s.sendto(("["+name+"] > " + message).encode("utf-8"), server)
	except:
		s.sendto(("["+name+"] <= left chat ").encode("utf-8"), server)
		shutdown = True
		
rT.join()
s.close()
