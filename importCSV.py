import pandas as pd

df_csv = pd.read_csv('data/Online Retail Data.csv', header=0)

print(df_csv)
print('================ Query with Index =================\n')

# mengambil 1 baris tertentu
print('---------mengambil 1 baris tertentu ----------')
print(df_csv.iloc[1], '\n')

# mengambil beberapa baris tertentu dengan index berupa list
print('--------- mengambil beberapa baris tertentu dengan index berupa list ----------')
print(df_csv.iloc[[5, 6, 7, 8]], '\n')

# mengambil beberapa baris tertentu dengan index berupa range
print('--------- mengambil beberapa baris tertentu dengan index berupa range ----------')
print(df_csv.iloc[10:15], '\n')

# mengambil semua baris setelah baris tertentu
print('--------- mengambil semua baris setelah baris tertentu ----------')
print(df_csv.iloc[49000:], '\n')

# mengambil semua baris sebelum baris tertentu
print('--------- mengambil semua baris sebelum baris tertentu ----------')
print(df_csv.iloc[:15], '\n')

# mengambil 1 baris terakhir
print('--------- mengambil 1 baris terakhir ----------')
print(df_csv.iloc[-1], '\n')

# mengambil beberapa baris terakhir
print('--------- mengambil beberapa baris terakhir ----------')
print(df_csv.iloc[-5:], '\n')

# mengambil semua baris setelahnya beberapa baris terakhir
print('--------- mengambil semua baris setelahnya beberapa baris terakhir ----------')
print(df_csv.iloc[:-10], '\n')

# mengambil 1 kolom tertentu
print('--------- mengambil 1 kolom tertentu ----------')
print(df_csv.iloc[:, 2], '\n')

# mengambil 1 kolom tertentu dengan index berupa list
print('--------- mengambil 1 kolom tertentu dengan index berupa list ----------')
print(df_csv.iloc[:, [1, 2, 3]], '\n')

print('================== query with index non-integer ----------')
df_noninteger = df_csv.copy()
df_noninteger.set_index('order_id', inplace=True)
print(df_noninteger)

# mengambil baris dengan index non-integer tertentu
print('------------mengambil baris dengan index non-integer tertentu------------')
print(df_noninteger.loc[['493413', 'C493411', '539991']])

# mengambil 1 kolom dengan index non-integer tertentu
print('------------mengambil 1 kolom dengan index non-integer tertentu ------------')
print(df_noninteger.loc[:, 'product_name'])

# mengambil beberapa kolom dengan index non-integer tertentu
print('------------mengambil beberapa kolom dengan index non-integer tertentu ------------')
print(df_csv.loc[:, ['order_id', 'product_code', 'product_name']], '\n')

print('================ Query with Logical Expression =================\n')

# mengambil baris dengan 1 kondisi tertentu
print('------------ mengambil baris dengan 1 kondisi tertentu -------------')
print(df_csv[df_csv['order_id'] == '539991'])

# mengambil baris dengan 1 kondisi tertentu dan beberapa kolom tertentu
print('------------ mengambil baris dengan 1 kondisi tertentu dan beberapa kolom tertentu -------------')
print(df_csv.loc[df_csv['order_id'] == '539991', [
      'product_code', 'product_name', 'quantity']])

# alternatif penulisan df['order_id']
print("---------- alternatif penulisan df['order_id'] -----------------")
print(df_csv.loc[df_csv.order_id == '539991'])

# mengambil baris dengan beberapa kondisi dengan operator & (and)
print("---------- mengambil baris dengan beberapa kondisi dengan operator & (and) -----------------")
print(df_csv[(df_csv['product_name'].str.contains('TEA'))
      & (df_csv['quantity'] == 1)])


# mengambil baris dengan beberapa kondisi dengan operator | (or)
print("---------- mengambil baris dengan beberapa kondisi dengan operator | (or) -----------------")
print(df_csv[(df_csv['product_name'].str.contains('TEA'))
      | (df_csv['product_name'].str.contains('COFFEE'))])


# mengambil baris dengan beberapa kondisi dengan kombinasi kondisi and ataupun or
print("---------- mengambil baris dengan beberapa kondisi dengan kombinasi kondisi and ataupun or-----------------")
print(df_csv[(df_csv['product_name'].str.contains('TEA')) | (
    df_csv['product_name'].str.contains('COFFEE')) & (df_csv['quantity'] > 10)])
