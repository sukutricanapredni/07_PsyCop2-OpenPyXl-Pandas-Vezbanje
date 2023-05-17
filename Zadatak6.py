import pandas as pd

dt=pd.read_csv('data.csv')
print(dt)


p=pd.DataFrame({'Ime':['Marko','MIljan','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Nikolic','Milovanovic','Ilic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,4,1,2],
                   'Razred':[5,6,7,8,7,6]})

#   p.to_csv('fajl.csv')  OVAKO UPISUJE I INDEKSE
p.to_csv('fajl.csv',index=False)        
dt=pd.read_csv('fajl.csv')
print(dt)