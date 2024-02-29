import os 


def validateInt(context:str):
    try:
        num=int(input(context +' --> '))
        if num>=0:
            return num
        else:
            return validateInt(context)
    except ValueError:
        return validateInt(context)


def validateStr(context:str):
    n=input(context + ' --> ')
    if n.isalpha():
        return n
    else:
        return validateStr(context)

def validateEmail(context:str):
    e=input(context+ ' --> ')
    if e.isalnum():
        return validateEmail(context)
    else:
        return e

