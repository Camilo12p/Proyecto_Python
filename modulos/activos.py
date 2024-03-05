import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate

def asignartipo()->str:
    core.clearScreen()
    titulo='Seleccione el tipo de activo: '
    tipos=['Teclado','Mouse','Monitor','CPU']
    titulo2=[['1. Teclado'],['2. Mouse'],['3. Monitor'],['4. CPU']]
    print(tabulate(tipos,tablefmt='fancy_grid'))
    op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(titulo2,tablefmt='fancy_grid'))
    if op>0 and op<4:
        return tipos[op-1]
    else: 
        return asignartipo()

def DictActivos():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    CodCampus= v.codcampus('Ingrese el codigo de campus')
    if v.newRegister(CodCampus,'Activos'):
        return
    CodTransaccion=v.validateInt('Ingrese el codigo de transaccion del activo')
    NroFormulario=v.validateInt('Ingrese el Nro de formulario del activo')
    Marca=v.validateStr('Ingrese la marca del activo')
    Tipo=asignartipo()
    ValorUnitario=v.validateFloat('Ingrese el valor unitario del activo')
    Proveedor=v.validateStr('Ingrese el proveedor del activo')
    NroSerial=v.nombreActivo('Ingrese el numero serial del activo')
    EmpresaResponsable=v.validateStr('Ingrese la empresa responsable del activo')
    Nombre=input('Ingrese el nombre completo del activo')
                            
    activo={
        'codTransaccion':CodTransaccion,
        'nroformulario':NroFormulario,
        'codcampus':CodCampus,
        'nombre':Nombre,
        'marca':Marca,
        'categoria':'Equipo de computo',
        'tipo':Tipo,
        'valorUnitario':ValorUnitario,
        'proveedor':Proveedor,
        'nroserial':NroSerial,
        'empresaResponsable':EmpresaResponsable,
        'estado':0,
        'historial':{}
        
        }
    

    srcData.get('Activos').update({CodCampus:activo})
    core.updateFile('Inventario_Campus.json',srcData)

def Editar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(input('Ingrese el codigo de campus del activo a editar')).upper()
    menu=[['1. Codigo de transaccion'],['2. Numero de formulario'],['3. Marca'],['4. Tipo'],['5. Valor unitario'],['6. Proveedor'],['7. Numero serial'],['8. Empresa Resposable'],['9.Nombre']]
    
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 

    isOption=True
    while isOption:

        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateOpciones('Ingrese una opcion',tabulate(menu,tablefmt='fancy_grid'))

        
        if op == 1:
            srcData.get('Activos').get(id)['codTransaccion']=v.validateInt('Ingrese el Codigo de transaccion del activo a editar ')
            isOption=False
        elif op==2:
            srcData.get('Activos').get(id)['nroformulario']=v.validateInt(' Ingrese el numero de formulario del activo a editar ')
            isOption=False  
        elif op==3:
            srcData.get('Activos').get(id)['marca']=v.validateStr(' Ingrese la marca del activo ')
            isOption=False
        elif op==4:
            srcData.get('Activos').get(id)['tipo']=v.validateStr('Ingrese el tipo de activo')
            isOption=False
        elif op==5:
            srcData.get('Activos').get(id)['valorUnitario']=v.validateFloat('Ingrese el valor unitario')
            isOption=False
        elif op==6:
            srcData.get('Activos').get(id)['proveedor']=v.validateStr('Ingrese el nombre del proveedor')
            isOption=False
        elif op==7:
            srcData.get('Activos').get(id)['nroserial']=v.nombreActivo('Ingrese el numero serial del activo')
            isOption=False
        elif op==8:
            srcData.get('Activos').get(id)['empresaResponsable']=v.validateStr('Ingrese el nombre de la empresa responsable')
            isOption=False
        elif op==9:
            srcData.get('Activos').get(id)['nombre']=v.nombreActivo('Ingrese el nombre del activo')
            isOption=False
        else:
            print('Ingrese un valor valido')

    core.updateFile('Inventario_Campus.json',srcData)

def eliminar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(input('Ingrese el activo a eliminar')).upper()
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 
    srcData.get('Activos').pop(id)
    core.updateFile('Inventario_Campus.json',srcData)

def buscar():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id=str(input('Ingrese el activo a buscar')).upper()
    if id not in srcData.get('Activos'):
            print('El id no se encuentra en el sistema')
            return 
    print()
    print('-------------------------------')
    
    for key,value in srcData.get('Activos').get(id).items():
        print(f'{key}  : {value}')