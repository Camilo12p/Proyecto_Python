import modulos.coreFile as core
import modulos.validation as v


def CrearAsignacion(srcData:dict):
    print('Que tipo de asiganacion va a crear?')
    print ('1.Personal\n2.zona\n')
    tipo=int(input('ingrese un valor --> '))
    activos={}
    asignadoA=0

    if tipo==1:
        
        asignadoA=asignarASujeto(srcData)
        activos.update(añadirActivos(srcData))
        asignacion={
        'nroAsignacion':str(len(srcData.get('asignacion'))+1).zfill(4),
        'fechaAsignacion':0,
        'tipoAsignacion':'personal',
        'asignadoA':asignadoA,
        'activos':activos
        }   


    elif tipo==2:
        
        asignadoA=asignarASujeto(srcData)
        activos.update(añadirActivos(srcData))
        asignacion={
        'nroAsignacion':str(len(srcData.get('asignacion'))+1).zfill(4),
        'fechaAsignacion':0,
        'tipoAsignacion':'zona',
        'asignadoA':asignadoA,
        'activos':activos
        } 
    else:   
        print('ingrese un valor valido')


def añadirActivos(srcData:dict)->dict:
    activos={}
    isOption=True
    while isOption:
        id2=input('Ingrese el id del activo a ingresar --> ')  #validar el id como se vaya a llamar en el dictionario activo
        if id2 not in srcData.get('activos'):
            print('El id no se encuentra en el sistema')
            return añadirActivos(id)
        else:
            activos.update({len(activos)+1:id2})
            op=input('desea añadir mas activos\n.S.para si\nEnter.para no --> ')
            if op=='':
                return activos
            elif op.lower()=='s' or op=='si':
                return añadirActivos(id,srcData)
        
        
        

def asignarASujeto(srcData:dict)->int:
    id=str(v.validateInt('id','personal',' a asignar'))
    if id not in srcData.get('personas'):
            print('El id no se encuentra en el sistema')
            return asignarASujeto(srcData)
    else:
        return int(id)
