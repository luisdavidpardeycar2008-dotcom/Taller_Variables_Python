numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
                division = numero1 / numero2
else:

                division = ("no se puede dividir entre cero")

print("Suma: " , suma)
print("Resta: " , resta)
print("Multiplicacion: " , multiplicacion)
print("Division: " , division)