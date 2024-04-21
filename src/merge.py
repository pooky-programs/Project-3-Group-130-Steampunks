import pandas as pd
import csv

table1 = pd.read_csv('spydata.csv')
table2 = pd.read_csv('steamdata.csv')

# full outer join
merged = pd.merge(table1, table2, on='appid', how='outer')

merged = merged[['appid', 'name', 'type', 'genre', 'metacritic', 'developer', 'positive','negative','owners', 'initialprice','ccu']]
# merged.drop(columns=['recommendations'], inplace=True)

merged.to_csv('merged_data.csv', index=False)