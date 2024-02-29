import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def DictActivos(srcData:dict):
    CodTransaccion=v.validateInt('Codigo de transaccion','activo')
    NroFormulario=v.validateInt('Nro de Formulario','activo')
    CodCampus= v.validateInt('Cod Campus','activo')
    Marca=v.validateStr('Marca','activo')
    Categoria=v.validateStr('Categoria', 'activo')
    Tipo=v.validateStr('Tipo','activo')
    ValorUnitario=v.validateStr('Valor Unitario','activo')
    Proveedor=v.validateStr('Proveedor','activo')
    NroSerial=v.validateInt('Nro de serial','activo')
    EmpresaResponsable=v.validateStr('Nombre del al empresa responsable ','activo')
    ValorUnitario=v.validateStr('Valor Unitario ','activo')
    persona={
        'CodTransaccion':CodTransaccion,
        'Nroformulario':NroFormulario,
        'Codcampus':CodCampus,
        'Marca':Marca,
        'Categoria':Categoria,
        'Tipo':Tipo,
        'ValorUnitario':ValorUnitario,
        'Proveedor':Proveedor,
        'Nroserial':NroSerial,
        'EmpresaResponsable':EmpresaResponsable,
        'Estado':0,
        'Historial':{}
        }
    

    srcData.get('Activos').update({CodCampus:DictActivos})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar(srcData:dict):
    id=str(v.validateInt('id','personal','a editar'))
    menu=[['1. Nombre'],['2.Email'],['3. telefonos']]
    menu2=[['1.movil'],['2.Casa'],['3.Personal'],['4.Oficina']]
    
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return 

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=int(input('Seleccione una opcion --> '))

        
        if op == 1:
            srcData.get('Personas').get(id)['name']=v.validateStr('nombre','personal','a editar')
            isOption=False
        elif op==2:
            srcData.get('Personas').get(id)['email']=v.validateEmail('a editar')
            isOption=False
        elif op == 3:
            print(tabulate(menu2,tablefmt='fancy_grid'))
            op2=int(input('Seleccione una opcion --> '))
            if op2==1:
                srcData.get('Personas').get(id)['telefonos']['movil']=v.validateInt('movil','personal','a editar')
                isOption=False
            elif op2==2:
                srcData.get('Personas').get(id)['telefonos']['casa']=v.validateInt('telefono de casa','personal','a editar')
                isOption=False
            elif op2==3:
                srcData.get('Personas').get(id)['telefonos']['personal']=v.validateInt('telefono personal','personal','a editar')
                isOption=False
            elif op2==4:
                srcData.get('Personas').get(id)['telefonos']['oficina']=v.validateInt('telefono de oficina','personal','a editar')
                isOption=False
            else:
                print('ingrese un valor valido')
        else:
            print('ingrese un valor valido')

    core.updateFile('Inventario_Campus.json',srcData)

def eliminar(srcData:dict):
    id=str(v.validateInt('id','personal','a eliminar'))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return 
    srcData.get('Personas').pop(id)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar(srcData:dict):
    id=str(v.validateInt('id','personal','a buscar'))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Personas').get(id).items():
        print(f'{key}  : {value}')