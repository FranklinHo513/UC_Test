import requests
import json
import pandas as pd

url = 'https://data.cdc.gov.tw/en/download?resourceid=a59483fd-4b09-42bd-af15-3c12' \
      '3147d7e3&dataurl=https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'

r = requests.get(url)
a = json.loads(r.content)
df = pd.DataFrame.from_dict(a)
df.rename(columns={'個案研判日': 'Report date', '是否為境外移入': 'Import'}, inplace=True)
useful_df = df[['Report date', 'Import']]
useful_df.replace(to_replace='是', value='Yes', inplace=True)
useful_df.replace(to_replace='否', value='No', inplace=True)
