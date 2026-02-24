import time
import os

# --- LOGICA DE OPERADORES ---

def evaluar_operador(op, p, q):
    """
    Este es el switch que traduce los simbolos a logica de Python.
    """
    match op:
        case "^": 
            return p and q
        case "v": 
            return p or q
        case "->": 
            # La condicional (p -> q) es lo mismo que (no p o q)
            return not p or q
        case "<->": 
            # La bicondicional es True si ambos son iguales
            return p == q
        case _: 
            return False

def borrar_pantalla():
    """Limpia la consola para que el Usuario 2 no vea la respuesta."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# --- LOGICA DEL JUEGO ---

def ejecutar_hackeo():
    # El Usuario 1 define la 'llave' del sistema
    print("CONFIGURACION DE PROPOSICION - USUARIO 1")
    print("Operadores validos: ^, v, ->, <->")
    
    op1 = input("Introduce Op1: ")
    op2 = input("Introduce Op2 (central): ")
    op3 = input("Introduce Op3: ")
    
    borrar_pantalla()
    
    # El Usuario 2 intenta entrar al sistema
    print("SISTEMA BLOQUEADO - USUARIO 2")
    print("Estructura: (A op1 B) op2 (C op3 D)")
    
    # Empezamos a contar el tiempo y los movimientos desde aqui
    tiempo_inicial = time.time()
    movimientos = 0
    limite = 180 # 3 minutos
    
    while True:
        # Calculo del tiempo transcurrido en cada vuelta del bucle
        tiempo_actual = time.time()
        transcurrido = tiempo_actual - tiempo_inicial
        
        # Si te pasas de los 3 minutos, el programa se corta
        if transcurrido > limite:
            print("TIEMPO AGOTADO. El sistema se ha bloqueado.")
            break
            
        print(f"\nTiempo: {int(transcurrido)}s / {limite}s | Movimientos: {movimientos}")
        print("1. Probar combinacion de bits (0/1)")
        print("2. Intentar descifrar operadores")
        print("3. Salir")
        
        opcion = input("Seleccion: ")
        movimientos += 1
        
        match opcion:
            case "1":
                try:
                    # Probando la tabla de verdad manualmente
                    a = int(input("A: "))
                    b = int(input("B: "))
                    c = int(input("C: "))
                    d = int(input("D: "))
                    
                    # Resolvemos por partes como en algebra
                    izq = evaluar_operador(op1, a, b)
                    der = evaluar_operador(op3, c, d)
                    # El op2 conecta los dos resultados anteriores
                    resultado = evaluar_operador(op2, izq, der)
                    
                    print(f"Resultado del sistema: {int(resultado)}")
                except ValueError:
                    print("Error: Solo puedes meter 0 o 1.")

            case "2":
                # Validacion final de los tres operadores
                g1 = input("Adivina Op1: ")
                g2 = input("Adivina Op2: ")
                g3 = input("Adivina Op3: ")
                
                # Solo ganas si los tres coinciden exactamente
                if g1 == op1 and g2 == op2 and g3 == op3:
                    print("ACCESO CONCEDIDO")
                    print(f"Lo lograste en {int(transcurrido)} segundos y {movimientos} movimientos.")
                    break
                else:
                    print("ACCESO DENEGADO. Sigue intentando.")

            case "3":
                print(f"La clave era: {op1}, {op2}, {op3}")
                break
            
            case _:
                print("Opcion invalida.")

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_hackeo()