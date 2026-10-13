# Comprobar si un numero entero es palindromo y devolver la suma de sus digitos

numero = input("Dime un numero: ")

# Primero comprobamos si el número tiene un número par o impar de dígitos

if len(numero) % 2 == 0:
    # Es par
    for valor in range(0, len(numero)):
        if numero[valor] == numero[len(numero)-1]:
            break
    else:
       print("El número no es un palíndromo")
else:
    # Es impar

