# Aqui vamos a trabajar el proyeccto de Estructuras discretas, aqui unas reglas importantes
# 1. El programa debe ser escrito en Python
# 2. El programa debe ser escrito en un solo archivo
# 3. Cada vez que se modifique algo, se tiene que subir a github con un comentario explicando lo que se hizo
# 4. Igual en el grupo de whasapp se tiene que avisar cada vez que se suba algo a github (Explicando lo que hizo)
# 5. Al momento de subirlo a github, subir antes de la explicacin su inicial para saber quien hizo el ultimo cambio
#  Ejemplo: "J. Se agrego la funcion de suma" 


variable_p = input("Ingrese el valor de p: ")
variable_q = input("Ingrese el valor de q: ")
print("Lista de los operadores logicos: ")
print("1. Conjuncion")
print("2. Disyuncion")
print("3. Negación")
print("4. Condicional")
print("5. Bicondicional")
print("6. Exclusivo")
opcion = input("Ingrese el numero de la opcion que desea: ")

if opcion == "1":
    
    print("El resultado de la conjuncion para: ", variable_p, "y", variable_q, "es: p ∧ q")

elif opcion == "2":
    
    print("El resultado de la disyuncion para: ", variable_p, "o", variable_q, "es: p ∨ q")
elif opcion == "3":
    print("El resultado de la negacion para: ", variable_p, "es: ¬p y para ", variable_q, "es: ¬q")
elif opcion == "4":
    print("El resultado del condicional para: ", variable_p, "entonces", variable_q, "es: p → q")
elif opcion == "5":
    print("El resultado del bicondicional para: ", variable_p, "si y solo si", variable_q, "es: p ↔ q")
elif opcion == "6":
    print("El resultado del exclusivo para: ó ", variable_p, "ó", variable_q, "es: p ⊕ q")
else:
    print("Opcion no valida")    
