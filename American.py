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
#useful_df = useful_df[useful_df['Report date'] >= '2020/02/01']
#useful_df = useful_df[useful_df['Report date'] <= '2020/11/30']
#print(useful_df)
useful_df.plot(x='Report date', title='US')
#plt.axvline(x='2020/04/16', c='r', label='the day the white house policy was implemented', ymax=0.625)
#plt.axvline(x='2020/05/15', c='c', label='the day the state policy was implemented', ymax=0.625)
#plt.axvline(x='2020/05/29', c='y', label='2 week after the policy', ymax=0.625)
#plt.legend()
plt.show()
