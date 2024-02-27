import menu as m
import os
import modulos.coreFile as core

if (__name__ == '__main__'):
    Inventario_Campus={
        'activos':{},
        'personas':{},
        'zonas':{},
        'asignacio':{}
    }
    core.checkFile('Inventario_Campus.json',Inventario_Campus)

    m.menuPrincipal(Inventario_Campus)