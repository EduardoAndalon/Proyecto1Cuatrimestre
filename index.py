##Inicio programa login requerido
import random
import os

# --------VARIABLES GLOBALES----------
# Lista de contraseñas Users
usuariosAdmin = []
passwordsAdmin = []

#Credenciales locales
ADMIN = ('local.fc.000', 'root')
# -----------------------------------


#----------------------------------------------------FUNCIONES----------------------------------------------------------
# Main
def main():
    print("\t\t _____________________________________________________________________________________")
    print("\t\t|                                                                                     |")
    print("\t\t|   B  I  E  N  V  E  N  I  D  O  S   A  L   C  L  U  B    D  E  P  O  R  T  I  V  O  |")
    print("\t\t|_____________________________________________________________________________________|")
    input("Presiona una tecla para continuar.")
    #login staff requerido por seguridad.
    login()

#TODO
# Menu pincipal de interacción
def menuOpciones():
    os.system('cls')
    print("\n---Menú---")
    print("1 - Registrar equipo.")
    print("2 - Generar encuentro.")
    print("3 - Iniciar partido.")
    print("4 - Finalizar partido.")
    opcion = input("\nIngrese una opción->")
    return opcion

# Funcion para generar un user de staff y dar de alta el usuario
def altaNuevoAdmin():
    os.system('cls')
    print("---GENERAR USUARIO STAFF---")
    nombreAlta = str(input("Primer nombre: "))
    apellidoAlta = str(input("Primer apellido: "))
    passwordAlta = str(input("Genera una contraseña: "))
    userID = random.randint(100, 999)
    usuarioNuevo = nombreAlta + "." + apellidoAlta + "." + str(userID)
    usuariosAdmin.append(usuarioNuevo)
    passwordsAdmin.append(passwordAlta)
    print(f"\t\t USUARIO CREADO [{usuarioNuevo}]\n\t\t'Presiona una tecla para continuar..'")
    input()
    login()

# Login principal
def login():
    os.system('cls')
    print("\n\n---LOGIN CLUB DEPORTIVO---")
    opcion = int(input("1. Inicia sesión.\n2. Registrar nuevo usuario.\nOpción-> "))
    if opcion is 1:
        usuarioLogin = str(input("Usuario: "))
        passwordLogin = str(input("Contraseña: "))
        if validarLogin(usuarioLogin,passwordLogin):
            menuOpciones()
    elif opcion is 2:
        os.system('cls')
        if credencialesAdmin():
            altaNuevoAdmin()
        else:
            login()

# Validación de datos login
def validarLogin(usuario, password):
    if usuario in usuariosAdmin:
        index = usuariosAdmin.index(usuario)
        if passwordsAdmin[index] == password:
            return True
        else:
            validarPassUsuario(usuario,password,index)
    else:
        print("El usuario no existe, favor de registrarlo.")
        login()

# Validación si es que el usuario existe pero la contraseña no coincide // Máximo 3 intentos.
def validarPassUsuario(usuario,password,index):
    intentosPassword = 1
    while passwordsAdmin[index] != password:
        if intentosPassword != 3:
            print(f"USUARIO: [{usuario}] INTENTO :[{intentosPassword}]")
            password = str(input("Favor de escribir su contraseña:"))
        else:
            print(f"USUARIO: [{usuario}] 3 INTENTOS FALLIDOS.")
            login()
        intentosPassword = intentosPassword +1


# Verificación de cuenta Local
def credencialesAdmin():
    print("---¡ ALERTA !----\nCredenciales de ADMIN requeridas.")
    userAdmin = str(input("User ADMIN: "))
    passAdmin = str(input("Password ADMIN: "))
    return userAdmin == ADMIN[0] and passAdmin == ADMIN[1]
#-----------------------------------------------------------------------------------------------------------------------


# Inicio
main()








