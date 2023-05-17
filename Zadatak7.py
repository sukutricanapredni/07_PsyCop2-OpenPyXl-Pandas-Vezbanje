import pandas as pd
import openpyxl as op
dt=pd.read_csv('data.csv')
print('Prosecan puls:',dt.loc[0:,('Pulse')].mean())

dt1=pd.read_csv('fajl.csv')
print('Najmanja ocena:', dt1.loc[0:,('Ocena')].min())
print('Najveca ocena:', dt1.loc[0:,('Ocena')].max())
print(dt1.loc[0:,'Ocena'].agg(['min','max']))

dt2=pd.read_excel('test.xlsx',sheet_name='Sheet1')   
print(dt2)
dt2.to_csv('file1.csv',index=False)

wb=op.load_workbook('test1.xlsx')
ws=wb.active
def popuni_recnik(kolona):
    ime=ws[kolona]
    r_ime={}
    r_ime[ime[0].value]=[]
    for i in range(1,len(ime)):
        r_ime[ime[0].value].append(ime[i].value)
    return r_ime

r_ime=popuni_recnik('A')
r_prezime=popuni_recnik('B')
r_ocena=popuni_recnik('C')
r_razred=popuni_recnik('D')

print(r_ime,r_prezime,r_ocena,r_razred)
r={}
r.update(r_ime)
r.update(r_prezime)
r.update(r_ocena)
r.update(r_razred)
r.update(r.odeljenje)

#r=r_ime|r_prezime|r_plata

d=pd.DataFrame(r)
print(d)


dt4=pd.read_csv('fajl.csv')
print(dt4)
r_odeljenje={'Odeljenje':[1,1,2,3,4,5]}
