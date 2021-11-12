import pandas as pd
from definitions import ROOT_DIR
import json

def read_csv():
    df = pd.read_csv(ROOT_DIR + '\\..\\files\\steam_games_prep.csv')
    return df

def get_price_ranges(df):
    price_range = {
        "Free" : 0,
        "0-5" : 0,
        "6-10" : 0,
        "11-25" : 0,
        "26-50" : 0,
        "51-75" : 0,
        "76-100" : 0,
        "100+" : 0
    }
    for index, row in df.iterrows():
        number = row['original_price']
        if number == 0:
            price_range['Free'] = price_range['Free'] + 1
        elif number <= 5:
            price_range['0-5'] = price_range['0-5'] + 1
        elif number <= 10:
            price_range['6-10'] = price_range['6-10'] + 1
        elif number <= 25:
            price_range['11-25'] = price_range['11-25'] + 1
        elif number <= 50:
            price_range['26-50'] = price_range['26-50'] + 1
        elif number <= 75:
            price_range['51-75'] = price_range['51-75'] + 1
        elif number <= 100:
            price_range['76-100'] = price_range['76-100'] + 1
        elif number > 100:
            price_range['100+'] = price_range['100+'] + 1
        else:
            print(row['url'], row['original_price'])
    print(price_range)

def get_genres(df):
    genres = {'None':0}
    for index, row in df.iterrows():
        try:
            genres_list = row['popular_tags'].split(',')
            for genre in genres_list:
                if genre in genres:
                    genres[genre]+=1
                else:
                    genres[genre]=1
        except:
            genres['None']+=1
    print(genres)

def get_developers(df):
    developers = {'None':0}
    for index, row in df.iterrows():
        try:
            developers_list = row['developer'].split(',')
            for developer in developers_list:
                if developer in developers:
                    developers[developer]+=1
                else:
                    developers[developer]=1
        except:
            developers['None']+=1
    with open('developers.txt', 'w') as file:
        file.write(json.dumps(developers))
    #print(developers)

def get_publishers(df):
    publishers = {'None':0}
    for index, row in df.iterrows():
        try:
            publishers_list = row['publisher'].split(',')
            for publisher in publishers_list:
                if publisher in publishers:
                    publishers[publisher]+=1
                else:
                    publishers[publisher]=1
        except:
            publishers['None']+=1
    with open('publishers.txt', 'w') as file:
        file.write(json.dumps(publishers))
    #print(publisher)

df = read_csv()
#get_price_ranges(df)
#get_genres(df)
#get_developers(df)
get_publishers(df)