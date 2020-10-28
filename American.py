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
useful_df.set_index('date', inplace=True)
print(useful_df)
useful_df.plot()
plt.show()
