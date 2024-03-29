#Este es el modulo para la creacion, asignacion, edicion, eliminacion y busqueda de zonas disponibles
import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate
#esta es la funcion para crear una zona
def CrearZona():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
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
#aqui se edita una de las zonas ya existentes
def Editar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
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
        op=v.validateOpciones('Ingrese una opcion',tabulate(menu,tablefmt='fancy_grid'))

        
        if op == 1:
            srcData.get('Zonas').get(id2)['NombreZona']=v.validateStr('Ingrese el nombre de la zona ').capitalize()
            isOption=False
        elif op==2:
            srcData.get('Zonas').get(id2)['TotalCapacidad']=v.validateInt(' Ingrese la capacidad total')
            isOption=False
        else:
            print('Ingrese un valor valido')

        core.updateFile('Inventario_Campus.json',srcData)
#aqui se elimina alguna de las zonas ya existentes
def eliminar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
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
#con esta funcion se busca una de las zonas ya creadas
def buscar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
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
