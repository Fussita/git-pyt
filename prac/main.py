

from typing import Dict

datos: Dict[str, int] = {"edad": 25, "puntuación": 90, "name": 90}

def deco(func):
    def wrapper(*arg, **kwargs):
        result = func(*arg, **kwargs)
        print(f' logging: {arg} , {kwargs} result: {result} ')
        return result
    return wrapper
        
@deco
def hi(dic: Dict[str, int]):
    pass
    #print(f'hello { dic.name } ')

hi(datos)
