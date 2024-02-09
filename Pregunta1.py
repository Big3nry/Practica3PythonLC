while True:
    try:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        x, y = map(int, fraction.split('/'))
        if x > y or y == 0:
            raise ValueError
        percentage = x / y * 100
        if percentage < 1:
            print("E")
        elif percentage > 99:
            print("F")
        else:
            print(round(percentage), "%")
        break
    except ValueError:
        print("Error: X e Y deben ser números enteros, Y debe ser distinto de cero y X debe ser menor o igual a Y.")
    except ZeroDivisionError:
        print("Error: Y no puede ser cero.")
