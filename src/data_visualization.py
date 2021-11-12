import pandas as pd
from definitions import ROOT_DIR

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

df = read_csv()
get_price_ranges(df)