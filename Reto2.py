Nombre_Cliente = input("Ingrese el nombre del cliente: ")
Valor_Comida = float(input("Ingrese el valor de la comida: "))
Valor_Bebida = float(input("Ingrese el valor de la bebida: "))

Total = Valor_Comida + Valor_Bebida * 1.10

print("==========Factura==========")
print("Nombre del cliente: ", Nombre_Cliente)
print("Valor de la comida: ", Valor_Comida)
print("Valor de la bebida: ", Valor_Bebida)
print("El total a pagar es: ", Total)

