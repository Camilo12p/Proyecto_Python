import sys
import os
import modulos.coreFile as core
import modulos.personal as p
import modulos.asignaciones as A
import modulos.movimientos as m
import modulos.validation as v
from tabulate import tabulate

def menuPrincipal(srcData:dict):
    
    # def wrapper(func):  
    #     func
    #     menuPrincipal(Inventario_Campus)

    titulo='''

         _______________________________
        |                               |    
        |  Menu de asignacion de Campus |
        |_______________________________|

    '''

    menu=[['1. Activos'],['2. Personal'],['3. Zonas'],['4. Asignacion'],['5. Reportes'],['6. Movimiento de activos'],['7. Salir'],]
    
    isOption=True
    while isOption:   
        try:
            core.clearScreen()
            print(titulo)
            print(tabulate(menu,tablefmt='fancy_grid'))
            op=v.validateInt('Ingrese una opcion')
            if op==1:
                pass
            elif op==2:
                menuPesonal(srcData)
                pass
            elif op==3:
                pass
            elif op==4:
                menuAsignacion(srcData)
            elif op==5:
                pass
            elif op==6:
                menuMovimientos(srcData)
            elif op==7:
                sys.exit("Vuelva pronto, Bye Bye")


        except ValueError:
            print('El valor ingresado no es valido ')

            core.pauseScreen()


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
        print(titulo)
        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Ingrese una opcion')
        if op==1:
            p.Agregar(srcData)
            core.pauseScreen()
        elif op==2:
            p.Editar(srcData)
            core.pauseScreen()
        elif op==3:
            p.eliminar(srcData)
            core.pauseScreen()
        elif op==4:
            p.buscar(srcData)
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
        print(titulo)
        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Ingrese una opcion --> ')
        if op==1:
            A.CrearAsignacion(srcData)
            core.pauseScreen()
        elif op==2:
            A.buscarAsignaciones(srcData)
            core.pauseScreen()
        elif op==3:
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
        print(titulo)
        print(tabulate(menu,tablefmt='fancy_grid'))
        op=v.validateInt('Ingrese una opcion')
        if op==1:
            m.retornos(srcData)
            core.pauseScreen()
        elif op==2:
            m.darBaja(srcData)
            core.pauseScreen()
        elif op==3:
            m.cambiarAsignacion(srcData)
            core.pauseScreen()
        elif op==4:
            m.enviarGarantia(srcData)
            core.pauseScreen()
        elif op==5:
            isOption=False
            menuPrincipal(srcData)