#Ejercisios
numero = int(input("Numero: "))
sumatorio = 0
# Completa el ejercicio aquí
counter = 0
size = range(numero)
for num in size:
    
    if num%5 == 0 or num%7 == 0:
        print("cumtiplo de 5 o 7")
    else:
        sumatorio += counter
    counter +=1
print(sumatorio)