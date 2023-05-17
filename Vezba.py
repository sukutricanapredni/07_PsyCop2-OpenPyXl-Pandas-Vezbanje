import pandas as pd
import openpyxl as op

dt=pd.read_excel('test2.xlsx',sheet_name='Sheet1')

l=[1,2,3,4,5,6]
dt['Odeljenja']=l
print(dt)
dt.to_excel('excel1.xlsx',index=False)



dt=pd.read_excel('test.xlsx',sheet_name='Sheet1')
# print(dt.loc[0:,'Ime'].loc[dt.loc[0:,'Plata'].max()])
# print(dt.loc[0:'Ime'].loc[dt.loc[0:,'Plata'].max()])

print(dt.loc[0:,('Ime','Plata')].max())