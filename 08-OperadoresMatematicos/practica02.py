
#La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones. 

#x = 0.13



#print(input("tu nombre es: ")) 

#cuantohasvendido = float(input("cuanto has vendido: "))






nombre = str(input('cual es tu nombre?: '))
venta = int(input('cual es su venta total?: '))



print(f"tu nombre es {nombre} y tu comision por ventas es {round(venta*0.13,2)}") 