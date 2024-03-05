import os 
from modulos.coreFile import updateFile,readFile,clearScreen

def validateInt(context:str):
    clearScreen()
    try:
        num=int(input(context +' --> '))
        if num>=0 and num<=10000000000000:
            return num
        else:
            return validateInt(context)
    except ValueError:
        return validateInt(context)

def validateFloat(context:str):
    try:
        num=float(input(context +' --> '))
        if num>=0 and num<=10000000000000:
            return num
        else:
            return validateFloat(context)
    except ValueError:
        return validateFloat(context)

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
        return validateExit(context)

def validateEmail(context:str):
    clearScreen()
    e=input(context+ ' --> ')
    if e.isalnum():
        if len(e.split())<=2:
            return validateEmail(context)
    else:
        return ''.join(e)

def validatePrestamo(srcData:dict,id:int):
    srcData.update(readFile('Inventario_Campus.json'))
    for key,value in srcData.get('Asignacion').items():
        if (value['asignadoA'])==str(id):
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

def codcampus(context:str):
    clearScreen()
    nombre=str(input(f'{context} --> ')).upper()
    if len(nombre.split())<=15 and nombre.isalnum():
        return "".join(nombre)
    else:
        return codcampus(context)

def validateOpciones(context:str,titulo='',titulo2=''):
    clearScreen()
    print(titulo)
    print(titulo2)
    try:
        num=int(input(context +' --> '))
        if num>=0 and num<=15:
            return num
        else:
            return validateOpciones(context,titulo,titulo2)
    except ValueError:
        return validateOpciones(context,titulo,titulo2)

def nombreActivo(context:str):
    n=str(input(f'{context} --> '))
    if len(n.split())<=2 and n.isalnum():
        return "".join(n)
        
    else: 
        return nombreActivo(context)
