from numpy import NaN, nan
import numpy as np
import pandas as pd
from definitions import ROOT_DIR
import json

def initial_prep():

    # Import csv
    df = pd.read_csv(ROOT_DIR + '\\..\\files\\steam_games.csv')

    # Remove discount
    df = df.drop('discount_price', axis=1)

    # Drop bundles & remove column types because the only type remaining is 'app'
    df = df.drop(df[(df['types'] == 'bundle') | (df['types'] == 'sub')].index).reset_index(drop=True)
    df = df.drop('types', axis=1)

    bad_rows = []
    id_list = []
    for i, row in df.iterrows():

        # Convert free into 0 and clear dollar sign
        if row['original_price'] is not nan:
            if row['original_price'] is None:
                bad_rows.append(i)
                continue
            df.at[i, 'original_price'] = row['original_price'].replace('$', '')
            try:
                df.at[i, 'original_price'] = float(df.at[i, 'original_price'])
            except ValueError:
                if df.at[i, 'original_price'] == "Free to Play":
                    df.at[i, 'original_price'] = 0.0
                else:
                    bad_rows.append(i)
                    continue
        else:
            bad_rows.append(i)
            continue

        # Remove games with inapropriate dates
        if row["release_date"]:
            field = str(row["release_date"]).split(' ')
            if len(field) != 3:
                bad_rows.append(i)
                continue

        # Simplify recent and all_time reviews
        if row["recent_reviews"]:
            try:
                percent_index = row["recent_reviews"].index('%')
                df.at[i,'recent_reviews'] = int(row["recent_reviews"][percent_index-2:percent_index]) 
            except Exception as e:
                df.at[i,'recent_reviews'] = -1

        if row["all_reviews"]:
            try:
                percent_index = row["all_reviews"].index('%')
                df.at[i,'all_reviews'] = int(row["all_reviews"][percent_index-2:percent_index]) 
            except Exception as e:
                df.at[i,'all_reviews'] = -1

        # Add app id to id_list
        split_url = row['url'].split("/")
        try:
            app_index = split_url.index('app')
            id_list.append(split_url[app_index+1])
        except:
            bad_rows.append(i)
            continue

        
        if row['publisher'] is not nan:
            string = row['publisher']
            substring1 = string[0:int(len(string)/2)]
            substring2 = string[int(len(string)/2)+1:]
            if(substring1 == substring2):
                df.at[i,'publisher'] = substring1
        else:
            df.at[i,'publisher'] = ""

    # Remove bad rows
    for index in bad_rows:
        df = df.drop(index)

    # Update index after operations
    df = df.reset_index(drop=True)

    # Create new column on Dataframe with all app id's
    df['app_id'] = id_list
    df['app_id'].to_json("temp.json")
    df.to_csv(path_or_buf=ROOT_DIR + '\\..\\files\\steam_games_prep.csv',index=False)
    df.to_json(path_or_buf=ROOT_DIR + '\\..\\files\\steam_games_prep.json',orient='records')

    return

def merge_reviews():

    f = open('files\\reviews3.json')
    reviews = json.load(f)

    review_extract = {}
    for item in reviews:
        game_id = item['game_id']
        if game_id in review_extract:
            review_extract[game_id].append(item['review'])
        else:
            review_extract[game_id] = [item['review']]

    with open('files\\reviews.json', 'w') as outfile:
        json.dump(review_extract, outfile)

    f = open('files\\steam_games_prep.json')
    data = json.load(f)

    for entry in data:
        if entry['app_id'] in review_extract:
            entry["reviews"] = review_extract[entry['app_id']]
        else:
            entry["reviews"] = ""
    
    with open('files\\games.json', 'w') as outfile:
        json.dump(data, outfile)

    return

     
initial_prep()
merge_reviews()