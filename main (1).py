import heapq

def a_star(posicion_inicial, posicion_objetivo):
    
    def heuristica(posicion, objetivo):
        return abs(posicion - objetivo)

    # cola de prioridad (heap)
    abierta = []
    heapq.heappush(abierta, (0, posicion_inicial))
    cerrada = set()

    while abierta:
        _, posicion_actual = heapq.heappop(abierta)

        print(f"Explorando posición: {posicion_actual}")

        if posicion_actual == posicion_objetivo:
            print(f"Posición encontrada: {posicion_actual}")
            return posicion_actual

        cerrada.add(posicion_actual)

        for movimiento in [-1, 1]:  # Movimientos: izquierda o derecha
            nueva_posicion = posicion_actual + movimiento
            if nueva_posicion not in cerrada:
                costo = heuristica(nueva_posicion, posicion_objetivo)
                heapq.heappush(abierta, (costo, nueva_posicion))

    print("No se encontró la posición.")
    return None

# Consola para ingresar de datos
posicion_inicial = int(input("Ingresa la posición inicial del bloque del motor: "))
posicion_objetivo = int(input("Ingresa la posición objetivo de montaje: "))

# Ejecutar la búsqueda heurística
a_star(posicion_inicial, posicion_objetivo)

