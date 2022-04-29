class Efecto:
    def __init__(self, environnement):
        self.environnement = environnement

    # mover hacia abajo
    def move_forward(self):
        self.environnement.move_forward()

    # ascender
    def move_backward(self):
        self.environnement.move_backward()

    # mover a la derecha
    def move_right(self):
        self.environnement.move_right()

    # moverse a la izquierda
    def move_left(self):
        self.environnement.move_left()

    # Buscar objetos
    def pick(self):
        self.environnement.pick()

    # agente robot
    def vacuum(self):
        self.environnement.vacuum()

    def setCost(self, cost):
        self.environnement.setCost(cost)

    def setPenitence(self, penitence):
        self.environnement.setCost(penitence)

