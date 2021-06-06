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
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass

shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.1.206", 11719)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input('name ---> ')
name = Fore.GREEN + 'К' + Fore.BLUE + 'О' + Fore.BLUE + 'Р' + Fore.CYAN + 'О' + Fore.BLUE + 'Н' + Fore.YELLOW + 'А' + Fore.YELLOW + 'В' + Fore.RED + 'І' + Fore.BLUE + 'Р' + Fore.GREEN + 'У' + Fore.BLUE + 'С' + Fore.RESET
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)

rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

while shutdown == False:
	try:
		message = input('['+name+'] ------> ')
		message = Fore.CYAN + message + Fore.RESET
		if message != '':
			s.sendto(("["+name+"] => " + message).encode("utf-8"), server)
	except:
		s.sendto(("["+name+"] => left chat ").encode("utf-8"), server)
		shutdown = True

rT.join()
S.close()
