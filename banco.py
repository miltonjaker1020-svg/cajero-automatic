usuarios = {}  

def registrar():
    print("===== REGISTRO DE USUARIO =====")
    
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    
    if usuario == "":
        print("El nombre de usuario no puede estar vacío.")
        return
    if len(contrasena) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return   
    if usuario in usuarios:
        print("El usuario ya existe, intenta con otro.")
        return
    usuarios[usuario] = contrasena
    print(f"Usuario '{usuario}' registrado exitosamente.")

def iniciar_sesion():
    print("===== INICIO DE SESIÓN =====")
    
    usuario = input("Ingrese su nombre de usuario: ").strip()
    contrasena = input("Ingrese su contraseña: ").strip()
    
    if usuario not in usuarios:
        print("Usuario no encontrado.")
        return
    
    contrasena_guardada = usuarios[usuario]
    
    if contrasena == contrasena_guardada:
        print(f"Acceso concedido. ¡Bienvenido, {usuario}!")
    else:
        print("Contraseña incorrecta. Acceso denegado.")


def menu():
    while True:
        print("MENU PRINCIPAL")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            registrar()
        elif opcion == 2:
            iniciar_sesion()
        elif opcion == 3:
            print("sistema cerrado")
            break
        else:
            print("La opcion es invalida")
            

menu()


            


