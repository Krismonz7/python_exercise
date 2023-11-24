#clase 89- Salidas:
v= "Salida"
n = 10
print("Txto: ",v,"Numero: ",n)
c = "Un texto {} y u numero {}".format(v,n)

print(c)
print("Un texto {v} y u numero '{n}'")
#Centrando textos izquierda a derecha:
print("{:>52}".format("Una palabra cualquiera derecha"))


#Centrando textos derecha a izquierda:
print("{:52}".format("Una palabra cualquiera izquierda"))
#Centrando :
print("{:^52}".format("Una palabra cualquiera central"))
#Fragmentado :
print("{:.3}".format("Una palabra cualquiera fragmentada"))
#Alineamiento con fragmentacion :
#>Alineacion | .Fragmentacion
print("{:>22.3}".format("Una palabra cualquiera central"))

#Formate denumeros enteros :
print("{:1d}".format(10))
print("{:2d}".format(10))
print("{:3d}".format(10))
print("{:4d}".format(10))
#Podemos rellenar con otros elementos 
print("{:04d}".format(10))
#Podemos rellenar con otros elementos 
print("{:7.3f}".format(5.40))
print("{:7.3f}".format(118.800))