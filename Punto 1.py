#Punto 1

print("Bienvenido al organizador de eventos")
print("Por favor elija una opción")
print("*************")
print("1. Registrar una banda")
print("2. Mostrar el estado de la banda")
print("3. Cambiar la hora de presentación")
print("4. Retirar una agrupación no presente")
print("5. Salir del programa")
bandas = []
opcion = 0
while opcion != 5:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        idBanda = int(input("Ingrese el ID de la banda: "))
        nombreBanda = input("Ingrese el nombre de la banda: ")
        generoBanda = input("Ingrese el género de la banda: ")
        horaPresentacion = input("Ingrese la hora de presentación: ")
        sueldoTotal = int(input("Ingrese el pago total: "))
        estadoBanda = int(input("¿Se presentó? (0 para no y 1 para sí): "))
        
        # Verificar que la respuesta sea 0 o 1
        if estadoBanda not in (0, 1):
            print("Respuesta inválida, ingrese 0 o 1 para el estado de la banda.")
        else:
            banda = {
                "ID": idBanda,
                "nombrebanda": nombreBanda,
                "genero": generoBanda,
                "hora": horaPresentacion,
                "sueldo": sueldoTotal,
                "estado": estadoBanda
            }
            bandas.append(banda)
            print("Banda registrada con éxito!")

    elif opcion == 2:
        print("Bandas que no se presentaron:")
        for banda in bandas:
            if banda["estado"] == 0:
                print(f"ID: {banda['ID']}, Nombre: {banda['nombrebanda']}")

    elif opcion == 3:
        print("Cambiar la hora")
        print("*************")
        idbanda = int(input("Ingrese la ID de la banda: "))
        nuevahora = input("Ingrese la nueva hora de la banda: ")
        banda_encontrada = False
        for banda in bandas:
            if banda["ID"] == idbanda:
                banda["hora"] = nuevahora
                print("Hora de la presentación actualizada")
                banda_encontrada = True
                break
        if not banda_encontrada:
            print("La banda no se encuentra registrada, intenta de nuevo.")

    elif opcion == 4:
        idbanda = int(input("Ingrese el ID de la banda que desea retirar si no se presentó: "))
        banda_encontrada = False
        for banda in bandas:
            if banda["ID"] == idbanda and banda["estado"] == 0:
                bandas.remove(banda)
                print("Banda retirada con éxito")
                banda_encontrada = True
                break
        if not banda_encontrada:
            print("La banda no se encuentra registrada o ya se presentó, intenta de nuevo.")
    
    elif opcion == 5:
        print("Hasta luego")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese una respuesta válida.")