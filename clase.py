# Cambiar todos los strings almacenados para que no tengan mayúsculas

variable = ["john", "DOE", "sTaRlEtTe", "TesT"]

# Tu solución aquí

for palabra in variable:
    variable_corregida = palabra.lower()
    print(variable_corregida)