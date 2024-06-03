#CALCULADORA DE PROPINAS 💥
#Si la cuenta fue de $1500, repartida entre 5 personas, con 12% de propina
#Cada persona deberá pagar (150.00 / 5) * 1.12
#Formatear el resultado con 2 decimales = 33.60
#Por lo tanto, la parte de la factura total que corresponda a todos es $30.00 más una propina de $3,60.
#Consejo: hay 2 formas de redondear un número. Quizás tengas que buscar en Google para resolver esto.💪
#Ejemplo Input
#¡Bienvenido a la calculadora de propinas!
#¿Cuál fue la factura total? $124.56
#¿Cuánta propina te gustaría dar? ¿10, 12 o 15? 12
#¿Cuántas personas para dividir la cuenta? 7
#Ejemplo Salida
#Cada persona debe pagar: 19,93

print("¡Bienvenido a la calculadora de propinas!")
total = float(input("¿Cuál fue la factura total?: ")) 
propina =float(input("¿Cuánta propina te gustaría dar? ¿10, 12 o 15?: "))
division = float(input("¿Cuántas personas para dividir la cuenta?: "))

propina2 = (total*(propina/100))

print(f"el valor a pagar es:  {round(((total+propina2)/division),2)}")