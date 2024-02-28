import modulos.coreFile as core


def CrearAsignacion(srcData:dict):
    print('Que tipo de asiganacion va a crear?')
    print ('1.Personal\n2.zona\n')
    tipo=int(input('ingrese un valor --> '))

    if tipo==1:
        id=str(v.validateInt('id','personal',' a asignar'))
        if id not in srcData.get('personas'):
            print('El id no se encuentra en el sistema')
            return 
        asignadoA=srcData.get('personas').get(id)['id']

        n=int(input('cuantos activos va a ingresar --> '))

        for i in range(n):
            
            id2=v.validateInt('id','activo','a ingresar')   #validar el id como se vaya a llamar en el dictionario activo
            if id not in srcData.get('activos'):
                print('El id no se encuentra en el sistema')
                
    elif tipo==2:
        id=str(v.validateInt('numero','zona',' a asignar'))

        if id not in srcData.get('zonas'):
            print('El id no se encuentra en el sistema')
            return 
        asignadoA=srcData.get('zonas').get(id)['nrozona']     # verificar si la llave de nrozona esta bien
    else:
        print('ingrese un valor valido')