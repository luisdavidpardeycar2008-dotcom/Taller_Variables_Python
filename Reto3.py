nombre = input("Ingrese su nombre: ")
Peso = float(input("Ingrese su peso en kilogramos: "))
Altura = float(input("Ingrese su altura en metros: "))

IMC = Peso / (Altura ** 2)

print("Nombre: ", nombre)
print("Peso en kilogramos es: ", Peso)
print("Altura en metros es: ", Altura)
print("IMC: ", IMC)