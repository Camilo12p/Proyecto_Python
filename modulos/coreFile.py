import json
import os
import external_data.readCsv as r1
BASE= 'data/'

def checkFile(*params):          # Checkea si existe un archivo y si no esta crea uno nuevo
    if(os.path.isfile(BASE+params[0])):
        params[1].update(readFile(params[0]))
    else:
        params[1].update(r1.readCsv(params[1]))
        createFile(params[0],params[1])
        

def createFile(*params):      #creador de json
    with open(BASE+params[0],'w') as bw:
        json.dump(params[1],bw, indent=4)


def readFile(*params):       #leedor de json
    with open(BASE+params[0],'r') as br:
        return json.load(br)
    

def updateFile(*params):    #actualiza el json
    with open(BASE+params[0],'w+') as bw:
        bw.seek(0)
        json.dump(params[1],bw,indent=4)
    

def clearScreen():     #limpia la pantalla para una mejor visualizacion en consola
    if os.sys.platform=='linux' or os.sys.platform=='darwin':          
        os.system('clear')
    else:
        os.system('cls')

def pauseScreen():   #pausa la pantalla para tener tiempo suficiente para visualizar la informacion en pantalla, para salir de la pausa se define que pulse cualquier tecla
    input('Presione cualquier tecla para continuar... ')