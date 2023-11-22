# Programa para almacenar la suma de todos los numeros del 1 al 100
rango =  list(range(1,100,1))
suma = 0
for numero in rango:

    suma += numero
    if numero%10 == 0:
        print(numero)

print("La suma total es de : ",suma)