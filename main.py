import menu as m
import os
import modulos.coreFile as core 



if __name__ == '__main__' :
    core.clearScreen()
    print('Bienvenidos al programa de Administracion de activos de campus')
    print('Reglas\n1.Para cancelar cualquier operacion ctrl + c\n2.Los nombres de las zonas y personas no pueden contener numeros')
    print('3.Los email deben tener un @\n4. los codigos de campus del activo siempre son en mayuscula, asi usted los escriba en minuscual')
    print('5. los id, telefonos de las personas solo pueden ser numeros\n6.nro de formulario,codigo de transaccion,valor unitario de los activos solo son numeros')
    core.pauseScreen()

    Inventario_Campus={
        'Personas':{},
        'Zonas':{},
        'Asignacion':{},
        'Activos':{}
    }
    core.checkFile('Inventario_Campus.json',Inventario_Campus)
    
    m.menuPrincipal(Inventario_Campus)


