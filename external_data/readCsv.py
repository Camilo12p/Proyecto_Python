from csv import reader
from modulos.coreFile import updateFile

data=[]


    
def readCsv(Inventario_Campus:dict):
    with open('external_data/baseDatos.csv', 'r') as br:
        lector=reader(br)
        for row in lector:
            categoria=row[5].split('-')
            activo={
                'codTransaccion':row[1],
                'nroformulario':row[4],
                'codcampus':row[3],
                'nombre':row[5],
                'marca':'compumax',
                'categoria':'equipo de computo',
                'tipo':categoria[0],
                'valor unitario':2000,
                'proveedor':row[7],
                'nroserial':row[2],
                'empresaresponsable':row[8],
                'estado':0
            }

            Inventario_Campus.get('Activos').update({len(Inventario_Campus.get('Activos')):activo})
        updateFile('Inventario_Campus.json',Inventario_Campus)
