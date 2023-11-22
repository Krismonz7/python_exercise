matriz = [[8,  7,  0],[34, 2, -1],[5, -5, 12]]
# Completa el ejercicio aquí

#Recorremos las listas
for lista in matriz:
    
#Reorremos los elementos de la lista
    for elemento in lista:
        
        if elemento%2 == 0:
            
            
            posicion = lista.index(elemento)
            lista[posicion] = 0 
        else:
            posicion = lista.index(elemento)
            lista[posicion] = 1