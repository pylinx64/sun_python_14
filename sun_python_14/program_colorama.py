'''
try:
	x = input()
	b = input() 
	print(int(x) / int(b))
except ZeroDivisionError:
	print('На ноль нельзя!')
except:
	print('Введите пожалуйста число!')
'''

import colorama, tqdm, time, random
from colorama import Fore

progress_bar = tqdm.tqdm(range(10), ascii=True, colour='GREEN', desc='Loading Game')
for x in progress_bar:
	time.sleep(0.1)
	
colorama.init()
print(Fore.MAGENTA + 'Hello world')
print(Fore.CYAN + 'A', end='')
print(Fore.BLUE + 'l', end='')
print(Fore.YELLOW + 'e', end='')
print(Fore.RED + 'x', end='')
