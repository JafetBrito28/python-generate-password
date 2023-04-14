import os
import random
import string

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Arte ASCII de un gato
gato_ascii = r'''
                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
'''

# Función para imprimir el menú
def imprimir_menu():
    clear_screen()
    print("Bienvenidos.")
    print("HASHMALWARE ALPHA 1.0")
    print(gato_ascii)
    print("Hack the planet")
    print("Menu:")
    print("1. Generar contraseña")
    print("2. Salir")

# Función para generar una contraseña aleatoria
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Loop principal del programa
while True:
    imprimir_menu()
    seleccion = input("Selecciona una opción: ")
    if seleccion == "1":
        clear_screen()
        print("Generador de contraseñas")
        longitud = int(input("Ingresa la longitud de la contraseña: "))
        contrasena = generar_contrasena(longitud)
        print("Contraseña generada: ", contrasena)
        input("Presiona Enter para continuar...")
    elif seleccion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
        input("Presiona Enter para continuar...")
