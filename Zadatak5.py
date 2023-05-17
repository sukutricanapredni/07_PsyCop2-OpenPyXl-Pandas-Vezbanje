import pandas as pd


dt=pd.read_json('data.json')
print(dt)

p=pd.DataFrame({'Ime':['Marko','MIljan','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Nikolic','Milovanovic','Ilic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,4,1,2],
                   'Razred':[5,6,7,8,7,6]})

p.to_json('data1.json',orient='split',compression='infer')

dt=pd.read_json('data1.json',orient='split',compression='infer')
print(dt)
