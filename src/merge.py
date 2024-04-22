import pandas as pd
import csv

table1 = pd.read_csv('spydata.csv')
table2 = pd.read_csv('steamdata.csv')

table1 = table1.drop_duplicates(subset=['appid'], keep='first')
table2 = table2.drop_duplicates(subset=['appid'], keep='first')

# full outer join
merged = pd.merge(table1, table2, on='appid', how='outer')

merged = merged[['appid', 'name', 'type', 'genre', 'metacritic', 'developer', 'positive','negative','owners', 'initialprice','ccu']]

for col in merged.columns:
    merged[col] = merged[col].apply(lambda x: str(x).replace('"', '') if pd.notnull(x) else '')

merged.to_csv('merged_data_test.csv', index=False)