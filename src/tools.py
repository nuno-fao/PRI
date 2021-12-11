import requests
import json
def get_true_discount(df):
    x = 0
    for _, row in df.iterrows():
        try:
            disc = row.get('discount_price')
            orig = row.get('original_price')
            disc = str(disc)
            if disc < orig:
                x+=1
        except:
            continue
    return x


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

        response = get_reviews(appid, params)
        cursor = response['cursor']
        reviews += response['reviews']

        if len(response['reviews']) < 100: break

    return reviews

def str_to_list():
    f = open('src\\steam_games_prep.json')
    data = json.load(f)
    for entry in data:
        if entry["popular_tags"]:
            entry["popular_tags"] = entry["popular_tags"].split(",")
        if entry["game_details"]:
            entry["game_details"] = entry["game_details"].split(",")
        if entry["languages"]:
            entry["languages"] = entry["languages"].split(",")
        if entry["genre"]:
            entry["genre"] = entry["genre"].split(",")

    with open('games.json', 'w') as outfile:
        json.dump(data, outfile)
    return

str_to_list()