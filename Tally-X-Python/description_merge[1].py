import numpy as np
import pandas as pd

df1= pd.read_excel('xlsx_file\\SCAN_1.xlsx', na_filter=False, engine='openpyxl')
print(df1.columns)
def Concat(a,b):
    if a!=b:
        res=a + ' ' + b
        return res
    else:
        return a

def desc_merge(df):

    # df['Description'] = df.apply(lambda row:Concat(row[1],row[2]),axis=1)  
    # df.drop(['Unnamed: 1 ', 'Description of Goods '], axis=1, inplace = True)
    # df_new = df[['SI No.', 'Description', 'Unnamed: 3 ', 'HSN/SAC ', 'Quantity ', 'per ', 'Unnamed: 7 ']]
    if 'Unnamed: 1' in list(df.columns):# and 'per ' in list(df2.columns):
        print('yes')
        df.insert(1, 'Description999', df.apply(lambda row:Concat(row[1],row[2]),axis=1))
        df.insert(1, 'Description', np.where((df['Description999'] != df['Unnamed: 3']) , df['Description999'] + df['Unnamed: 3'], df['Description999']))
        print("columns:::::::::::::", df.filter(regex='Description999|Description of Goods|3|1').columns)
        df.drop(df.filter(regex='Description999|Description of Goods|3|1').columns, axis=1, inplace=True)
    elif 'Unnamed: 2 ' in list(df.columns):
        df.insert(1, 'Description', df.apply(lambda row:Concat(row[1],row[2]),axis=1))
        df.drop(df.filter(regex='Description of |2').columns, axis=1, inplace=True)
    else:
        print('gnadu')
        df.rename(columns={ df.columns[1]: "Description" }, inplace=True)
        
        print('ye thik h!')
        # df.to_excel('.\\le_ronak.xlsx', index=False)
    return df

desc_merge(df1)
# df1.to_excel('.\\le_ronak.xlsx', index=False)
print(df1.columns)