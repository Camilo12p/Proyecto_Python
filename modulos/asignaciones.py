import modulos.coreFile as core
import modulos.validation as v
from datetime import datetime

def CrearAsignacion(srcData:dict):
    print('Que tipo de asiganacion desea crear?')
    print ('1.Personal\n2.Zona\n')
    tipo=int(input('Ingrese un valor --> '))
    activos={}
    asignadoA=0

    if tipo==1:
        
        asignadoA=asignarASujeto(srcData)
        añadirActivos(srcData,activos)
        asignacion={
        'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
        'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
        'tipoAsignacion':'personal',
        'asignadoA':asignadoA,
        'activos':activos
        }   
        srcData.get('Asignacion').update({len(srcData.get('Asignacion'))+1:asignacion})
        core.updateFile('Inventario_Campus.json',srcData)

    elif tipo==2:
        
        asignadoA=asignarASujeto(srcData)
        añadirActivos(srcData,activos)
        asignacion={
        'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
        'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
        'tipoAsignacion':'zona',
        'asignadoA':asignadoA,
        'activos':activos
        }
        srcData.get('Asignacion').update({len(srcData.get('Asignacion')):asignacion})
        core.updateFile('Inventario_Campus.json',srcData)
    else:   
        print('Ingrese un valor valido')


def añadirActivos(srcData:dict,activos:dict)->dict:

    id2=input('Ingrese el id del activo a ingresar --> ')  #validar el id como se vaya a llamar en el dictionario activo
    if id2 not in srcData.get('Activos'):
        print('El id no se encuentra en el sistema')
        añadirActivos(srcData,activos)
    else:
        if srcData.get('Activos')[id2]['estado']==0:
            activos.update({len(activos)+1:id2})
            srcData.get('Activos')[id2]['estado']=1
            op=input('desea añadir mas activos\n.S(si)\nENTER para NO --> ')
            core.updateFile('Inventario_Campus.json',srcData)
            if op=='':
                return
            elif op.lower()=='s' or op=='si':
                añadirActivos(srcData,activos)
            else:
                añadirActivos(srcData,activos)
    
        

def asignarASujeto(srcData:dict)->int:
    id=str(v.validateInt('id','personal',' a asignar'))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return asignarASujeto(srcData)
    else:
        return int(id)


def buscarAsignaciones(srcData:dict):
    id=v.validateInt('id','asignaciones','a buscar')
    if id in srcData.get('Asignacion'):
        for key,value in srcData.get('Asignacion')[id]:
            print(f'{key} : {value}')
    else:
        print('EL id no se enuentra')
        