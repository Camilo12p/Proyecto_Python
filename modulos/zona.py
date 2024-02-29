import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def CrearZona(srcData:dict):
    NombreZona=v.validateStr('Ingrese el nombre de la zona')
    TotalCapacidad= v.validateInt('Ingrese la capacidad total')

    Zona={
        'NombreZona':NombreZona,
        'TotalCapacidad':TotalCapacidad,
        'NroZona':len(Zona)+1
        }    

    srcData.get('Zonas').update({len(Zona)+1:Zona})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar(srcData:dict):
    id=str(input('Ingrese la zona a editar'))
    menu=[['1. Nombre de la zona'],['2. Total Capacidad de la zona']]
    
    if id not in srcData.get('Zonas'):
            print('El id no se encuentra en el sistema')
            return
    
    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Seleccione una opcion valida  ')

        
        if op == 1:
            srcData.get('Zonas').get(id)['NombreZona']=v.validateStr('Ingrese el nombre de la zona ')
            isOption=False
        elif op==2:
            srcData.get('Zonas').get(id)['TotalCapacidad']=v.validateInt(' Ingrese la capacidad total')
                                                                 
            isOption=False
        else:
            print('Ingrese un valor valido')

        core.updateFile('Inventario_Campus.json',srcData)

def eliminar(srcData:dict):
    id=str(input('Ingrese la zona a eliminar'))
    if id not in srcData.get('Zonas'):
            print('El id no se encuentra en el sistema')
            return 
    srcData.get('Zonas').pop(id)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar(srcData:dict):
    id=str(input('Ingrese la zona a buscar'))
    if id not in srcData.get('Zonas'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Zonas').get(id).items():
        print(f'{key}  : {value}')
