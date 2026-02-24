import ProyectoLED   # importamos el nombre del archivo 
#aqui se ejecuta todo el proyecto llamando las funciones por medio de un menu . 
#el usuario podra elejir que funcion usar , son tres funciones , l mostrar los operadores y sus simbolos 
#la segunda opcion 

# voy a defini el menu , y hare un bucle usando while true 
def menu_principal():
    while True:
        print("\n----Menu---")
        print("1.Mostrar operadores logicos ")
        print("2.evaluar logica(0,1), tablas de verdad")
        print("3.Minujuego hackeo de la proposicion")
        print("4.Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ProyectoLED.mostrar_operadores()

        elif opcion == "2":
            ProyectoLED.evaluar_logica()

        elif opcion == "3":
            ProyectoLED.ejecutar_hackeo()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")

        input("\nPresione ENTER para continuar...")


# Punto de entrada
if __name__ == "__main__":
    menu_principal()