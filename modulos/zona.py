import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def CrearZona(srcData:dict):
    NombreZona=v.validateStr('Ingrese el nombre de la zona').capitalize()
    if v.newRegisterZona(NombreZona,'Zonas'):
        return
    TotalCapacidad= v.validateInt('Ingrese la capacidad total')
    nrozona=len(srcData.get('Zonas'))+1
    Zona={
        'NombreZona':NombreZona,
        'TotalCapacidad':TotalCapacidad,
        'NroZona':nrozona
        }    

    srcData.get('Zonas').update({nrozona:Zona})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar(srcData:dict):
    id=v.validateStr('Ingrese el nombre de la zona a editar').capitalize()
    menu=[['1. Nombre de la zona'],['2. Total Capacidad de la zona']]
    id2=0

    r=0
    for key,value in srcData.get('Zonas').items():
        if id == value['NombreZona']:
                id2=key
                r=0
                break
        else:
            r=1
    if r==1:
        print('El id no se encuentra en el sistema')
        return

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Seleccione una opcion valida')

        
        if op == 1:
            srcData.get('Zonas').get(id2)['NombreZona']=v.validateStr('Ingrese el nombre de la zona ').capitalize()
            isOption=False
        elif op==2:
            srcData.get('Zonas').get(id2)['TotalCapacidad']=v.validateInt(' Ingrese la capacidad total')
            isOption=False
        else:
            print('Ingrese un valor valido')

        core.updateFile('Inventario_Campus.json',srcData)

def eliminar(srcData:dict):
    id2=0
    id=v.validateStr('Ingrese la zona a eliminar').capitalize()
    r=0
    for key,value in srcData.get('Zonas').items():
        if id == value['NombreZona']:
                id2=key
                r=0
                break
        else:
            r=1

    if r==1:
        print('El id no se encuentra en el sistema')
        return
    srcData.get('Zonas').pop(id2)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar(srcData:dict):
    id2=0
    id=v.validateStr('Ingrese la zona a buscar').capitalize()
    r=0
    for key,value in srcData.get('Zonas').items():
        if id == value['NombreZona']:
                id2=key
                r=0
                break
                
        else:
            
            r=1
    if r==1:
        print('El id no se encuentra en el sistema')
        return
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Zonas').get(id2).items():
        print(f'{key}  : {value}')
