import pandas as pd
from definitions import ROOT_DIR
from numpy import NaN, nan
import json
import re

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
    with open('prices.json', 'w') as file:
        file.write(json.dumps(price_range))
    #print(price_range)

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
    with open('genres.json', 'w') as file:
        file.write(json.dumps(genres))
    #print(genres)

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
    with open('developers.json', 'w') as file:
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
    with open('publishers.json', 'w') as file:
        file.write(json.dumps(publishers))
    #print(publisher)

def get_years_months(df):
    years = {'None':0,
    'Unreleased':0}
    months = {}
    for index, row in df.iterrows():
        try:
            if(row['release_date'] is NaN):
                years['None']+=1
            elif('coming' in row['release_date'].lower() or 'soon' in row['release_date'].lower()):
                years['Unreleased']+=1
            else:
                years_list = row['release_date'].split(', ')
                if years_list[1] in years:
                    years[years_list[1]]+=1
                else:
                    years[years_list[1]]=1
                month = years_list[0].split(' ')[0]
                if month in months:
                    months[month]+=1
                else:
                    months[month]=1
        except Exception as e:
            years['None']+=1
    with open('years.json', 'w') as file:
        file.write(json.dumps(years))
    with open('months.json', 'w') as file:
        file.write(json.dumps(months))

def get_reviews_and_total(df):
    reviews = {'None':0}
    review_nr = {'None':0,
    '<=1k':0,
    '1k-10k':0,
    '10k-50k':0,
    '50k-250k':0,
    '250k-1M':0,
    '>1M':0,
    }
    for index, row in df.iterrows():
        try:
            if(row['all_reviews'] is not None and row['all_reviews'] is not NaN):
                text_list = row['all_reviews'].split(',')
                rate = text_list[0]
                if rate in reviews:
                    reviews[rate]+=1
                else:
                    reviews[rate]=1
                if len(text_list)<3:
                    review_nr['<=1k']+=1
                elif text_list[1] is None:
                    review_nr['None']+=1
                else:
                    #number = int(text_list[1][1:-1])
                    number = re.search('\((.*)\)', row['all_reviews'])
                    number = int(number.group(1).replace(',',''))
                    if number <= 1000:
                        review_nr['<=1k']+=1
                    elif number <= 10000:
                        review_nr['1k-10k']+=1
                    elif number <= 50000:
                        review_nr['10k-50k']+=1
                    elif number <= 250000:
                        review_nr['50k-250k']+=1
                    elif number <= 1000000:
                        review_nr['250k-1M']+=1
                    else:
                        review_nr['>1M']+=1
            else:
                reviews['None']+=1
                review_nr['None']+=1
        except Exception as e:
            print(e)
            reviews['None']+=1
            review_nr['None']+=1
    with open('reviews.json', 'w') as file:
        file.write(json.dumps(reviews))
    with open('review_nr.json', 'w') as file:
        file.write(json.dumps(review_nr))
    #print(publisher)

df = read_csv()
#get_price_ranges(df)
#get_genres(df)
#get_developers(df)
#get_publishers(df)
#get_years_months(df)
get_reviews_and_total(df)