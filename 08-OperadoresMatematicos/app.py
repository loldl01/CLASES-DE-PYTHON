x = 6
y = 2
z = 7

print(F"{x} + {y} es igual {x+y}")
print(F"{x} - {y} es igual {x-y}")
print(F"{x} * {y} es igual {x*y}")
print(F"{x} / {y} es igual {x/y}")

#divicion por modulo
print(F"{z} // {y} es igual {z//y}")  
print(F"{z} % {y} es igual {z%y}")  
print(F"{x} elevado a la {y} es igual {x**y}")  #para hacer un elevado. se coloca doble ** para que se vea elevado a la y
print(F"{x} elevado a la {3} es igual {x**3}") 
print(F"{x} la raiz cuadrada de {x} es igual {x**0.5}") 

#redondeo
resultado = 97/7
print(resultado)
redondeo = round(resultado, 2) #el 2 es para decirle con cuantos decimales queremos que salgan nuestros resultados
print(redondeo)

