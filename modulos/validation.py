import os 
from modulos.coreFile import updateFile

def validateInt(context:str):
    try:
        num=int(input(context +' --> '))
        if num>=0:
            return num
        else:
            return validateInt(context)
    except ValueError:
        return validateInt(context)


def validateStr(context:str):
    n=str(input(context + ' --> '))
    if n.isalpha():
        return n
    else:
        return validateStr(context)

def validateEmail(context:str):
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

    updateFile('Inventario.json',srcData)