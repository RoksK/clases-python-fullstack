# Hacer las siguientes lambdas:
# tomar una lista de números y darme su suma
# tomar un string y dármelo en mayúsculas y añadiendo un espacio y 
# su tamaño al final (ejemplo "abc" deberia darme "ABC 3"
# tomar un diccionario y devolverme una tupla, primero con una tupla de 
# sus claves y después una tupla de sus valores

suma = lambda numeros: sum(numeros)

string = lambda texto: f"{texto.upper()} {len(texto)}"

tupla = lambda diccionario: (tuple(diccionario.keys()), tuple(diccionario.values()))

print(suma([1, 2, 3]))
print(string("abc"))
print(tupla({"a": 1, "b": 2, "c": 3}))