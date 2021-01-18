import random

print('-> Приветсвую тебя в казино.нет')
money = 200

while True:
	# здесь выбирает ПК рандомно число 
	number_random = random.randint(1, 10)

	number_player = input('Введите число от 1 до 10: ')
	number_player = int(number_player)
	money = money - 5
	if number_player == number_random:
		print('-> You win баклажан$$$')
		money = money + 20
	else:
		print('-> Вы проиграли баклажан (((')
		print(number_random)
	print(money)
	print()
