import requests
import pandas as pd
import json

def get_reviews(appid, params={'json':1}):
		url = 'https://store.steampowered.com/appreviews/'
		response = requests.get(url=url+str(appid), params=params, headers={'User-Agent': 'Mozilla/5.0'})
		return response.json()

def get_n_reviews(appid, n=100):
	reviews = []
	cursor = '*'
	params = {
			'json' : 1,
			'filter' : 'all',
			'language' : 'english',
			'day_range' : 9223372036854775807,
			'review_type' : 'all',
			'purchase_type' : 'all'
			}
	while n > 0:
		params['cursor'] = cursor.encode()
		params['num_per_page'] = min(100, n)
		n -= 100
		try:
				response = get_reviews(appid, params)
		except requests.exceptions.RequestException as e:
				continue

		cursor = response['cursor']
		reviews += response['reviews']

		if len(response['reviews']) < 100: break

	a = {"id": appid, "reviews":reviews}
	return a


df = pd.read_json('temp.json', typ='series')
reviews = []
z = 0
for x in df:
	reviews.append(get_n_reviews(x,10))
	with open("data_file.json", "a") as write_file:
		json.dump(reviews, write_file)
	reviews = []
	z +=1
	print(z+"/38010" )
