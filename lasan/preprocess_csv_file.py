import numpy as np
import pandas as pd
import os
from appconfig import AppConfig
from flask import session


def pehla_wala(data):
    if 'Unnamed: 0' in list(data.columns):
        data.rename(columns = {'Unnamed: 0':'SI'}, inplace = True)

    data.columns = data.columns + ' ' + data.iloc[0]
    data.drop(index=0, inplace = True)
    return data


def preprocess_csv_file(file_name, file_path, id):
    pd.set_option("display.max_columns", 30)
    df = pd.read_excel(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'), na_filter=False)
    # os.remove(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'))
    # def pehla_wala(df):
    #     if 'Unnamed: 0' in list(df.columns):
    #         df.rename(columns = {'Unnamed: 0':'SI'}, inplace = True)

    #     df.columns = df.columns + ' ' + df.iloc[0]
    #     df.drop(index=0, inplace = True)
    #     return df

    df2 = pehla_wala(df)


    if 'Rate' in list(df2.columns) and 'per' in list(df.columns):
        df2['Rate'] = df2['Rate'].str.replace('[^,.0-9]', '', regex=True).str.strip()
        df2['per'] = df2['per'].str.replace('[^a-zA-Z]', '', regex = True).str.strip()
    else:
        print('Sab sahi h bro!')


    def Concat(a,b):
        if a!=b:
            res=a + ' ' + b
            return res
        else:
            return a

    def amt_merge(df):
       
        if 'Unnamed: 9 ' in list(df.columns):
            df2['Amount'] = np.where((df2['Amount '] != df2['Unnamed: 9 ']) , df2['Amount '] + df2['Unnamed: 9 '], df2['Amount '])
            df.drop(df.filter(regex='Amount |9').columns, axis=1, inplace=True)
        elif 'Unnamed: 8 ' in list(df.columns):
            df2['Amount'] = np.where((df2['Amount '] != df2['Unnamed: 8 ']) , df2['Amount '] + df2['Unnamed: 8 '], df2['Amount '])
            df.drop(df.filter(regex='Amount |8').columns, axis=1, inplace=True)
        elif 'Unnamed: 7 ' in list(df.columns):
            df.rename(columns={ 'Unnamed: 7 ' : 'Amount' }, inplace=True)
            first_column = df.pop('Amount')
            df.insert(len(df.columns), 'Amount', first_column)
        else:
            df.insert(len(df.columns), 'Amount', df['Amount '])
            df.drop(['Amount '], axis = 1, inplace = True)
            print('ye thik h!')
        return df

    df3 = amt_merge(df2)

    def desc_merge(df):
        if 'Unnamed: 1 ' in list(df.columns):
            df.insert(1, 'Description999', df.apply(lambda row:Concat(row[1],row[2]),axis=1))
            df.insert(1, 'Description', np.where((df['Description999'] != df['Unnamed: 3 ']) , df['Description999'] + df['Unnamed: 3 '], df['Description999']))
            df.drop(df.filter(regex='Description999|Description of|3|1').columns, axis=1, inplace=True)
        elif 'Unnamed: 2 ' in list(df.columns):
            df.insert(1, 'Description', df.apply(lambda row:Concat(row[1],row[2]),axis=1))
            df.drop(df.filter(regex='Description of|2').columns, axis=1, inplace=True)
        else:
            df.rename(columns={ df.columns[1]: "Description" }, inplace=True)
            df.drop(df.filter(regex='Description of|2').columns, axis=1, inplace=True)
            print('ye thik h!')    
        return df

    df4 = desc_merge(df3)
    print(df4)

    # df4.to_excel(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'), index=None)
    # df5 = pd.read_excel(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'), na_filter=False)
    # os.remove(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'))
    # df5.drop(index=0, inplace=True)
    # df5.rename(columns = {'SI':'SI No.'}, inplace = True)
    # Amount = df5['SI No.'].to_list()
    # last = len(Amount)
    # Amount = [ele for ele in Amount if ele != '']
    # for amt in range(len(Amount)):
    #     if (Amount[amt] != Amount[-1]):
    #         x = np.where(df5['SI No.'] == Amount[amt] )
    #         y = np.where(df5['SI No.'] == Amount[amt+1] )
    #         for col in df5.columns:
    #             df5[col][x[0][0]:y[0][0]] = df5[col][x[0][0]:y[0][0]].str.cat(sep='\n')
    #     else:
    #         x = np.where(df5['SI No.'] == Amount[amt])
    #         for col in df5.columns:
    #             df5[col][x[0][0]:last] = df5[col][x[0][0]:last].str.cat(sep='\n')
    # df_1 = df5.drop_duplicates(keep='first')
    df_1 = df4.style.set_properties(**{'text-align': 'left'})
    # df_1.to_excel(os.path.join(file_path,file_name.split('.')[0]+'.xlsx'), index = None)
    
    return df_1


# json = df_1.to_json(path_or_buf = 'test1.json')


# json_split = df_1.to_json(path_or_buf = 'test2.json', orient ='split')
# print("json_split = ", json_split, "\n")
   
# json_records = df_1.to_json(path_or_buf = 'test3.json', orient ='records')
# print("json_records = ", json_records, "\n")
   
# json_index = df_1.to_json(path_or_buf = 'test4.json', orient ='index')
# print("json_index = ", json_index, "\n")
   
# json_columns = df_1.to_json(path_or_buf = 'test5.json', orient ='columns')
# print("json_columns = ", json_columns, "\n")
   
# json_values = df_1.to_json(path_or_buf = 'test6.json', orient ='values')
# print("json_values = ", json_values, "\n")
   
# json_table = df_1.to_json(path_or_buf = 'test7.json', orient ='table')
# print("json_table = ", json_table, "\n")