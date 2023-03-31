import pandas as pd
import os

df_excel = pd.read_excel('data/Online Retail Data.xlsx',
                         sheet_name='Online Retail Data', header=0)
print(df_excel)

