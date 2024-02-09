while True:
    try:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_lista = calificaciones.split(',')
        calificaciones_enteros = [int(cal) for cal in calificaciones_lista]
        print("Calificaciones en entero:", calificaciones_enteros)
        break
    except ValueError:
        print("Error: Asegúrese de ingresar solo números separados por comas. Inténtelo de nuevo.")