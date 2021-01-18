#https://tenor.com/search/fat-cat-gifs
import bs4
import requests

def gif_fat_cat():
	'''Ищет ссылки на гифки и сохраняет их'''
	res = requests.get('https://tenor.com/search/fat-cat-gifs')
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

	return gif_list
	

    
