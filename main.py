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
dummy = pd.get_dummies(useful_df['Case classification*'])
useful_df = pd.concat([useful_df, dummy], axis=1)
useful_df.drop('Case classification*', axis=1, inplace=True)
useful_df['Total Local Case'] = useful_df['Epidemiologically linked with imported case'] + useful_df['Epidemiologically linked with local case'] + useful_df['Local case'] + useful_df['Epidemiologically linked with possibly local case'] + useful_df['Possibly local case']
useful_df.drop(['Epidemiologically linked with imported case', 'Epidemiologically linked with local case', 'Local case', 'Possibly local case', 'Epidemiologically linked with possibly local case'], axis=1, inplace=True)
useful_df = useful_df.groupby('Report date').aggregate({'Imported case': 'sum', 'Total Local Case': 'sum'})
useful_df.rename(columns={'Total Local Case': 'Local Case', 'Imported case': 'Imported Case'}, inplace=True)
useful_df.reset_index(inplace=True)
print(useful_df)
#useful_df = useful_df[useful_df['Report date'] >= '2020/07/01']
#useful_df = useful_df[useful_df['Report date'] <= '2020/08/31']
useful_df.plot(x='Report date', title='Hong Kong')
#plt.axvline(x='2020/07/22', c='r')
plt.ylim(-0.5, 150)
plt.show()
