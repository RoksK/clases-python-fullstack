personas = {
    "persona_1": {
        "nombre": "Joaquin",
        "apellido": "Hernandez",
        "edad": 30,
        "trabajo": "ingeniero",
        "hobbies": {"astronomia": 40,
                          "fotografia":25,
                          "cocina": 66}
    },
    "persona_2": {
        "nombre": "Pedro",
        "apellido": "Hernandez",
        "edad": 12,
        "trabajo": "ingeniero",
        "hobbies": ["astronomia", "fotografia", "cocina"]
    },
    "persona_3": {
        "nombre": "Sara",
        "apellido": "Hernandez",
        "edad": 8,
        "trabajo": "ingeniero",
        "hobbies": ["astronomia", "fotografia", "cocina"]
    },
}

for persona in personas:
    if personas[persona]["edad"] > 18:
        print(f"{personas[persona]['nombre']} es mayor de edad")