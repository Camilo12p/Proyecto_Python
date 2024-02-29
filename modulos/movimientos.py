import modulos.coreFile as core
from modulos.asignaciones import CrearAsignacion,asignarASujeto,updateHistorial
import modulos.validation as v
from datetime import datetime

def retornos(srcData:dict):
    id=str(input('Ingrese el activo a devolver --> '))
    r=0
    for key, value in srcData.get('Asignacion').items():
        for key2,value2 in value['activos'].items():
            if id in value2:
                value['activos'].pop(key2)
                v.validatePrestamo(srcData,srcData.get('Asignacion').get(key2).get('asignadoA'))
                srcData.get('Activos').get(id)['estado']=0
                r=1
                break
    print('El id no se encuentra en el sistemas') if r==0 else ''
    core.updateFile('Inventario_Campus.json',srcData)
    

def darBaja(srcData:dict):
    id1=v.validateInt('Ingrese su id')
    if str(id1) in srcData.get('Personas'):
        id=str(input('Ingrese el activo a dar de baja --> '))   
        for key, value in srcData.get('Asignacion').items():
            for key2,value2 in value['activos'].items():
                if id in value2:
                    value['activos'].pop(key2)
                    v.validatePrestamo(srcData,srcData.get('Asignacion').get(key2).get('asignadoA'))
                    break
        try:
            srcData.get('Activos').get(id)['estado']=2
            updateHistorial(srcData,2,id1,id)
        except TypeError:
            print('El id no se encuentra en el sistema')
        core.updateFile('Inventario_Campus.json',srcData)
    else:
        print('Usted no hace parte del personal de campus no tiene permiso de hacer cambios')


def cambiarAsignacion(srcData:dict):
    id1=v.validateInt('Ingrese su id')
    if str(id1) in srcData.get('Personas'): 
        id=str(input('Ingrese el activo a reasignar --> '))
        r=0
        for key, value in srcData.get('Asignacion').items():
            for key2,value2 in value['activos'].items():
                if id in value2:
                    
                    value['activos'].pop(key2)
                    v.validatePrestamo(srcData,srcData.get('Asignacion').get(key2).get('asignadoA'))
                    updateHistorial(srcData,4,id1,id)
                    r=1
                    break
        print('El id no se encuentra en el sistemas') if r==0 else cambiar(srcData,id)
    else:
        print('Usted no hace parte del personal de campus no tiene permiso de hacer cambios')        
    

def enviarGarantia(srcData:dict):
    id1=v.validateInt('Ingrese su id')
    if str(id1) in srcData.get('Personas'): 
        id=str(input('Ingrese el activo a enviar a garantia --> '))

        for key, value in srcData.get('Asignacion').items():
            for key2,value2 in value['activos'].items():
                if id in value2:
                    value['activos'].pop(key2)
                    v.validatePrestamo(srcData,srcData.get('Asignacion').get(key2).get('asignadoA'))
                    break
        try:
            srcData.get('Activos').get(id)['estado']=3
            updateHistorial(srcData,3,id1,id)
        except TypeError:
            print('El id no se encuentra en el sistema')
        core.updateFile('Inventario_Campus.json',srcData)
    else:
        print('Usted no hace parte del personal de campus no tiene permiso de hacer cambios') 
def cambiar(srcData:dict, id:str)->bool:
    print('Que tipo de rasignacion desea?')
    print ('1.Personal\n2.Zona\n')
    tipo=v.validateInt('Ingrese un valor --> ')
    activos={}
    asignadoA=0

    if tipo==1:
        asignadoA=asignarASujeto(srcData,'Ingrese el Id de la persona a asiganar')
        activos.update({len(activos)+1:id})
        asignacion={
        'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
        'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
        'tipoAsignacion':'personal',
        'asignadoA':asignadoA,
        'activos':activos
        }   
        srcData.get('Asignacion').update({len(srcData.get('Asignacion'))+1:asignacion})
        core.updateFile('Inventario_Campus.json',srcData)
        return 

    elif tipo==2:
        
        asignadoA=asignarASujeto(srcData,'Ingrese el Nro de zona de la zona a asiganar')
        activos.update({len(activos)+1:id})
        asignacion={
        'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
        'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
        'tipoAsignacion':'zona',
        'asignadoA':asignadoA,
        'activos':activos
        }
        srcData.get('Asignacion').update({len(srcData.get('Asignacion')):asignacion})
        core.updateFile('Inventario_Campus.json',srcData)
        return 
    else:   
        print('Ingrese un valor valido')
        return 

    