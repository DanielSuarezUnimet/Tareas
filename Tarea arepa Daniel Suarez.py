#Daniel Suarez 31.985.504

#Solicitud de ingredientes a utilizar

Harina = input("Ingrese la cantidad de tazas de harina: ")
Agua = input("Ingrese la cantidad de tazas de agua que desea: ")
Aceite = input("Ingrese la cantidad de cucharadas de aceite [Cantidad 1/16] Tazas: ")
Sal = input("Ingrese la cantidad de cucharaditas de sal que desea [Cantidad 1/16/3] Tazas: ")

#Cambio de Str a float/Int para hacer los calculos

Harina = int(Harina)
Agua = int(Agua)
Aceite = float(Aceite)
Sal = float(Sal)

#Conversion de cantidades ["C" hace referencia a cantidad]
#Cambio de cucharadas a tazas

C_Aceite = (Aceite/16)
C_Sal = (Sal/16/3)

#Impresion de valores

print("Cantidades finales a utilizar de: ")

print("Harina: ", Harina," Tazas")
print("Agua: ", Agua," Tazas")
print("Aceite: ", C_Aceite," Tazas")
print("Sal: ", C_Sal," Tazas")

#Sumas finales para obtener los valores de cantidad del bol y el budare

Bol = (Harina + Agua + C_Sal)
Budare = (Bol + C_Aceite)

print("El bol es de: ", Bol, " Tazas")

print ("Tu arepa equivale a una cantidad tolas de: ", Budare, " Tazas")
