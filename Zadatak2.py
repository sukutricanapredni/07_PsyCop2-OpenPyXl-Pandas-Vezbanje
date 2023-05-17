import pandas as panda

p=panda.DataFrame({'Ime':['Nikola'],'Prezime':['Savic']})

p.loc[len(p)]=['Marko','Kacarevic']     # dodavanje reda u DataFrame, len se dodaje da bi sew oznacio red na koji se dodaje

p.drop(1,axis=0,inplace=True)                           # izbacuje red '0' oznacava red

p.drop('Prezime',axis=1,inplace=True)                   # izbacuje kolonu '1' oznacava kolonu
print(p)
