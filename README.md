# Cajero automatico (login)



el proyecto esta enfocado en un ATM el cual tiene implementado un login **donde**:

* ## registra el usuario


```
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
```

### resumen del codigo
#### guardado
```
usuarios={} #para guardar los datos de las variables  **usuario** y  **contraseña**

def registrar():
    print("===== REGISTRO DE USUARIO =====")
    
    usuario = input("Ingrese un nombre de usuario: ")   
    contrasena = input("Ingrese una contraseña: ")
```
> aqui se guardan en variables los inputs que contienen la informacion
>del **nombre del usuario** y la **contraseña**
#

#### parseo de errores
```
def registrar():
    pif usuario == "":
        print("El nombre de usuario no puede estar vacío.")
        return
    if len(contrasena) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return   
    if usuario in usuarios:
        print("El usuario ya existe, intenta con otro.")
        return
```
>aqui se evitan errores como:
>* no poner nada al momento de registra un usuario
>* digitar menos de 6 caracteres en la contraseña
>* poner un usuario previamente registrado
___

* ## inicio de sesion del usuario
```
udef iniciar_sesion():
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
```
### resumen del codigo
#### estructura inicial
```
 usuario = input("Ingrese su nombre de usuario: ").strip()  
    contrasena = input("Ingrese su contraseña: ").strip() 
``` 
>se pide el **usuario** y **contraseña** registrados anterior mente
#
 #### inicio de sesion invalido
```
 if usuario not in usuarios:
        print("Usuario no encontrado.")
        return False

``` 

>esto evita que un usuario no registrado inicie sesion


```
 else:
        print("Contraseña incorrecta. Acceso denegado.")
        return False
``` 
>esto evita que el usuario pueda acceder con una contraseña invalida
#

#### inicio de sesion exitoso
```
    contrasena_guardada = usuarios[usuario]
    
    
    if contrasena == contrasena_guardada:
        print(f"Acceso concedido. ¡Bienvenido, {usuario}!")
        return True
``` 
> establece en cual espacio de del diccionario se encuentra la contraseña y la empaqueta en una variable
>
>para luego validar si esta misma es suministrada por el usuario al momento del registro

---
* ## menu
```
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
```
### resumen del codigo
#### despliege del menu

```
   def menu():
    while True:
        print("MENU PRINCIPAL")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")

```
>ponemos un while true para que siempre despliegue el **menu** seguido de prints
>
>los cuales al salir en consola le muestran al usuario a que numero corresponde
>
>cada accion

#
### validacion de acciones
```
 opcion = int(input("Seleccione una opcion: "))

```
>aqui se le pide al usuario que ingrese el numero entero correspondiente
>
>a la accion a realizar
#

#### accion de registrar
```
    if opcion == 1:
            registrar()
```
>valida que al digitar 1 en opcion se despliegue la variable registrar
#

#### accion de inicio de sesion
```
 elif opcion == 2:
            if iniciar_sesion():
                sistema_bank()
```
> valida que al digitar 2 en opcion se despliegue la variable inicio de sesion ademas de al cumplir con exito esta
>
> despliega el sistema_bank donde tenemos las operaciones del ATM

#### accion de salir

```
elif opcion == 3:
            print("sistema cerrado")
            break
```
>se valida que al digitar 3 en opcion se mande un print y luego se cierre el programa 
---

# Cajero automatico (ATM)
en este apartado se veran las utilidades comunes de un **ATM** como:

* ## menu
```
def menu2 ():
    print("1, para retirar el saldo")
    print("2, para depositar dinero")
    print("3, consultar saldo")
    print("4, salir de la cuenta")
```
>donde se le muestran al usuario a que accion corresponde cada entero
* ## saldo
```
saldo_init=0
```
>este es el saldo inicial del usuario ademas es el que se va a modificar a lo largo del proceso
* ## retirar
```
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
            print("no puedes retirar numeros negativos")
            continue
```

### manejo de errores

```

    global saldo_ini
    if saldo_ini == 0:
        print("No tienes saldo para retirar.")
        return
```
> en esta funcion se utiliso el global ya que saldo_ini era una variable fuera de todas las funciones utilisadas ademas se manifesto la condicion de que si el mismo era 0 le sea imposible retirar
```
else:
            print("no puedes depositar numeros negativos")
            continue
```
>se previnio que el usuario ingrese valores negativos a retirar

### retiro exitoso
```
  while True:
        valor_retirar=int(input("favor ingrese el valor a retirar"))
        if valor_retirar<=saldo_ini and valor_retirar>0:
            saldo_ini-=valor_retirar
            print("retirando......")
            break
```
>se pide el valor a retirar despues se verifica si este mismo es menor al saldo_ini y es una cantidad positiva. se le quita la cantidad del valor_retirar al saldo_ini


* ## deposito
```
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
```
## manejo de errores
```
 while valor_dep<0:
            print("no puedes depositar menos de 0 dolares")
            valor_dep=int(input("favor ingrese el valor a depositar"))
```
> se uso while para que salgan los prints y la variable valor_dep hasta que el usuario ponga digitos validos

## deposito con exito
```
while True:

        valor_dep=int(input("favor ingrese el valor a depositar"))
        if valor_dep>0:
            saldo_ini+=valor_dep
            print("depositando.....")
            break
```
> se pide un valor a depositar y si este cumple con la condicion de ser mayor a 0 le sume el monto ingresado en valor_dep a el saldo_ini
