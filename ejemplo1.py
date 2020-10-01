a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
#Operaciones Matematicas
suma= a+b
multi= a*b

print("La suma de "+ str(a) + " con el numero "+ str(b) +" es igual a:" +str(suma))
print("La Multiplicacion de "+ str(a) + " con el numero "+ str(b) +" es igual a:" +str(multi))

#creamos una condicion
if (a>b):
    print("El numero "+ str(a) + " Es mayor que " + str(b))

elif (a<b):
    print("El numero "+ str(b) + " Es mayor que " + str(a))
else:
    print("Los numeros son iguales")