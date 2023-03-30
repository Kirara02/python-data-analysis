import gspread as gs
import pandas as pd

sheet_id = '1ZNVJziTv1Krl3DUEmpcIsVTaabeiFFSRk02q400Guk4'
sheet_name = 'Online Retail Data'
gc = gs.service_account('data/kirara-project-python-31f2b5de218c.json')

sheet = gc.open_by_key(sheet_id).worksheet(sheet_name).get_all_records()

df_sheet = pd.DataFrame(sheet)
print(df_sheet)

df_sheet.info()
