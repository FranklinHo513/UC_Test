import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

r = requests.get("https://api.covidtracking.com/v1/us/daily.json")
a = json.loads(r.content)
df = pd.DataFrame.from_dict(a)
print(df.columns)