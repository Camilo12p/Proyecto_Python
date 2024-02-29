import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def DictActivos(srcData:dict):
    CodTransaccion=v.validateInt('Ingrese el codigo de transaccion del activo')
    NroFormulario=v.validateInt('Ingrese el Nro de formulario del activo')
    CodCampus= v.validateInt('Ingrese el codigo de campus del activo')
    Marca=v.validateStr('Ingrese la marca del activo')
    Categoria=v.validateStr('Ingrese la categoria del activo')
    Tipo=v.validateStr('Ingrese el tipo del activo')
    ValorUnitario=v.validateInt('Ingrese el valor unitario del activo')
    Proveedor=v.validateStr('Ingrese el proveedor del activo')
    NroSerial=v.validateInt('Ingrese el numero serial del activo')
    EmpresaResponsable=v.validateStr('Ingrese la empresa responsable del activo')
    Nombre=input('Ingrese el nombre completo del activo')
                            
    activo={
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
        'Historial':{},
        'Nombre':Nombre
        }
    

    srcData.get('Activos').update({CodCampus:activo})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar(srcData:dict):
    id=str(input('Ingrese el codigo de campus del activo a editar'))
    menu=[['1. Codigo de transaccion'],['2. Numero de formulario'],['4. Marca']['5. Categoria']['6. Tipo']['7. Valor unitario']['8. Proveedor']['9. Numero serial']['10. Empresa Resposable']]
    
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Seleccione una opcion valida --> ')

        
        if op == 1:
            srcData.get('Activos').get(id)['CodTransaccion']=v.validateInt('Ingrese el Codigo de transaccion del activo a editar ')
            isOption=False
        elif op==2:
            srcData.get('Activos').get(id)['Nroformulario']=v.validateInt(' Ingrese el numero de formulario del activo a editar ')
            isOption=False
        elif op == 3:
            srcData.get('Activos').get(id)['CodCampus']=input('Ingrese el codigo de campus del activo')
            isOption=False    
        elif op==4:
            srcData.get('Activos').get(id)['Marca']=v.validateStr(' Ingrese la marca del activo ')
            isOption=False
        elif op==5:
            srcData.get('Activos').get(id)['Categoria']=v.validateStr(' Ingrese la categoria del activo ')
            isOption=False
        elif op==6:
            srcData.get('Activos').get(id)['Tipo']=v.validateStr('Ingrese el tipo de activo')
            isOption=False
        elif op==7:
            srcData.get('Activos').get(id)['ValorUnitario']=v.validateInt('Ingrese el valor unitario')
            isOption=False
        elif op==8:
            srcData.get('Activos').get(id)['Proveedor']=v.validateStr('Ingrese el nombre del proveedor')
            isOption=False
        elif op==6:
            srcData.get('Activos').get(id)['Nroserial']=v.validateStr('Ingrese el numero serial del activo')
            isOption=False
        elif op==6:
            srcData.get('Activos').get(id)['EmpresaResponsable']=v.validateStr('Ingrese el nombre de la empresa responsable')
            isOption=False
        elif op==6:
            srcData.get('Activos').get(id)['Nombre']=v.validateStr('Ingrese el nombre del activo')
            isOption=False
        else:
            print('Ingrese un valor valido')
       

    core.updateFile('Inventario_Campus.json',srcData)

def eliminar(srcData:dict):
    id=str(input('Ingrese el activo a eliminar'))
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 
    srcData.get('Activos').pop(id)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar(srcData:dict):
    id=str(input('Ingrese el activo a buscar'))
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Activos').get(id).items():
        print(f'{key}  : {value}')