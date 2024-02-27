import json
import os
BASE= 'data/'

def checkFile(*params):          # Checkea si existe un archivo y si no esta crea uno nuevo
    if(os.path.isfile(BASE+params[0])):
        params[1].update(readFile(params[0]))
    else:
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