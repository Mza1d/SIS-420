import statistics
import threading
import time

from capturas import Sensor
from efectos import Efecto
from nodo import Node


class Agent(threading.Thread):
    def __init__(self, environnement):
        super().__init__()

        # coordenadas del robot (centro de la matriz)
        environnement.posRobotX = self.posRobotX = 4
        environnement.posRobotY = self.posRobotY = 4

        # iteración en el cuadro de exploración informe
        self.iteration_min = 1
        self.iteration = 2
        self.iteration_max = 3

        # Iteraciones, recorridos 
        self.liste_realCost = []

        # vida de robot
        self.life = True

        # Estado Creencia Deseo Intención
        self.etatBDI = {"estado": [], "nombreItem": 0, "penitence": 0}

        # planes de acción
        self.plan = []
        self.planInforme = []
        self.costInforme = 0
        self.planNoInforme = []
        self.costNoInforme = 0

        # Interfaz del robot
        self.Sensors = Sensor(environnement)
        self.effecteurs = Efecto(environnement)

    # puesta en funcionamiento del agente
    def run(self):
        while self.amIAlive():
            self.observeEnvironnmentWithAllMySensors()
            self.updateMyState()
            self.chooseAnAction()
            # Sobre eleccion de plan de accion al siguiente hijo
            if self.costNoInforme is not None and self.costInforme is not None:
                if self.costNoInforme > self.costInforme:
                    self.plan = self.planInforme
                    self.justDoIt()
                else:
                    while 1:
                        self.plan = self.planNoInforme
                        # aplique el recorrido y analice las actuaciones
                        for i in range(0, self.iteration):
                            self.justDoIt()
                            self.realCost()
                        moy = statistics.mean(self.liste_realCost)
                        # Detectar y explorar
                        if self.costInforme > moy:
                            if self.iteration - 1 <= self.iteration_min:
                                self.iteration = self.iteration_min
                            else:
                                self.iteration -= 1
                            break
                        # retirar los pasos
                        else:
                            if self.iteration + 1 >= self.iteration_max:
                                self.iteration = self.iteration_max
                            else:
                                self.iteration += 1



    def realCost(self):
        realcost = self.Sensors.getCost() - self.Sensors.getPenitence()
        self.liste_realCost.append(realcost)
        self.effecteurs.setCost(0)
        self.effecteurs.setPenitence(0)

    # informacion de exploracion
    def informe(self):
        self.planInforme, self.costInforme = self.greedy()

    def greedy(self):
        if self.etatBDI["nombreItem"] != 0:
            # limite de profundidad
            piece_max = 2
            # lista de objetos
            liste_obj = []
            # lista de objetos rasgos
            liste_traite = []
            # Lista de acciones retornar
            liste_action = []
            # coordenadas del robot
            x = self.posRobotX
            y = self.posRobotY

            # nodo principal
            n_princ = Node(x, y, None, 0, [], None, None, 0)
            # implementar lista de piezas con objetos
            for i in range(len(self.etatBDI["estado"])):
                if self.etatBDI["estado"][i]["ave1"] and self.etatBDI["estado"][i]["ave"]:
                    n = Node(i % 5, i // 5, None, 2, ["robot", "buscar"], None, None, 0)
                    n.changeHeuristic(x, y, n_princ)
                    liste_obj.append(n)
                elif self.etatBDI["estado"][i]["ave1"]:
                    n = Node(i % 5, i // 5, None, 1, ["robot"], None, None, 0)
                    n.changeHeuristic(x, y, n_princ)
                    liste_obj.append(n)
                elif self.etatBDI["estado"][i]["ave"]:
                    n = Node(i % 5, i // 5, None, 1, ["buscar"], None, None, 0)
                    n.changeHeuristic(x, y, n_princ)
                    liste_obj.append(n)
            # implementar la lista de objetos procesados
            liste_traite.insert(0, n_princ)

            for item in range(1, piece_max):
                liste_obj.sort(key=lambda c: c.heuristic)
                liste_traite.insert(0, liste_obj[0])
                liste_obj.pop(0)
                # Si la lista de objetos atrae retorna al plan de accion
                if not liste_obj:
                    n = liste_traite[0]
                    cout = 0
                    while n.previous is not None:
                        liste_action += n.action
                        cout += n.cost
                        n = n.previous
                    return liste_action, cout
                xtmp, ytmp = liste_traite[0].coord
                # actualizar - heuristico
                for node in liste_obj:
                    node.changeHeuristic(xtmp, ytmp, liste_traite[0])
            # devuelve el plan de acción que corresponde
            n = liste_traite[0]
            cout = 0
            while n.previous is not None:
                liste_action += n.action
                cout += n.cost
                n = n.previous
            return liste_action, cout
        else:
            return "nothing", None

    # exploración no informada
    def noInforme(self):
        self.planNoInforme, self.costNoInforme = self.dls()

    def dls(self):
        if self.etatBDI["nombreItem"] != 0:
            # límite de profundidad
            depth_max = 9
            # Lista de nodos a explorar
            liste_a_traite = []
            # Lista de nodos a explorar
            liste_traite = []
            # Lista de acciones a realiza
            liste_action = []
            # Potencialmente explorable
            liste_noeud = []

            # Creacion de nodo principal
            if self.etatBDI["estado"][self.posRobotX + self.posRobotY * 5]["ave"]:
                if self.etatBDI["estado"][self.posRobotX + self.posRobotY * 5]["ave1"]:
                    if self.etatBDI["nombreItem"] == 2:
                        n = Node(self.posRobotX, self.posRobotY, 0, 2, ["robot", "buscar"], 2)
                        liste_action += n.action
                        return liste_action, n.cost
                    else:
                        liste_a_traite.insert(0, Node(self.posRobotX, self.posRobotY, 0, 2, ["robot", "buscar"], 1))
                else:
                    if self.etatBDI["nombreItem"] == 1:
                        n = Node(self.posRobotX, self.posRobotY, 0, 1, ["buscar"], 1)
                        liste_action += n.action
                        return liste_action, n.cost
                    else:
                        liste_a_traite.insert(0, Node(self.posRobotX, self.posRobotY, 0, 1, ["buscar"], 1))
            elif self.etatBDI["estado"][self.posRobotX + self.posRobotY * 5]["ave1"]:
                if self.etatBDI["nombreItem"] == 1:
                    n = Node(self.posRobotX, self.posRobotY, 0, 1, ["robot"], 1)
                    liste_action += n.action
                    return liste_action, n.cost
                else:
                    liste_a_traite.insert(0, Node(self.posRobotX, self.posRobotY, 0, 1, ["robot"], 1))
            else:
                liste_a_traite.insert(0, Node(self.posRobotX, self.posRobotY, 0, 0, [], 0))

            # hacemos un bucle siempre que la lista de nodos para procesar no esté vacía
            while liste_a_traite:
                for i in range(0, depth_max - liste_a_traite[0].depth):
                    x, y = liste_a_traite[0].coord
                    # ampliamos la frontera
                    # caja a la derecha
                    if x + 1 < 5:
                        if self.etatBDI["estado"][x + 1 + y * 5]["ave"]:
                            if self.etatBDI["estado"][x + 1 + y * 5]["ave1"]:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 2:
                                    n = Node(x + 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 3,
                                             ["robot", "buscar", "derecha"], liste_a_traite[0].item_clean + 2,
                                             liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x + 1, y, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 3,
                                                                  ["robot", "buscar", "derecha"],
                                                                  liste_a_traite[0].item_clean + 2, liste_a_traite[0]))
                            else:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                    n = Node(x + 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                             ["buscar", "derecha"], liste_a_traite[0].item_clean + 2,
                                             liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x + 1, y, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 2, ["buscar", "derecha"],
                                                                  liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        elif self.etatBDI["estado"][x + 1 + y * 5]["ave1"]:
                            # verificación del logro del objetivo
                            if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                n = Node(x + 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                         ["robot", "derecha"], liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                liste_noeud.append(n)
                            else:
                                liste_a_traite.insert(1, Node(x + 1, y, liste_a_traite[0].depth + 1,
                                                              liste_a_traite[0].cost + 2, ["robot", "derecha"],
                                                              liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        else:
                            liste_a_traite.insert(1, Node(x + 1, y, liste_a_traite[0].depth + 1,
                                                          liste_a_traite[0].cost + 1, ["derecha"],
                                                          liste_a_traite[0].item_clean, liste_a_traite[0]))
                    # caja a la izquierda
                    if x - 1 >= 0:
                        if self.etatBDI["estado"][x - 1 + y * 5]["ave"]:
                            if self.etatBDI["estado"][x - 1 + y * 5]["ave1"]:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 2:
                                    n = Node(x - 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 3,
                                             ["robot", "buscar", "izquierda"],
                                             liste_a_traite[0].item_clean + 2, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x - 1, y, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 3,
                                                                  ["robot", "buscar", "izquierda"],
                                                                  liste_a_traite[0].item_clean + 2, liste_a_traite[0]))
                            else:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                    n = Node(x - 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                             ["buscar", "izquierda"],
                                             liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x - 1, y, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 2,
                                                                  ["buscar", "izquierda"],
                                                                  liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        elif self.etatBDI["estado"][x - 1 + y * 5]["ave1"]:
                            # verificación del logro del objetivo
                            if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                n = Node(x - 1, y, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                         ["robot", "izquierda"],
                                         liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                liste_noeud.append(n)
                            else:
                                liste_a_traite.insert(1, Node(x - 1, y, liste_a_traite[0].depth + 1,
                                                              liste_a_traite[0].cost + 2,
                                                              ["robot", "izquierda"],
                                                              liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        else:
                            liste_a_traite.insert(1, Node(x - 1, y, liste_a_traite[0].depth + 1,
                                                          liste_a_traite[0].cost + 1, ["izquierda"],
                                                          liste_a_traite[0].item_clean, liste_a_traite[0]))
                    # case en abajo
                    if y + 1 < 5:
                        if self.etatBDI["estado"][x + (y + 1) * 5]["ave"]:
                            if self.etatBDI["estado"][x + (y + 1) * 5]["ave1"]:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 2:
                                    n = Node(x, y + 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 3,
                                             ["robot", "buscar", "abajo"],
                                             liste_a_traite[0].item_clean + 2, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x, y + 1, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 3,
                                                                  ["robot", "buscar", "abajo"],
                                                                  liste_a_traite[0].item_clean + 2, liste_a_traite[0]))
                            else:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                    n = Node(x, y + 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                             ["buscar", "abajo"],
                                             liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x, y + 1, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 2,
                                                                  ["buscar", "abajo"],
                                                                  liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        elif self.etatBDI["estado"][x + (y + 1) * 5]["ave1"]:
                            # verificación del logro del objetivo
                            if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                n = Node(x, y + 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                         ["robot", "abajo"],
                                         liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                liste_noeud.append(n)
                            else:
                                liste_a_traite.insert(1, Node(x, y + 1, liste_a_traite[0].depth + 1,
                                                              liste_a_traite[0].cost + 2,
                                                              ["robot", "abajo"],
                                                              liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        else:
                            liste_a_traite.insert(1, Node(x, y + 1, liste_a_traite[0].depth + 1,
                                                          liste_a_traite[0].cost + 1, ["abajo"],
                                                          liste_a_traite[0].item_clean, liste_a_traite[0]))
                    # case en arriba
                    if y - 1 >= 0:
                        if self.etatBDI["estado"][x + (y - 1) * 5]["ave"]:
                            if self.etatBDI["estado"][x + (y - 1) * 5]["ave1"]:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 2:
                                    n = Node(x, y - 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 3,
                                             ["robot", "buscar", "arriba"],
                                             liste_a_traite[0].item_clean + 2, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x, y - 1, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 3,
                                                                  ["robot", "buscar", "arriba"],
                                                                  liste_a_traite[0].item_clean + 2, liste_a_traite[0]))
                            else:
                                # verificación del logro del objetivo
                                if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                    n = Node(x, y - 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                             ["buscar", "arriba"],
                                             liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                    liste_noeud.append(n)
                                else:
                                    liste_a_traite.insert(1, Node(x, y - 1, liste_a_traite[0].depth + 1,
                                                                  liste_a_traite[0].cost + 2,
                                                                  ["buscar", "arriba"],
                                                                  liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        elif self.etatBDI["estado"][x + (y - 1) * 5]["ave1"]:
                            # verificación del logro del objetivo
                            if self.etatBDI["nombreItem"] == liste_a_traite[0].item_clean + 1:
                                n = Node(x, y - 1, liste_a_traite[0].depth + 1, liste_a_traite[0].cost + 2,
                                         ["robot", "arriba"],
                                         liste_a_traite[0].item_clean + 1, liste_a_traite[0])
                                liste_noeud.append(n)
                            else:
                                liste_a_traite.insert(1, Node(x, y - 1, liste_a_traite[0].depth + 1,
                                                              liste_a_traite[0].cost + 2,
                                                              ["robot", "arriba"],
                                                              liste_a_traite[0].item_clean + 1, liste_a_traite[0]))
                        else:
                            liste_a_traite.insert(1, Node(x, y - 1, liste_a_traite[0].depth + 1,
                                                          liste_a_traite[0].cost + 1, ["arriba"],
                                                          liste_a_traite[0].item_clean, liste_a_traite[0]))
                    liste_traite.append(liste_a_traite[0])
                    liste_a_traite.pop(0)
                    i += 1
                # quitamos las hojas (4 max) de nuestra rama para poder volver al nodo anterior
                for j in range(0, 4):
                    if liste_a_traite and liste_a_traite[0].depth == depth_max:
                        liste_traite.append(liste_a_traite[0])
                        liste_a_traite.pop(0)
            # si tenemos nodos objetivos de éxito elegimos el de menor coste
            if liste_noeud:
                liste_noeud.sort(key=lambda c: c.cost)
                n = liste_noeud[0]
            # si solo logramos parcialmente el objetivo, clasificamos por artículo buscado y por costo
            else:
                # on tri d'abord par item max ramasse
                liste_traite.sort(key=lambda c: c.item_clean, reverse=True)
                # solo mantenemos los nodos capaces de buscar la cantidad máxima de elementos
                liste_traite = list(filter(lambda c: c.item_clean == liste_traite[0].item_clean, liste_traite))
                # on tri ces noeuds par cout
                liste_traite.sort(key=lambda c: c.cost)
                # el nodo que nos interesa es el primero
                n = liste_traite[0]
            cout = 0
            while n.previous is not None:
                cout += n.cost
                liste_action += n.action
                n = n.previous
            return liste_action, cout
        else:
            return "nothing", None

    # criterio de parada
    def amIAlive(self):
        return self.life

    # llamada al sensor
    def observeEnvironnmentWithAllMySensors(self):
        self.Sensors.observeEnvironment()

    # campo de ambiente
    def updateMyState(self):
        self.etatBDI["estado"], self.etatBDI[
            "penitence"], self.posRobotX, self.posRobotY = self.Sensors.getObservations()
        self.etatBDI["nombreItem"] = 0
        for i in range(len(self.etatBDI["estado"])):
            if self.etatBDI["estado"][i]["ave1"]:
                self.etatBDI["nombreItem"] += 1
            if self.etatBDI["estado"][i]["ave"]:
                self.etatBDI["nombreItem"] += 1

    # algo de exploracion
    def chooseAnAction(self):
        self.noInforme()
        self.informe()

    def justDoIt(self):
        # retraso entre las acciones del robot
        delai = 0.5

        self.plan = list(reversed(self.plan))
        for action in self.plan:
            if action == "derecha":
                self.effecteurs.move_right()
                time.sleep(delai)
            elif action == "izquierda":
                self.effecteurs.move_left()
                time.sleep(delai)
            elif action == "abajo":
                self.effecteurs.move_forward()
                time.sleep(delai)
            elif action == "arriba":
                self.effecteurs.move_backward()
                time.sleep(delai)
            elif action == "robot":
                self.effecteurs.vacuum()
                time.sleep(delai)
            elif action == "buscar":
                self.effecteurs.pick()
                time.sleep(delai)
