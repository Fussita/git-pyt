
"""    
    list(dic) RETORNA UNA LISTA DE LAS CLAVES
    get() Retorna el valor especificado por la clave
    keys() Retorna una listcon las claves del diccionarioa
    values() Retorna una lista con todos los valores del diccionario
    items() Retorna unalistconteniendo un tuplepor cada clave:valor
    update() Actualiza el diccionario con la clave valor especificad
"""
# Borrar: dic.pop('nombre')
dic = {"nombre": "Juan", "edad": 25}
dic["ciudad"] = "Caracas"
for i in dic.items():
    print( f' {i[0]} : {i[1]} ' )

# LIST
    # .append(x)
    # .insert(i, x) INSERTA UN ELEMENTO I EN LA POSICION X
    # .remove(x) REMUEVE EL PRIMER ELEMENTO DE LA LIST CUYO VALOR ES X
    # .pop([i]) REMUEVE Y RETORNA EL ELEMENTO I ESPECIFICADO.
    # .count(x) CUENTA CUANTAS VECES X EXISTE
    # .reverse() INVIERTE EL ORDEN
    # len(list) NUMERO DE LEMENETOS
# range(8) : 0,1,2,3,4,5,6,7, range(30, 60, 3) : 30, 33, 36, 39 ...

# for m in list(range(8)):
    
# COMPRENSION DE LISTAS: CREAR LSITA DESDE UNA OPERACION
    # expersion for elemento in iterable

cubos = [ i ** 3 for i in range(1,8)]
cubos = [ i ** 3 for i in range(1,8) if i%2 ==0 ]


# TUPLAS: SON INMUTABLES        
tp = ( 1, 2, 3 )
def operaciones(x, y):
    return x + y, x - y, x * y, x / y

# PARA MODIFICAR - listtp = list(tp) , tp = tuple(listtp)

# SETS. coleccion sin orden que no permite repetidos. Mutable
s = { 1, 2, 3, 4 }
    # s.add(58) # s.remove(1) # s.discard(58)

# REMOVE GENERA UN ERROR SI NO EXISTE, DISCARD NO GENERA EL ERROR
# NO SE PUEDE OBTENER ACCEDER A LOS ELEMENTOS USANDO UN INDICE

"""
    a = { 1, 2, 3 }
    b = { 44, 32 }
    a.add(2)
    a.union(b)
    a.intersection(b)
    a.difference(b)
    a.symmetric_difference(b)
    a.issubset(b)
    a.issuperset(b)

    add() AGREGA UN ELEMENTO
    clear() REMUEVE TODO
    difference() RETORNA UN SET CON LA DIFERENCIA ENETRE UNO O MAS SETS
    intersection() retorna un set que es la interseccion de otros dos sets
    issubset() RETORNA TRUE SI UN SET CONTIENE A ESTE
    issuperset() RETORNA TRUE SI ESTE SET CONTIENE A OTRO
    update() ACTUALIZA EL SET CON LA UNION DE ESTE Y OTROS SETS
"""

