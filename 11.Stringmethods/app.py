texto = "Este es el texto de jose"
resultado = texto.upper() #upper es para hacer que el texto se haga mayuscula
resultado = texto.split("t") #split es un metodo que coloca los elementos en una lista y los separa por comas. #("-") esa simbologia es para que separe por guion
resultado = texto.find("t") #para verificar si hay "t"
resultado = texto.replace("jose", "Python")  #que en vez de "jose" quiero que lo remplace por "python"
#print (resultado)

a = "aprender"
b = "python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d]) #la lista se declara con los corchetes y coloco las palabras que quiero que se una
#print(e)

#estos metodos solo funcionan con el string, no funciona con cosas que no sean listas

url = "https://www.ejemplo.com/path/to/page?query=valor"
url2 = url.split("/")
print(url2[2:3:])