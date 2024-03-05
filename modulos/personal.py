import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate
#Esta es la funcion para agregar personal 
def Agregar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=v.validateInt('Ingrese el C.C. de la persona')  #Aqui el programa valida que la informacion que se ingreso como CC sea numeros solamente
    if v.newRegister(str(id),'Personas'):
        return
    #toda esta seccion es para ir guardando al informacion en cada variable de la informacion que se pide para el personal
    name=v.validateStr('Ingrese el nombre de la persona')                
    email= v.validateEmail('Ingrese el email')
    movil=v.validateInt('Ingrese el movil de la persona')
    telCasa=v.validateInt('Ingrese el telefono de casa de la persona')
    telPers=v.validateInt('Ingrese el telefono personal de la persona')
    telOffice=v.validateInt('Ingrese el telefono de la oficna de la persona')

    persona={
        'id':id,
        'name':name,
        'email':email,
        'telefonos':{
            'movil':movil,
            'casa':telCasa,
            'personal':telPers,
            'oficina':telOffice
        },
        'Prestamo':False
    }

    srcData.get('Personas').update({id:persona})
    core.updateFile('Inventario_Campus.json',srcData)
#Esta es la funcion pora editar el personal, se puede editar cualquiera de la informacion requerida
def Editar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(v.validateInt('Ingrese el id de la persona a editar'))
    menu=[['1. Nombre'],['2.Email'],['3. telefonos']]
    menu2=[['1.movil'],['2.Casa'],['3.Personal'],['4.Oficina']]
    
    if id not in srcData.get('Personas'):   #aqui se valida si el id esta o no dentro del sistema de personas
            print('El id no se encuentra en el sistema')
            return 

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateOpciones('Ingrese una opcion',tabulate(menu,tablefmt='fancy_grid'))        
        if op == 1:
            srcData.get('Personas').get(id)['name']=v.validateStr('Ingrese el nombre')
            isOption=False
        elif op==2:
            srcData.get('Personas').get(id)['email']=v.validateEmail('Ingrese el email')
            isOption=False
        elif op == 3:
            print(tabulate(menu2,tablefmt='fancy_grid'))
            op2=v.validateOpciones('Ingrese una opcion',tabulate(menu2,tablefmt='fancy_grid'))
            if op2==1:
                srcData.get('Personas').get(id)['telefonos']['movil']=v.validateInt('Ingrese el movil')
                isOption=False
            elif op2==2:
                srcData.get('Personas').get(id)['telefonos']['casa']=v.validateInt('Ingrese el telefono')
                isOption=False
            elif op2==3:
                srcData.get('Personas').get(id)['telefonos']['personal']=v.validateInt('Ingrese el telefono personal')
                isOption=False
            elif op2==4:
                srcData.get('Personas').get(id)['telefonos']['oficina']=v.validateInt('Ingrese el telefono de oficina')
                isOption=False
            else:
                print('ingrese un valor valido')
        else:
            print('ingrese un valor valido')

    core.updateFile('Inventario_Campus.json',srcData)
#Funcion para eliminar personal de la base
def eliminar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(v.validateInt('Ingrese el id de la persona a eliminar'))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return 
    if not srcData.get('Personas').get(str(id))['Prestamo']:
        srcData.get('Personas').pop(id)
    else:
        print('No se puede eliminar la persona porque tiene un prestamo')
    core.updateFile('Inventario_Campus.json',srcData)
#Funcion para buscar un personal que ya existe dentro de la base
def buscar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(v.validateInt('id de la persona a buscar'))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Personas').get(id).items():
        print(f'{key}  : {value}')
