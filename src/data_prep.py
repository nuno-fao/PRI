from numpy import NaN, nan
import pandas as pd
from definitions import ROOT_DIR

# Import csv
df = pd.read_csv(ROOT_DIR + '/steam_games.csv')

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
        df.at[i, 'original_price'] = row['original_price'].replace('$', '')
        try:
            df.at[i, 'original_price'] = float(df.at[i, 'original_price'])
        except ValueError:
            df.at[i, 'original_price'] = 0.0

    # Add app id to id_list
    split_url = row['url'].split("/")
    try:
        app_index = split_url.index('app')
        id_list.append(split_url[app_index+1])
    except:
        bad_rows.append(i)

    
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

print(df)