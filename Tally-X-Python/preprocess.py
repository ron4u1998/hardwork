import pandas as pd
import numpy as np
import json


class preprocessss:
    def exceltojson(excelfile):
        df = pd.read_excel(excelfile, na_filter=False, engine='openpyxl')
        df.columns = (df.columns + " " + df.iloc[0])
        df = df.drop(0)
        df2 = df.drop_duplicates(keep='first')
        df2.columns = df2.columns.str.strip()
        name = excelfile.split('/')[1]
        print(name)
        name1 = name.split('.')[0]
        print(name1)
        df2.to_json(path_or_buf='json_file/'+name1+'.json', orient='records')


preprocessss.exceltojson('xlsx_file/21.xlsx')
