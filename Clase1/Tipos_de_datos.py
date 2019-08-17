# Podemos tener diferentes tipos de datos

# El primer tipo de datos es booleano
# Que toma valores entre True y False
boleano = True
print(f'El valor de mi variable boleano es {boleano}')

# Los numeros se pueden representar como int o float
entero = 10
print(f'El valor de mi variable "entero" es {entero}')

flotante = 25.6
print(f'El valor de mi variable "flotante" es {flotante}')

# Las cadenas contienen una serie de caracteres
cadena = "hola a todos"
print(f'El valor de mi variable "cadena" es {cadena}')

# Podemos hacer operaciones entre nuestras variables

# Booleanos
print(f'La negación de mi variable "boleano" es {not boleano}')
print(f'La conjunción entre True y False es {True and False}')
print(f'La disyunción entre True y False es {True or False}')

# Numeros

otro_numero = 30
otro_numero -= entero
print(f'El valor de mi "Otro numero" es {otro_numero}')

otro_numero *= entero
print(f'El valor de mi "Otro numero" es {otro_numero}')

otro_numero //= 3
print(f'El valor de mi "Otro numero" es {otro_numero}')

otro_numero %= 5
print(f'El valor de mi "Otro numero" es {otro_numero}')

print(f'La conjunción entre "Otro numero" y True '
      f'es {otro_numero and True}')

print(f'La conjunción entre "0" y True '
      f'es {0 and True}')

# Cadenas
print("Hola " + "Mundo")

print("Hola " * 5)

print(f'La longitud de "{cadena}" es {len(cadena)}')

print(f'El elemento 4 de mi cadena es {cadena[3]}')

print(f'El ultimo elemento de mi cadena es {cadena[-1]}')

print(f'Una porcion de mi cadena es {cadena[0:4]}')

print(f'hola pertenece a mi cadena? {"hola" in cadena}')




