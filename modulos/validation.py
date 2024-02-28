import os 


def validateInt(name:str,subject:str,action:str=''):
    try:
        num=int(input('Ingrese el '+name+' del '+subject+' '+action+' --> '))
        if num>=0:
            return num
        else:
            return validateInt(name,subject,action)
    except ValueError:
        return validateInt(name,subject,action)


def validateStr(name:str,subject:str,action:str=''):
    n=input('Ingrese el '+name+' del '+subject+' '+action+' --> ')
    if n.isalpha():
        return n
    else:
        return validateStr(name,subject,action)

def validateEmail(action:str=''):
    e=input('Ingrese el email del productor' +action+' --> ')
    if e.isalnum():
        return validateEmail(action)
    else:
        return e
