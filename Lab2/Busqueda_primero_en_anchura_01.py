from random import random
import sys
from Nodos import Nodo

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # operador 1
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo1 = Nodo(hijo)

            if not hijo1.en_lista(nodos_visitados) and not hijo1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo1)

            # operador 2
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo2 = Nodo(hijo)
            if not hijo2.en_lista(nodos_visitados) and not hijo2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo2)

            # operador 3
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo3 = Nodo(hijo)
            if not hijo3.en_lista(nodos_visitados) and not hijo3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo3)

            # operador 4
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo4 = Nodo(hijo)
            if not hijo4.en_lista(nodos_visitados) and not hijo4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo4)

            # operador 5
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo5 = Nodo(hijo)
            if not hijo5.en_lista(nodos_visitados) and not hijo5.en_lista(nodos_frontera):
                nodos_frontera.append(hijo5)
            
            # operador 6
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo6 = Nodo(hijo)
            if not hijo6.en_lista(nodos_visitados) and not hijo6.en_lista(nodos_frontera):
                nodos_frontera.append(hijo6)

            # operador 7
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo7 = Nodo(hijo)
            if not hijo7.en_lista(nodos_visitados) and not hijo7.en_lista(nodos_frontera):
                nodos_frontera.append(hijo7)

            # operador 8
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo8 = Nodo(hijo)
            if not hijo8.en_lista(nodos_visitados) and not hijo8.en_lista(nodos_frontera):
                nodos_frontera.append(hijo8)

            # operador 9
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2],estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo9 = Nodo(hijo)
            if not hijo9.en_lista(nodos_visitados) and not hijo9.en_lista(nodos_frontera):
                nodos_frontera.append(hijo9)

            nodo_actual.set_hijo([hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, hijo7, hijo8, hijo9])


if __name__ == "__main__":
    estado_inicial = [3, 1, 2, 4, 5, 7, 6, 8, 9, 0]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)