# Tendremos una lista de usuarios
# usuarios = ["joaquin", "ana", "maria", "pablo"]
# Queremos un sistema que nos pida un usuario. Si el usuario ya existe
# lo indica. Si no, se añade y se notifica (dando el total)

usuarios = ["joaquin", "ana", "maria", "pablo"]

usuario = input("Introduzca el nombre de usuario: ").lower()

while usuario != "stop":
    if usuario not in usuarios:
        usuarios.append(usuario)
        print("Usuario añadido correctamente")
    else:
        print("El usuario ya existe")
    usuario = input("Introduzca el nombre de usuario: ").lower()

print("Número de usuarios: ", len(usuarios))