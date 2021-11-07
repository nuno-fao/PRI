from numpy import NaN, nan
import pandas as pd
from definitions import ROOT_DIR
import tools

# Import csv
df = pd.read_csv(ROOT_DIR + '\\..\\files\\steam_games_original.csv')

# Remove discount
df = df.drop('discount_price', axis=1)

# Drop bundles & remove column types because the only type remaining is 'app'
df = df.drop(df[(df['types'] == 'bundle') | (df['types'] == 'sub')].index).reset_index(drop=True)
df = df.drop('types', axis=1)

for i, row in df.iterrows():
    # Convert free into 0 and clear dollar sign
    if row['original_price'] is not NaN:
        df.at[i,'original_price'] = row['original_price'].replace('$','')
        try:
            df.at[i,'original_price'] = float(df.at[i,'original_price'])
        except ValueError:
            df.at[i,'original_price'] = 0.0

print(df)
