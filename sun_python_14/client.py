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

# вкл/выкл чат
shutdown = False
join = False

# ваш ip, ваш порт
host = 
port = 0
