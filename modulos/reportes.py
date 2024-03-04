import modulos.coreFile as core
import modulos.validation as v
from tabulate import tabulate


def ListarActivos(srcData:dict):
    Activos = []
    for key,value in srcData.get("Activos").items():
        Activos.append([value["codcampus"],value["nombre"],value["categoria"],value["tipo"],value["estado"]])
    headers = ["codcampus","nombre","categoria","tipo","estado"]
    print(tabulate(Activos,headers=headers, tablefmt="fancy_grid"))
    core.pauseScreen()

def ListarPorCategoria(srcData:dict):
    isOption=True
    while isOption: 
        core.clearScreen()
        print("Que categoria desea buscar")
        print("1. Equipo de computo\n2. Electrodomestico\n3. Juego\n4. Volver a reportes")
        op=v.validateInt('Ingrese una opcion --> ')
        if op==1:
            ListarActivosCategoria(srcData,"Equipo de computo")
            core.pauseScreen()
        elif op==2:
            ListarActivosCategoria(srcData,"Electrodomestico")
            core.pauseScreen()
        elif op==3:
            ListarActivosCategoria(srcData,"Juego")
            core.pauseScreen()
        elif op==4:
           pass
        elif op==5:
            ListarActivosHistorial(srcData,"historial")
            core.pauseScreen()
            
        
    

def ListarActivosCategoria(srcData:dict,categoria:str):
    Activos = []
    for key,value in srcData.get("Activos").items():
        if value["categoria"] == categoria:
            Activos.append([value["codcampus"],value["nombre"],value["categoria"],value["tipo"],value["estado"]])
    headers = ["codcampus","nombre","categoria","tipo","estado"]
    print(tabulate(Activos,headers=headers, tablefmt="fancy_grid"))
    core.clearScreen()
    
def ListarActivosBaja(srcData:dict):
    Activos = []
    for key,value in srcData.get("Activos").items():
        if value["estado"] == 2:
            Activos.append([value["codcampus"],value["nombre"],value["categoria"],value["tipo"],value["estado"]])
    headers = ["codcampus","nombre","categoria","tipo","estado"]
    core.clearScreen()
    print(tabulate(Activos,headers=headers, tablefmt="fancy_grid"))
    core.pauseScreen()

def ListarActivosHistorial(srcData:dict):
    core.clearScreen
    historial = []
    id = str(input("Ingrese el codigo de campus "))
    try:
        
        for key,value in srcData.get("Activos").get(id).get("historial").items():
            historial.append([value["NroHistorial"],value["fecha"],["tipoMov"],["idResponsable"]])
        headers= ["Nro Historial","Fecha","Tipo de movimiento","id del responsable"]
        core.clearScreen()
        print(tabulate(historial, headers=headers, tablefmt="fancy_grid"))
        core.pauseScreen()
    except AttributeError:
        print("El id no se encuentra registrado ")
        ListarActivosHistorial(srcData)
    
def listarAsignacion(srcData:dict):
    titulo='Que tipo de asignacion desea ver\n1.Personal\n2.Zonas\n'
    op=v.validateOpciones('Ingrese una opcion',titulo)
    if op==1:
        id=v.validateInt('Ingrese el id de la persona')
        for key,value in srcData.get('Asignacion').items():
            if id == value['asignadoA']:
                for key3,value3 in value['activos'].items():
                    print(f'{key3} . {value3}')
        core.pauseScreen()
    elif op==2:
        zonas=[]
        for key,value in srcData.get('Zonas').items():
            print(f'{key}.',value['NombreZona'])
            zonas.append(value['NombreZona'])

        op=v.validateOpciones('Ingrese una opcion')

        for key,value in srcData.get('Asignacion').items():
            if zonas[op-1] == (value['asignadoA']):
                for key3,value3 in value['activos'].items():
                    print(f'{key3} . {value3}')
        core.pauseScreen()
    else:
        print('Ingrese un valor valido')
        core.pauseScreen()