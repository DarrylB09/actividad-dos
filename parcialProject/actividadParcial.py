# Conversión de entero a cadena
edad = 23
edad_str = str(edad)
print("La edad en formato string es: " + edad_str)
print()

# Conversión de decimal (float) a entero
estatura = 5.82
estatura_int = int(estatura)
print("La estatura en formato entero es: " + str(estatura_int))
print()

# Conversión de cadena a entero
numero_str = "227"
numero_int = int(numero_str)
print("La cadena convertida a entero es: " + str(numero_int))
print()

# Conversión de entero a decimal
edad = 18
edad_float = float(edad)
print("Mi edad en el formato float es: " + str(edad_float))
print()

#Multilíneas de cadenas.
mensaje_multilineas = """Este es un mensaje
que abarca múltiples
líneas."""
print(mensaje_multilineas)
print()

#Función len().
mensaje = "Estudio ingenieria de sistemas"
longitud_mensaje = len(mensaje)
print("La longitud del mensaje es: " + str(longitud_mensaje))
print()

#Obtener los primeros n caracteres de una cadena.
mensaje = "Soy estudiante de sexto semestre"
n = 9  # Número de caracteres que quiero obtener
primeros_n = mensaje[:n]
print("Los primeros " + str(n) + " caracteres son: " + primeros_n)
print()

#Obtener los caracteres de en medio de una cadena.
mensaje= "Sistemas"
medio = mensaje [3:7]
print("Los caracteres del medio son:", medio)
print()

#Obtener los últimos n caracteres de una cadena.
mensaje = "Soy estudiante de sexto semestre"
n = 6  # Número de caracteres que quiero obtener
ultimos_n = mensaje[-n:]
print("Los últimos " + str(n) + " caracteres son: " + ultimos_n)
print()

#Función upper().
mensaje = "Electiva profesional I"
mensaje_mayusculas = mensaje.upper()
print("Cadena en mayúsculas: " + mensaje_mayusculas)
print()

#Función lower().
mensaje = "Electiva Profesional I"
mensaje_minusculas = mensaje.lower()
print("Cadena en minúsculas: " + mensaje_minusculas)
print()

#Multilíneas de cadenas de caracteres.
mensaje_multilinea = """Esta es una cadena de texto
que abarca varias líneas.
Cada línea se mostrará como está escrita,
respetando los saltos y el formato."""
print(mensaje_multilinea)
print()

#Función strip().
mensaje_con_espacios = "   Hola Mundo 2024   "
mensaje_sin_espacios = mensaje_con_espacios.strip()
print("Cadena original: '" + mensaje_con_espacios + "'")
print("Cadena sin espacios: '" + mensaje_sin_espacios + "'")
print()

#Función replace().
mensaje = "Maria Jose Serna"
mensaje_reemplazado = mensaje.replace("Jose", "Fernanda")
print("Cadena original: " + mensaje)
print("Cadena con reemplazo: " + mensaje_reemplazado)
print()

#Función split().
mensaje = "Darryl Dayara Bolaños Serna"
lista_palabras = mensaje.split(" ")  # Divide por los espacios
print("Lista de palabras: " + str(lista_palabras))
print()

#Formato de cadenas F-String.
nombre = "Leonardo Bolaños"
edad = 44
mensaje_formato = f"Mi nombre es {nombre} y tengo {edad} años."
print(mensaje_formato)
print()
