# Examen Unidad 3 y 6
# Nombre: Arnold Avalos Torres
# No.Control: 18420428

def menu_principal():
    while True:
        print("/******************* Menu Principal ************************/")
        print(" 1. Validar Estudiante ")
        print(" 2. Cargar Materia ")
        print(" 3. Actualizar calificacion ")
        print(" 4. Salir ")

        opcion = int(input("Dame una opcion: "))

        # Opciones a realizar
        if opcion == 1:
            print("Validar Estudiante")
            # validar_est()
        elif opcion == 2:
            print("Cargar Materia")
            # cargar_materia()
        elif opcion == 3:
            print("Actualizar calificacion")
            # actualizar_cali()
        elif opcion == 4:
            break
        else:
            print("Opcion Incorrecta")

menu_principal()
