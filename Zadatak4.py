import pandas as pd

dt=pd.read_excel('test.xlsx',sheet_name='Sheet1')   # importuje excel tabelu u DataFrame
print(dt)


p=pd.DataFrame({'Ime':['Marko','MIljan','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Nikolic','Milovanovic','Ilic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,4,1,2],
                   'Razred':[5,6,7,8,7,6]})

p.to_excel('test1.xlsx',index=False)        # expotruje iy DataFrame u excel

dcsv=pd.read_csv('data.csv')            #   ucitavanje CSV fajlova
print(dcsv)

djason=pd.read_json('data.json')        #   ucitavanje Jason fajlova
print(dcsv)

