import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

r = requests.get("https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc"
                 "%2Fenhanced_sur_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%7D")
a = json.loads(r.content)
df = pd.DataFrame.from_dict(a)
print(df.columns)
useful_df = df[['Case no.', 'Report date', 'Case classification*']]
useful_df.set_index('Case no.', inplace=True)
useful_df['Report date'] = pd.to_datetime(useful_df['Report date'], format='%d/%m/%Y')
case = useful_df.groupby('Report date').count()
case.plot()
plt.axvline(x='2020-03-20', c='r')
plt.show()
