import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

r = requests.get("https://api.covidtracking.com/v1/us/daily.json")
a = json.loads(r.content)
df = pd.DataFrame.from_dict(a)
print(df.columns)
useful_df = df[['date', 'positiveIncrease']]
useful_df['date'] = pd.to_datetime(useful_df['date'], format='%Y%m%d')
useful_df.rename(columns={'positiveIncrease': 'Daily Case', 'date': 'Report date'}, inplace=True)
useful_df = useful_df[useful_df['Report date'] >= '2020/03/01']
useful_df = useful_df[useful_df['Report date'] <= '2020/05/30']
print(useful_df)
useful_df.plot(x='Report date', title='US')
plt.axvline(x='2020/03/16', c='r')
plt.show()
