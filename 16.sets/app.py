##los sets son otro tipo de estructuras de datos
#son inmutables
#sin datos repetidos
#existen dos formas de declara un set 
#se declara con {}, la diferencia con el diccionario es que este no tiene valor


#primera forma de declarar un set
mi_set = set([1,2,3,4])
print(type(mi_set))
print(mi_set)

#segunda forma de declarar un set

otro_Set = {1,2,3}
print(type(otro_Set))
print(otro_Set)

#ERRORES DE SETS    
print(mi_set[0])
mi_set[0] = 5
print(mi_set)

#los elementos unicos
mi_set = set((1,2,3,4,51,1,1,1,2,2,2,2))  #el set no admite duplicado por lo tanto al hacer print los elimina
print(mi_set)

#no permite otros tipos de datos 
#los sets permiten validar si existen un elemnto

mi_set = set((1,2,3,4,5))
print(2 in mi_set)

#union de los sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#aumentar un set
s1 = {1,2,3,4,5,6}
s1.add (4)
print(s1)

#eliminando set
s1.remove(3)
print(s1)

#decartar elementos
s1.discard(6)
print(s1)

#eliminar un elemento, # se elimina el primer elemento  
s1.pop()
print(s1)  
