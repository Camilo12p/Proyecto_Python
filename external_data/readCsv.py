from csv import reader

data=[]

with open('external_data/baseDatos.csv', 'r') as br:
    lector=reader(br)
    for row in lector:
        data.append(row)

print(ddata)