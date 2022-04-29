from busquedas import aestrella
from busquedas import ProblemaBusqueda
from busquedas import*

OBJETIVO = """1-2-3-4
5-6-7-8
9-0-A-B"""

INICIAL = """1-2-0-8
5-6-7-A
9-3-B-4"""


def list_to_string(list_):
    return "\n".join(["-".join(row) for row in list_])


def string_to_list(string_):
    return [row.split("-") for row in string_.split("\n")]


def find_location(filas, element_to_find):
    """Encuentra la ubicacion de una pieza en el rompecabezas.
    DEvuelve una tupla: fila, columna"""
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for numero in "1234567890AB":
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)


class rompecabeza(ProblemaBusqueda):
    def acciones(self, estado):
        """Devuelve una lista de piesas que se pueden mover a un espacio vacio."""
        filas = string_to_list(estado)
        fila_a, columna_a = find_location(filas, "A")

        """condiciones de acuerdo a las filas que existe 0 1 2"""
        acciones = []
        if fila_a > 0:
            acciones.append(filas[fila_a - 1][columna_a])
        if fila_a < 2:
            acciones.append(filas[fila_a + 1][columna_a])
        if columna_a > 0:
            acciones.append(filas[fila_a][columna_a - 1])
        if columna_a < 3:
            acciones.append(filas[fila_a][columna_a + 1])

        return acciones

    def resultado(self, estado, accion):
        """Devuelve el resultado despues de mover una pieza a un espacio en vacio"""
        filas = string_to_list(estado)
        fila_a, columna_a = find_location(filas, "A")
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_a][columna_a], filas[fila_n][columna_n] = (
            filas[fila_n][columna_n],
            filas[fila_a][columna_a],
        )

        return list_to_string(filas)

    def es_objetivo(self, estado):
        """Devuelve True si un estado es el estado_objetivo."""
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        """Devuelve el costo de ejecutar una accion."""
        return 1

    def heuristica(self, estado):
        """Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        """
        matriz = string_to_list(estado)
        distancia = 0

        for numero in "1234567890AB":
            # indice actual
            fila_n, columna_n = find_location(matriz, numero)
            # indice objetivo
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += (fila_n - fila_n_objetivo) ** 2 + (columna_n - col_n_goal) ** 2
        return distancia


resultado = aestrella(rompecabeza(INICIAL))

for accion, estado in resultado.camino():
    print("Mover numero", accion)
    print(estado)
