import modulos.coreFile as core
import modulos.validation as v
from datetime import datetime

def CrearAsignacion(srcData:dict):
    id1=v.validateInt('Ingrese su id')
    if str(id1) in srcData.get('Personas'):
        print('Que tipo de asiganacion desea crear?')
        print ('1.Personal\n2.Zona\n')
        tipo=v.validateInt('Ingrese un valor')
        activos={}
        asignadoA=0

        if tipo==1:
            
            asignadoA=asignarASujeto(srcData,'Ingrese el id de la persona a asignar')
            añadirActivos(srcData,activos,id1)
            asignacion={
            'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
            'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
            'tipoAsignacion':'personal',
            'asignadoA':asignadoA,
            'activos':activos
            }   
            srcData.get('Asignacion').update({len(srcData.get('Asignacion'))+1:asignacion})
            v.validatePrestamo(srcData,asignadoA)
            core.updateFile('Inventario_Campus.json',srcData)


        elif tipo==2:
            
            asignadoA=asignarASujeto(srcData,'Ingrese el Nro de zona de la zona a asignar')
            añadirActivos(srcData,activos,id1)
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
    else:
        print('Usted no hace parte del personal de campus no tiene permiso de hacer cambios') 
            

def añadirActivos(srcData:dict,activos:dict, id1:int)->dict:
        
    id2=input('Ingrese el Nro de campus del activo a ingresar --> ')  #validar el id como se vaya a llamar en el dictionario activo
    if id2 not in srcData.get('Activos'):
        print('El id no se encuentra en el sistema')
        añadirActivos(srcData,activos)
    else:
        if srcData.get('Activos')[id2]['estado']==0:
            activos.update({len(activos)+1:id2})
            updateHistorial(srcData,1,id1,id2)
            srcData.get('Activos')[id2]['estado']=1
            op=v.validateStr('desea añadir mas activos\n.S(si)\nENTER para NO \n ')
            core.updateFile('Inventario_Campus.json',srcData)
            if op=='':
                return
            elif op.lower()=='s' or op=='si':
                añadirActivos(srcData,activos,id1)
            else:
                añadirActivos(srcData,activos,id1)


def asignarASujeto(srcData:dict,name:str)->int:
    id=str(v.validateInt(name))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return asignarASujeto(srcData)
    else:
        return int(id)


def buscarAsignaciones(srcData:dict):
    id=str(v.validateInt('Ingrese el numero de la asignacion'))
    if (id) in srcData.get('Asignacion'):
        for key,value in srcData.get('Asignacion')[id].items():
            print(f'{key} : {value}')
    else:
        print('EL id no se enuentra')

def updateHistorial(srcData:dict,tipo:int,responsable:int,idActivo:str):
    historial={
        'NroHistorial':len(srcData.get('Activos').get(idActivo)['historial'])+1,
        'fecha': datetime.strftime(datetime.now(), '%B' '%d' '%Y'),
        'tipoMov':tipo,
        'idResponsable':responsable
    }
    srcData.get('Activos').get(idActivo)['historial'].update({len(srcData.get('Activos').get(idActivo)['historial'])+1:historial})