NombreProducto = input("Ingresa el nombre del producto: ")
precio = int(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad: "))

subtotal = precio * cantidad

print("Item de compra: ", NombreProducto)
print("Precio de compra: ", precio)
print("Cantidad: ", cantidad)

print("El precio de tu compra es: ", subtotal)
