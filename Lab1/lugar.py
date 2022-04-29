import random
import threading


class Environnement(threading.Thread):
    def __init__(self):
        super().__init__()

        # lugar
        self.life = True

        # coordenadas del robot
        self.posRobotX = None
        self.posRobotY = None

        # rendimiento del robot
        self.cost = 0
        self.penitence = 0

        # Matriz o tabla del campo de area
        self.grid = [{"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}, {"ave1": False, "ave": False},
                     {"ave1": False, "ave": False}]

    def run(self):
        while self.gameIsRunning():
            if self.shouldThereBeANewDustyPlace():
                self.generateDust()
            if self.shouldThereBeANewLostDiamond():
                self.generateDiamond()

    # generacion de aves
    def generateDust(self):
        prob = random.randint(0, 24)
        self.grid[prob]["ave1"] = True

    # generacion de aves
    def generateDiamond(self):
        prob = random.randint(0, 24)
        self.grid[prob]["ave"] = True

    def shouldThereBeANewDustyPlace(self):
        prob = random.randint(0, 10 ** 6)
        if prob == 1:
            return True
        else:
            return False

    def shouldThereBeANewLostDiamond(self):
        prob = random.randint(0, 10 ** 6)
        if prob == 1:
            return True
        else:
            return False

    def gameIsRunning(self):
        return self.life

    def getGrid(self):
        return self.grid

    def getPenitence(self):
        return self.penitence

    def getCost(self):
        return self.cost

    def setPenitence(self, penitence):
        self.penitence = penitence

    def setCost(self, cost):
        self.cost = cost

    def getPosRobot(self):
        return self.posRobotX, self.posRobotY

    def vacuum(self):
        self.cost += 1
        self.grid[self.posRobotX + self.posRobotY * 5]["ave1"] = False
        # Si encuentro otro objeto
        if self.grid[self.posRobotX + self.posRobotY * 5]["ave"]:
            self.grid[self.posRobotX + self.posRobotY * 5]["ave"] = False
            self.penitence += 1

    def pick(self):
        self.cost += 1
        self.grid[self.posRobotX + self.posRobotY * 5]["ave"] = False

    def move_forward(self):
        self.cost += 1
        if (self.posRobotY + 1) >= 5:
            pass
        else:
            self.posRobotY += 1

    def move_backward(self):
        self.cost += 1
        if (self.posRobotY - 1) < 0:
            pass
        else:
            self.posRobotY -= 1

    def move_right(self):
        self.cost += 1
        if (self.posRobotX + 1) >= 5:
            pass
        else:
            self.posRobotX += 1

    def move_left(self):
        self.cost += 1
        if (self.posRobotX - 1) < 0:
            pass
        else:
            self.posRobotX -= 1
