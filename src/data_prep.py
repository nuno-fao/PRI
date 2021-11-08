from numpy import NaN, nan
import pandas as pd
from definitions import ROOT_DIR
import tools

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

# Remove bad rows
for index in bad_rows:
    df = df.drop(index)

# Update index after operations
df = df.reset_index(drop=True)

# Create new column on Dataframe with all app id's
df['app_id'] = id_list

print(df)
