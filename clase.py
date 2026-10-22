# Vamos a hacer el sistema de una sala de seguridad o cámara acorazada. Tenemos 
# que hacer un sistema de pasos independientes en los que se tienen que cumplir 
# los siguientes:
# 1. Se tiene que presentar una tarjeta valida
# 2. Se tiene que introducir un PIN correctamente (para abrir la cámara o sala)
# 3. Se tiene que presentar una huella dactilar correcta
# Los tres pasos anteriores deben realizarse en ese orden, y se deben de 
# especificar por print, por separado. Si se produce un fallo, todo se reinicia 
# y se debe empezar desde cero. Si se producen tres fallos consecutivos, 
# el sistema se bloquea para siempre.

# Definimos una serie de usuarios ya almacenados para poder verificar los valores
usuarios = {
    "1111": {"pin": "1234", "huella": "huella1"},
    "2222": {"pin": "4231", "huella": "huella2"},
    "3333": {"pin": "3322", "huella": "huella3"}
}

def validar_tarjeta(sesion: dict[str, str]) -> bool:
    """Verifica si la tarjeta introducida es un valor almacenado en el sistema o no
    
    Args:
        sesion: información almacenada de los datos solicitados para el acceso

    Returns: 
        True si la tarjeta existe, False en caso contrario
    """

    print("Introduzca el número de la tarjeta")
    tarjeta = input("Tarjeta: ")
    if tarjeta in usuarios:
        print("Tarjeta válida")
        sesion["tarjeta"] = tarjeta
        return True

    print("La tarjeta introducida no es válida")
    return False
    
def validar_pin(sesion: dict[str, str]) -> bool:
    """Comprueba si el PIN introducido es el almacenado para la tarjeta introducida
    
    Args:
        sesion: información almacenada de los datos solicitados para el acceso

    Returns: 
        True si el PIN es correcto, False en caso contrario
    """

    print("Introduzca el PIN")
    return input("PIN: ") == usuarios[sesion["tarjeta"]]["pin"]

def validar_huella(sesion: dict[str, str]) -> bool:
    """Comprueba si la huella dactilar introducida es la almacenada para la tarjeta introducida
    
    Args:
        sesion: información almacenada de los datos solicitados para el acceso

    Returns: 
        True si la huella dactilar es correcta, False en caso contrario
    """

    print("Valide su huella dactilar")
    return input("Huella: ") == usuarios[sesion["tarjeta"]]["huella"]

def sistema_seguridad(validaciones, max_fallos: int = 3) -> bool:
    """Ejecuta las validaciones en orden y bloquea tras el número máximo de intentos permitidos.

    Cada intento empieza con una sesión vacía. Si una validación falla, se suma un fallo y el proceso 
    se reinicia desde el primero paso.
    
    Args:
        validaciones: funciones que reciben la sesión y devuelven la validación o no de cada uno de los pasos.
        max_fallos: número de fallos permitidos antes del bloqueo.

    Returns: 
        True si se concedió el acceso, False si el sistema se bloqueó.
    """

    fallos = 0

    while fallos < max_fallos:
        sesion = {} # Reiniciamos los valores almacenados cada vez que se produce un error
        for validacion in validaciones:
            if not validacion(sesion):
                fallos += 1
                print(f"Error en la validación. Número de fallos acumulados: {fallos}")
                break
        else: 
            print("Acceso concedido")
            return True
        
    print("Acceso denegado. Número de fallos máximos permitidos superados")
    return False

sistema_seguridad([validar_tarjeta, validar_pin, validar_huella])