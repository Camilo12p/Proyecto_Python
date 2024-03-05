import modulos.coreFile as core
import modulos.validation as v
from datetime import datetime

def CrearAsignacion():
    srcData={}
    srcData.update(core.readFile('Inventario_Campus.json'))
    id1=v.validateInt('Ingrese su id')
    if str(id1) in srcData.get('Personas'):
        titulo='Que tipo de asiganacion desea crear?'
        titulo2='1.Personal\n2.Zona\n'
        tipo=v.validateOpciones('Ingrese una opcion',titulo,titulo2)
        activos={}
        asignadoA=0

        if tipo==1:
            r=0
            asignadoA=asignarASujeto(srcData,'Ingrese el id de la persona a asignar')
            for key,value in srcData.get('Asignacion').items():                
                if asignadoA ==(value['asignadoA']):
                    activos.update(value['activos'])
                    añadirActivos(srcData,activos,id1)
                    value['activos'].update(activos)
                    r=1
                    break
            if r==0:
                añadirActivos(srcData,activos,id1)
                asignacion={
                'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
                'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
                'tipoAsignacion':'zona',
                'asignadoA':asignadoA,
                'activos':activos
                }
                srcData.get('Asignacion').update({len(srcData.get('Asignacion'))+1:asignacion})
                
            core.updateFile('Inventario_Campus.json',srcData)
            v.validatePrestamo(srcData,asignadoA)

        elif tipo==2:
            r=0
            print('Ingrese la zona a asignar')
            zonas=[]
            for key,value in srcData.get('Zonas').items():
                print(f'{key}.',value['NombreZona'])
                zonas.append(value['NombreZona'])

            op=v.validateOpciones('Ingrese una opcion') 
            asignadoA=zonas[op-1]
            
            
            for key,value in srcData.get('Asignacion').items():
                
                
                if asignadoA == str(value['asignadoA']):
                    activos.update(value['activos'])
                    añadirActivos(srcData,activos,id1)
                    value['activos'].update(activos)
                    r=1
                    break
            if r==0:
                añadirActivos(srcData,activos,id1)
                asignacion={
                'nroAsignacion':str(len(srcData.get('Asignacion'))+1).zfill(4),
                'fechaAsignacion':datetime.strftime(datetime.now(), '%B %d %Y'),
                'tipoAsignacion':'zona',
                'asignadoA':asignadoA,
                'activos':activos
                }
                srcData.get('Asignacion').update({len(srcData.get('Asignacion'))+1:asignacion})
            core.updateFile('Inventario_Campus.json',srcData)
        else:   
            print('Ingrese un valor valido')
    else:
        print('Usted no hace parte del personal de campus no tiene permiso de hacer cambios') 
            

def añadirActivos(srcData:dict,activos:dict, id1:int)->dict:
    
    id2=input('Ingrese el Nro de campus del activo a ingresar --> ')  #validar el id como se vaya a llamar en el dictionario activo
    if id2 not in srcData.get('Activos'):
        print('El id no se encuentra en el sistema')
        añadirActivos(srcData,activos,id1)
    else:
        if srcData.get('Activos')[id2]['estado']==0:
            activos.update({len(activos)+1:id2})
            updateHistorial(srcData,1,id1,id2)
            srcData.get('Activos')[id2]['estado']=1
            op=v.validateExit('desea añadir mas activos\n.S(si)\nENTER para NO \n ')
            core.updateFile('Inventario_Campus.json',srcData)
            
            if op=='' or type(op)==None:
                return
            elif op.lower()=='s' or op=='si':
                añadirActivos(srcData,activos,id1)
            else:
                añadirActivos(srcData,activos,id1)
        else:
            print('El activo no se puede asignar')
            añadirActivos(srcData,activos,id1)


def asignarASujeto(srcData:dict,name:str)->int:
    id=str(v.validateInt(name))
    if id not in srcData.get('Personas'):
            print('El id no se encuentra en el sistema')
            return asignarASujeto(srcData)
    else:
        return int(id)


# def buscarAsignaciones(srcData:dict):
#     id=str(v.validateInt('Ingrese el numero de la asignacion'))
#     if (id) in srcData.get('Asignacion'):
#         for key,value in srcData.get('Asignacion')[id].items():
#             print(f'{key} : {value}')
#     else:
#         print('EL id no se enuentra')

def updateHistorial(srcData:dict,tipo:int,responsable:int,idActivo:str):
    historial={
        'NroHistorial':len(srcData.get('Activos').get(idActivo)['historial'])+1,
        'fecha': datetime.strftime(datetime.now(), '%B %d %Y'),
        'tipoMov':tipo,
        'idResponsable':responsable
    }
    srcData.get('Activos').get(idActivo)['historial'].update({len(srcData.get('Activos').get(idActivo)['historial'])+1:historial})