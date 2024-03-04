import os 
from modulos.coreFile import updateFile,readFile,clearScreen

def validateInt(context:str):
    try:
        num=int(input(context +' --> '))
        if num>=0:
            return num
        else:
            return validateInt(context)
    except ValueError:
        return validateInt(context)

def validateFloat(contex:str):
    try:
        num=float(input(context +' --> '))
        if num>=0:
            return num
        else:
            return validateInt(context)
    except ValueError:
        return validateInt(context)

def validateStr(context:str):
    r=0
    clearScreen()
    n=str(input(context + ' --> ')).split(' ')
    for item in n:
        if item.isalpha():
            n2=" ".join(n)
            pass
        else:
            r=1
            return validateStr(context)
    if r==0:
        return n2

def validateExit(context:str):
    n=str(input(context + ' --> '))
    if n.isalpha() or n=='':
        return n
    else:
        return validateStr(context)

def validateEmail(context:str):
    clearScreen()
    e=input(context+ ' --> ')
    if e.isalnum():
        return validateEmail(context)
    else:
        return e

def validatePrestamo(srcData:dict,id:int):
    for key,value in srcData.get('Asignacion').items():
        if int(value['asignadoA'])==id:
            srcData.get('Personas').get(str(id))['Prestamo']=True
            break
        else:
            srcData.get('Personas').get(str(id))['Prestamo']=False    

    updateFile('Inventario_Campus.json',srcData)


def validateAsignacion(srcData:dict):
    for key,value in srcData.get('Asignacion').items():
        if len(value['activos']) ==0:
            srcData.get('Asignacion').pop(key)
            break
    updateFile('Inventario_Campus.json',srcData)


def newRegister(id:str,tipo:str):
    data={}
    data.update(readFile('Inventario_Campus.json'))
    if id in data.get(tipo):
        print(f'El {tipo} ya se encuentra registrado')
        return True

def newRegisterZona(id:str,tipo:str):
    data={}
    data.update(readFile('Inventario_Campus.json'))
    for key,value in data.get(tipo).items():
        if id in value['NombreZona']:
            print(f'El {tipo} ya se encuentra registrado')
            return True