# Comprobar si un numero entero es palindromo y devolver la suma de sus digitos

numero = input("Dime un numero: ")

for valor in range(0, len(numero) // 2):
    if numero[valor] != numero[len(numero)-valor-1]:
        print("El número no es un palíndromo")
        break
else:
    print("El número es un palíndromo")

suma = 0

for digito in numero:
    suma += int(digito)

print("Suma: " , suma)