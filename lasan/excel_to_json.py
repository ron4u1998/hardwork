import pandas as pd
import numpy as np
# import json
import os

class preprocessss:
    def exceltojson(excelfile):
        # print(excelfile)
        df = pd.read_excel(excelfile,na_filter=False, engine='openpyxl')
        df.columns = ( df.columns + " " + df.iloc[0])
        df = df.drop(0)
        df2 = df.drop_duplicates(keep='first')
        df2.columns = df2.columns.str.strip()
        name = excelfile.split('/')[2].split('.')[0]
        # print(name)
        # print(os.listdir())
        df2.to_json(path_or_buf = os.path.join('json_file',name+'.json'), orient ='records')

# preprocessss.exceltojson('xlsx_file\\Scan_10.xlsx')