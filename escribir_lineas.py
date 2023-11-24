#Clase 91 :ejercicios optativos 1
#Hola mundo alineado a la derecha 10caracteres
print("{:>20}".format("Hola mundo"))
#Hola mundo truncado
print("{:.3}".format("Hola mundo"))

#Hola mundo alineado en 20 espacios con trucamiento
print("{:^40.3}".format("Hola mundo"))
#Formatea los soguientes numeros y rellenalso con la mismacantidad de ceros
n1 = 400.03
n2 = 3.098755
n3 = 14.174
#Eespacios.cantidad de decimalesf
print("{:08.2f}".format(n1))
print("{:08.2f}".format(n2))

print("{:08.2f}".format(n3))                                     