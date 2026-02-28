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
        return False
    
    contrasena_guardada = usuarios[usuario]
    
    
    if contrasena == contrasena_guardada:
        print(f"Acceso concedido. ¡Bienvenido, {usuario}!")
        return True
    else:
        print("Contraseña incorrecta. Acceso denegado.")
        return False

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
            if iniciar_sesion():
                sistema_bank()
        elif opcion == 3:
            print("sistema cerrado")
            break
        else:
            print("La opcion es invalida")
            




            


saldo_ini=0


def menu2 ():
    print("1, para retirar el saldo")
    print("2, para depositar dinero")
    print("3, consultar saldo")
    print("4, salir de la cuenta")


def retirar ():
    global saldo_ini
    if saldo_ini == 0:
        print("No tienes saldo para retirar.")
        return
    
    
    while True:
        valor_retirar=int(input("favor ingrese el valor a retirar"))
        if valor_retirar<=saldo_ini and valor_retirar>0:
            saldo_ini-=valor_retirar
            print("retirando......")
            break
        
        else:
            print("no puedes depositar numeros negativos")
            continue




def depositar():
    global saldo_ini

    while True:
        valor_dep=int(input("favor ingrese el valor a depositar"))
        if valor_dep>0:
            saldo_ini+=valor_dep
            print("depositando.....")
            break
        
        while valor_dep<0:
            print("no puedes depositar menos de 0 dolares")
            valor_dep=int(input("favor ingrese el valor a depositar"))







def sistema_bank():
    while True:
        menu2()
        opcion=int(input("favor ingrese el numero de la opcion a realizar"))
    
        if opcion not in (1,2,3,4):
            print("favor ingresar numeros validos")
            continue
    
    
    
        if opcion==1:
            retirar()
    
        if opcion==2:
            depositar()
            continue
        if opcion==3:
            print(f"tu saldo actual es {saldo_ini}")
        if opcion==4:
            print("saliendo...")
            break

menu()
