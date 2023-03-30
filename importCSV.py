import pandas as pd

df_csv = pd.read_csv('data/Online Retail Data.csv', header=0)

print(df_csv)
df_csv.info()
