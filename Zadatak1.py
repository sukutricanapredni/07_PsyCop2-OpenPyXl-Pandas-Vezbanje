import pandas as panda

# p=panda.DataFrame({'Ime':['Marko','MIljan','Stefan'],
#                    'Prezime':['Savic','Nikolic','Milovanovic']})
# print(p)

# print(p.iloc[0:2,0:1])  # stampa po indexu

# print(p.iloc[2,1]) # vadi clan

# print(p.loc[0:2,('Prezime',)]) #zarez ide zato sto je tuple, stampa sve iz kolone Prezime

p=panda.DataFrame({'Ime':['Marko','MIljan','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Nikolic','Milovanovic','Ilic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,4,1,2],
                   'Razred':[5,6,7,8,7,6]})
print(p.loc[0:2,('Ime','Prezime','Razred')])      # stampa samo izabrane kolone, ovde ne treba zarez, jebem li ga sto
print ('===========================')
print(p.head()) #prvih 5
print ('===========================')
print(p.tail()) #poslednjih 5
print ('===========================')
print ('===========================')
print(p.shape)          # vraca dimenziju tabele
print ('===========================')
print(p.describe())     # vraca sve funkcije koje poznajemo do sad
print ('===========================')
print(p.size)           # vraca broj celija
print ('===========================')
print(p.sum())          # sabira sve elemente reda
print ('===========================')
print('Ocena suma:',p.loc[0:,('Ocena')].sum())     # sabira sve ocene
print ('===========================')
print ('===========================')
print(p.loc[0:,('Ocena')]) 
print ('===========================')    
print(p.loc[-1:,('Ocena')])         # poslednja ocena
print ('===========================')
print('Ocena poslednja:',p.loc[:1,('Ocena')])         # poslednja ocena
print ('===========================')
print('Ocena prosek:',p.loc[0:,('Ocena')].mean())     # sabira sve ocene
print ('===========================')
print('Ocena min:',p.loc[0:,('Ocena')].min())     # 
print ('===========================')
print('Ocena max:',p.loc[0:,('Ocena')].max())     # 
