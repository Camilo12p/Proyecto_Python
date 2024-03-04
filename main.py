import menu as m
import os
import modulos.coreFile as core 
import external_data.readCsv as r

if __name__ == '__main__' :
    Inventario_Campus={
        'Personas':{},
        'Zonas':{},
        'Asignacion':{},
        'Activos':{}
        
    }
    core.checkFile('Inventario_Campus.json',Inventario_Campus)
    # r.readCsv(Inventario_Campus)
    m.menuPrincipal(Inventario_Campus)


