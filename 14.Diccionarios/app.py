#diccionarios, tienen clave : valor
#utiles para guardas y ejecutar informacion a partir de su nombre y claves
#no utlizan indices
#para saber cuando es un tipo de dato diccionario se lo reconoce por usar la llave {} 
#{nombre:"jose"}
#son mutables
#no son ordenados
#no admite valores duplicados en el valor 

cliente = {'nombre':'jose','apellido':'diaz','peso':'88','talla':'1.75'} #todos tienen su clave y su valor 
print(type(cliente))  #dcit es la abreviatura para diccionario

consulta = (cliente['talla'])
print(consulta)

#otro ejemplo
dic = {'c1':'55','c2':[30,40,50],'c3':{'s1':'100','s2':'200'}} #[30,40,50] es una lista
print(dic['c3'])

#mostrar las propiedades y agregar el metodo
dic2 = {'c1':['a','b','c'],'c2':['d','f','g']}
print(dic2['c1'][0].upper())

#agregar elementos a un diccionario
dic3 = {1:'a',2:'b'}
print(dic3)

dic[3] = 'c'
print(dic3)

#modificar
dic3[2] = 'B'
print(dic3)

print(dic.keys())
print(dic3.values())
print(dic3.items())
