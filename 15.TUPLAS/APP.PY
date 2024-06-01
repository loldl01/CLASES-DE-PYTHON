#ALMACENAN VARIOS ELEMeNTOS
#inmutables #solo define los valores determinados Y NO SE PUEDEN EDITAR
#las duplas se las conoce por el () y dentro van los datos (1,"dos",(2.0,6))
#las duplas (), dicionarios {}, listas[]

mi_tupla = (1,2,(10,20),4)
print(type(mi_tupla))
print(mi_tupla[2][0])

#conversion y almacenaje
mi_tupla = list(mi_tupla)   #esta incompleto

#asignar diferentes variables
t = (1,2,3)
x,y,z = t
print(x,y,z)

#aplicando metodos en tuplas #lo que hacen es buscar dentro de las tuplas y solo existen dos metodos que son copunt e index
t = (1,2,3,1)
print(t.count(1)) # count busca en esa tupla los numeros repetidos

print(t.index(1)) #index busca en toda la variable la posicion de cada elemento


