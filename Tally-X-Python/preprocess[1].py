import pandas as pd
import numpy as np
import json
df = pd.read_excel(r'xlsx_file/21.xlsx', na_filter=False, engine='openpyxl')
# print(df.iloc[0])
# print(df)
df.columns = (df.columns + " " + df.iloc[0])

df = df.drop(0)

# df = df.iloc[0:].reset_index(drop=True)
print(df)

df2 = df.drop_duplicates(keep='first')
df2.to_excel('final12.xlsx', index=None)
json = df2.to_json(path_or_buf='default12.json')


# json_split = df2.to_json(path_or_buf = 'json_file\\split12.json', orient ='split')
# print("json_split = ", json_split, "\n")

json_records = df2.to_json(
    path_or_buf='json_file/records12.json', orient='records')
print("json_records = ", json_records, "\n")

json_index = df2.to_json(path_or_buf='json_file/index12.json', orient='index')
print("json_index = ", json_index, "\n")

# json_columns = df2.to_json(path_or_buf = 'json_file\\columns12.json', orient ='columns')
# print("json_columns = ", json_columns, "\n")

# json_values = df2.to_json(path_or_buf = 'json_file\\values12.json', orient ='values')
# print("json_values = ", json_values, "\n")

# json_table = df2.to_json(path_or_buf = 'json_file\\table12.json', orient ='table')
# print("json_table = ", json_table, "\n")
