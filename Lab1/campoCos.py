import pygame

from agente import Agent
from lugar import Environnement


class Campo:

    def __init__(self):
        pygame.init()
        self.ave1 = pygame.image.load("imagen\\ave1.png")
        self.ave2 = pygame.image.load("imagen\\ave2.png")
        self.backgroundImage = pygame.image.load("imagen\\grille.jpg")
        self.robotImage = pygame.image.load("imagen\\robot.jpg")
        self.screen = pygame.display.set_mode((600, 600))
        self.lugar = Environnement()
        self.agent = Agent(self.lugar)

    # ejecucion del lugar y del agente
    def run(self):
        self.lugar.start()
        self.agent.start()

    # campos activos
    def show(self):
        self.screen.blit(self.backgroundImage, (0, 0))
        self.screen.blit(self.robotImage, (20 + (self.lugar.posRobotX * 120), 70 + (self.lugar.posRobotY * 120)))
        for i in range(len(self.lugar.grid)):
            if self.lugar.grid[i]["ave1"]:
                x = i % 5  # modulo
                y = i // 5  # division del campo
                self.screen.blit(self.ave1, (20 + (x * 120), 20 + (y * 120)))
            if self.lugar.grid[i]["ave"]:
                x = i % 5  # modulo
                y = i // 5  # division del campo
                self.screen.blit(self.ave2, (70 + (x * 120), 20 + (y * 120)))
        pygame.display.flip()


def main():
    running = True
    campoCos = Campo()
    campoCos.run()
    while running:
        campoCos.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


if __name__ == "__main__":
    main()
