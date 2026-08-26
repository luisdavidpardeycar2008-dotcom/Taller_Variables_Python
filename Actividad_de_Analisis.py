#Actividad de análisis
#Observe el siguiente código:
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)



#Responda:
#1. ¿Qué problema presenta el código?
#El problema que tiene el codigo es que la variable edad esta como una cadena de texto string a traves de la funcion input(), y al sumar 5 a la cadena, se produce un error de tipo ya que no se puede hacer una operacion matematica entre una cadena y un numero entero.

#2. ¿Qué tipo de dato devuelve input()?
#La función input() devuelve un dato de tipo cadena de texto string

#3. ¿Cómo se puede corregir?
#Se puede corregir convirtiendo la variable edad a dato numerico osea int antes de realizar la suma, Esto se puede hacer utilizando la funcion int() para convertir en un entero

#4. Escriba el código corregido.
#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#nueva_edad = edad + 5
#print(nombre)
#print(nueva_edad)