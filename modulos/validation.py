#Este es el modulo para las validaciones utilizadas en todo el programa
import os 
from modulos.coreFile import updateFile,readFile,clearScreen
#esta es la validacion para validar que la informacion ingresada por el usuario sa de solo numeros 
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
#esta es la validacion para que los valores ingresados los compare con numeros flotantes o decimales
def validateFloat(context:str):
    try:
        num=float(input(context +' --> '))
        if num>=0 and num<=10000000000000:
            return num
        else:
            return validateFloat(context)
    except ValueError:
        return validateFloat(context)
#Esta es la validacion para solo texto
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
#esta es la validacion para salir de la ejecucion
def validateExit(context:str):
    n=str(input(context + ' --> '))
    if n.isalpha() or n=='':
        return n
    else:
        return validateExit(context)
#esta es la validacion para que cuando el usuario ingrese un correo, contenga @ para que cuente como email
def validateEmail(context:str):
    clearScreen()
    e=input(context+ ' --> ')
    if e.isalnum():
        if len(e.split())<=2:
            return validateEmail(context)
    else:
        return ''.join(e)
#esta es la validacion para saber si un activo ya esta en prestamo a un personal
def validatePrestamo(srcData:dict,id:int):
    srcData.update(readFile('Inventario_Campus.json'))
    for key,value in srcData.get('Asignacion').items():
        if (value['asignadoA'])==str(id) and type(id)==int:
            srcData.get('Personas').get(str(id))['Prestamo']=True
            break
        else:
            if type(id)==int:
                srcData.get('Personas').get(str(id))['Prestamo']=False    

    updateFile('Inventario_Campus.json',srcData)

#aqui se valida si la asignacion es valida
def validateAsignacion(srcData:dict):
    for key,value in srcData.get('Asignacion').items():
        if len(value['activos']) ==0:
            srcData.get('Asignacion').pop(key)
            break
    updateFile('Inventario_Campus.json',srcData)

#aqui se valida si el id esta registrado o no
def newRegister(id:str,tipo:str):
    data={}
    data.update(readFile('Inventario_Campus.json'))
    if id in data.get(tipo):
        print(f'El {tipo} ya se encuentra registrado')
        return True
#esta es la validacion para saber si una zona esta o no registrada
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

def validateOpciones2(context:str)->str:
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
