import sys
from tabulate import tabulate
import modulos.activos as ac
import modulos.zona as zo
import modulos.reportes as rp
import modulos.coreFile as core
import modulos.personal as p
import modulos.asignaciones as A
import modulos.movimientos as m
import modulos.validation as v


def menuPrincipal(srcData:dict):
    # def wrapper(func):  
    #     func
    #     menuPrincipal(Inventario_Campus)

    titulo='''

         __________________________________________
        |                                          |    
        |   SISTEMA G&C DE INVENTARIO CAMPUSLANDS  |
        |__________________________________________|

    '''

    menu=[['1. Activos'],['2. Personal'],['3. Zonas'],['4. Asignacion'],['5. Reportes'],['6. Movimiento de activos'],['7. Salir'],]
    
    isOption=True
    while isOption:   
        try:
            core.clearScreen()
            op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
            if op==1:
                menuActivos(srcData)
            elif op==2:
                menuPesonal(srcData)
                pass
            elif op==3:
                menuZonas(srcData)
            elif op==4:
                menuAsignacion(srcData)
            elif op==5:
                menuReportes(srcData)
            elif op==6:
                menuMovimientos(srcData)
            elif op==7:
                sys.exit("Vuelva pronto, Bye Bye ")


        except EOFError:
            print('El valor ingresado no es valido ')
            core.pauseScreen()
        except KeyboardInterrupt:
            print('Acabas de cancelar el programa')
            core.pauseScreen()

def menuActivos(srcData:dict):
    titulo='''

         ___________________________________
        |                                   |    
        |  Menu Administracion de activos   |
        |___________________________________|

    '''

    menu=[['1. Agregar'],['2. Editar'],['3. Eliminar'],['4. Buscar'],['5. Regresar al menu']]
    
    isOption=True
    while isOption: 
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            ac.DictActivos()
            core.pauseScreen()
        elif op==2:
            ac.Editar()
            core.pauseScreen()
        elif op==3:
            ac.eliminar()
            core.pauseScreen()
        elif op==4:
            ac.buscar()
            core.pauseScreen()
        elif op==5:
            isOption=False
            menuPrincipal(srcData)

def menuPesonal(srcData:dict):
    titulo='''

         ___________________________________
        |                                   |    
        |  Menu Administracion de personal  |
        |___________________________________|

    '''

    menu=[['1. Agregar'],['2. Editar'],['3. Eliminar'],['4. Buscar'],['5. Regresar al menu']]
    
    isOption=True
    while isOption: 
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            p.Agregar()
            core.pauseScreen()
        elif op==2:
            p.Editar()
            core.pauseScreen()
        elif op==3:
            p.eliminar()
            core.pauseScreen()
        elif op==4:
            p.buscar()
            core.pauseScreen()
        elif op==5:
            isOption=False
            menuPrincipal(srcData)

def menuZonas(srcData:dict):
    titulo='''

         _________________________________
        |                                 |    
        |  Menu Administracion de zonas   |
        |_________________________________|

    '''

    menu=[['1. Agregar'],['2. Editar'],['3. Eliminar'],['4. Buscar'],['5. Regresar al menu']]
    
    isOption=True
    while isOption: 
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            zo.CrearZona()
            core.pauseScreen()
        elif op==2:
            zo.Editar()
            core.pauseScreen()
        elif op==3:
            zo.eliminar()
            core.pauseScreen()
        elif op==4:
            zo.buscar()
            core.pauseScreen()
        elif op==5:
            isOption=False
            menuPrincipal(srcData)



def menuAsignacion(srcData:dict):
    titulo='''

         ____________________________
        |                            |    
        |    Menu de asignaciones    |
        |____________________________|

    '''

    menu=[['1. Crear Asignacion'],['2. Buscar Asignacion'],['3. Regresar a menu principal']]
    
    isOption=True
    while isOption: 
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            A.CrearAsignacion()
            core.pauseScreen()
        elif op==2:
            rp.listarAsignacion()
            core.pauseScreen()
        elif op==3:
            isOption=False
            menuPrincipal(srcData)
def menuReportes(srcData:dict):
    titulo="""
         ____________________________
        |                            |    
        |      Menu de reportes      |
        |____________________________|
    
    """
    menu=[['1. Listar todo los activos '],['2. Listar activos por categoria '],['3. Listar activos dados de baja por daños '],['4. Listar activos y asignacion'],['5. Listar historial de mov del activo'],['6. Regresar al menu principal']]
    isOption=True
    while isOption:
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            rp.ListarActivos()
        elif op==2:
            rp.ListarPorCategoria()
        elif op==3:
            rp.ListarActivosBaja()
        elif op==4:
            rp.listarAsignacion()
        elif op==5:
            rp.ListarActivosHistorial()
        elif op==6:
            isOption=False
            menuPrincipal(srcData)
            
    
    
def menuMovimientos(srcData:dict):
    titulo='''

         ____________________________
        |                            |    
        |    Menu de movimientos     |
        |____________________________|

    '''

    menu=[['1. Retornos de Activos'],['2. Dar de baja activo'],['3. Cambiar asignacion de activo'],['4. Enviar a garantia activo'],['5. Regresar a menu']]
    isOption=True
    while isOption: 
        core.clearScreen()
        op=v.validateOpciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        if op==1:
            m.retornos()
            core.pauseScreen()
        elif op==2:
            m.darBaja()
            core.pauseScreen()
        elif op==3:
            m.cambiarAsignacion()
            core.pauseScreen()
        elif op==4:
            m.enviarGarantia()
            core.pauseScreen()
        elif op==5:
            isOption=False
            menuPrincipal(srcData)