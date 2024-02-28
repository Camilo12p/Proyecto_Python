import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def Agregar(srcData:dict):
    id=v.validateInt('id','personal')
    name=v.validateStr('nombre','personal')
    email= v.validateEmail()
    movil=v.validateInt('movil','personal')
    telCasa=v.validateInt('telefono de casa', 'personal')
    telPers=v.validateInt('telefono personal','personal')
    telOffice=v.validateInt('telefono de la oficna','personal')

    persona={
        'id':id,
        'name':name,
        'email':email,
        'telefonos':{
            'movil':movil,
            'casa':telCasa,
            'personal':telPers,
            'oficina':telOffice
        }
    }

    srcData.get('personas').update({id:persona})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar(srcData:dict):
    id=str(v.validateInt('id','personal','a editar'))
    menu=[['1. Nombre'],['2.Email'],['3. telefonos']]
    menu2=[['1.movil'],['2.Casa'],['3.Personal'],['4.Oficina']]
    
    if id not in srcData.get('personas'):
            print('El id no se encuentra en el sistema')
            return 

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='grid'))
        op=int(input('Seleccione una opcion --> '))

        
        if op == 1:
            srcData.get('personas').get(id)['name']=v.validateStr('nombre','personal','a editar')
            isOption=False
        elif op==2:
            srcData.get('personas').get(id)['email']=v.validateEmail('a editar')
            isOption=False
        elif op == 3:
            print(tabulate(menu2,tablefmt='grid'))
            op2=int(input('Seleccione una opcion --> '))
            if op2==1:
                srcData.get('personas').get(id)['telefonos']['movil']=v.validateInt('movil','personal','a editar')
                isOption=False
            elif op2==2:
                srcData.get('personas').get(id)['telefonos']['casa']=v.validateInt('telefono de casa','personal','a editar')
                isOption=False
            elif op2==3:
                srcData.get('personas').get(id)['telefonos']['personal']=v.validateInt('telefono personal','personal','a editar')
                isOption=False
            elif op2==4:
                srcData.get('personas').get(id)['telefonos']['oficina']=v.validateInt('telefono de oficina','personal','a editar')
                isOption=False
            else:
                print('ingrese un valor valido')
        else:
            print('ingrese un valor valido')

    core.updateFile('Inventario_Campus.json',srcData)

def eliminar(srcData:dict):
    id=str(v.validateInt('id','personal','a eliminar'))
    if id not in srcData.get('personas'):
            print('El id no se encuentra en el sistema')
            return 
    srcData.get('personas').pop(id)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar(srcData:dict):
    id=str(v.validateInt('id','personal','a buscar'))
    if id not in srcData.get('personas'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('personas').get(id).items():
        print(f'{key}  : {value}')
