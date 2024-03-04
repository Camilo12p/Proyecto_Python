from csv import reader
from modulos.coreFile import updateFile

data=[]

def readCsv(Inventario_Campus:dict):
    valorUnitario=[1000,2000,3000]
    cantidad=[1,1,1,1]   #[teclado,monitor,cpu,mouse]
    
    valor=0
    with open('external_data/baseDatos.csv', 'r') as br:
        lector=reader(br)
        for row in lector:
            id=''
            categoria=row[5].split('-')
            if categoria[0].strip() == 'Teclado':
                valor=250
                id='TE' + str(cantidad[0]).zfill(4)
                cantidad[0]+=1

            elif categoria[0].strip() == 'Monitor':
                valor=500
                id='MON' + str(cantidad[1]).zfill(4)
                cantidad[1]+=1

            elif categoria[0].strip() == 'CPU':
                valor=1500
                id='CP' + str(cantidad[2]).zfill(4)
                cantidad[2]+=1
            elif categoria[0].strip() == 'Mouse':
                valor=100
                id='MO' + str(cantidad[3]).zfill(4)
                cantidad[3]+=1

            activo={
                'codTransaccion':row[1],
                'nroformulario':row[4],
                'codcampus':id,
                'nombre':row[5],
                'marca':'Compumax',
                'categoria':'Equipo de computo',
                'tipo':categoria[0],
                'valorUnitario':valor,
                'proveedor':row[7],
                'nroserial':row[2],
                'empresaresponsable':row[8],
                'estado':0,
                'historial':{}
            }
            Inventario_Campus.get('Activos').update({id:activo})
        updateFile('Inventario_Campus.json',Inventario_Campus)
