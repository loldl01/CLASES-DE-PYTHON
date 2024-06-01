mi_lista = ['a','b','c']
print(type(mi_lista))

#tamaño de string
print(len(mi_lista))
 #uni listas
mi_lista1 = ['a','b','c']
mi_lista2 = ['s','d','f']
print(mi_lista1 + mi_lista2)

#slides en listas

resultado = mi_lista[0:]
print(resultado)

#sobre escribir valores en una lista
mi_lista4 = ['z','f','g']
mi_lista4[0] = "alfa"
print(mi_lista4)  #esto se llama sobreescribir los valores)

#metodo de agregar
mi_lista4.append('h') #cuando yo quiero agregar un elemento append lo agrega al final
print(mi_lista4)


#metodo para eliminar
mi_lista4.pop(0) #el metodo pop siempre va a eliminar el ultimo de la lista si no pongo nada (), pero si quiero eliminar alguna pocision puedo ponerlo entre ()
print(mi_lista4)  

mi_lista5 = ['a','x','n','e','y','o','l']
lista_ordenada = mi_lista5.sort()
print(lista_ordenada)

mi_lista6 = [1, 10, 2, 3, 15, 5, 45, 95, 6, 9]
mi_lista6.sort()
print(mi_lista6)  #sort me ordena los valores 

