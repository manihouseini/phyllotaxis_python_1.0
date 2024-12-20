import pygame, setting
from sys import exit
import flower
from utility import tools, pygame_tools

pygame.init()


class App:
    def __init__(self, WIDTH, HEIGHT, FPS) -> None:
        self.setup_project()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CLOCK = pygame.time.Clock()
        self.FPS = FPS
        self.running = True

    def setup_project(self):
        self.FLOWER_HILIGHTING = 0
        self.FLOWER_ANGLE = int(
            tools.take_input(
                """
    please enter flower mode:
    1. normal (default)
    2. distichy
    3. anomalous phyllotaxis
    4. tristichy

    >""",
                1,
            )
        )
        match self.FLOWER_ANGLE:
            case 1:
                self.FLOWER_ANGLE = 137.508
            case 2:
                self.FLOWER_ANGLE = 180
            case 3:
                self.FLOWER_ANGLE = 99.5
            case 4:
                self.FLOWER_ANGLE = 120
        self.FLOWER_SPREAD = tools.take_input(
            "please enter a flower spread (12):      >", 12
        )
        self.FLOWER_NUMBER = tools.take_input(
            "please enter a flower size (1200):      >", 1200
        )
        self.FLOWER_SINGLE = int(
            tools.take_input("is it 1 flower. 1 for yes 0 for no (1): >", 1)
        )
        if not self.FLOWER_SINGLE:
            self.FLOWER_MOVING = int(
                tools.take_input(
                    "is the flower being created? 1 for yes 0 for no (1): >", 1
                )
            )
            self.FLOWER_HILIGHT_NUMBER = 1
        if not self.FLOWER_SINGLE and self.FLOWER_MOVING:
            self.FLOWER_ANGLE = 0
        elif not self.FLOWER_SINGLE and not self.FLOWER_MOVING:
            self.FLOWER_HILIGHTING = int(
                tools.take_input(
                    "does the flower have highlighting 1 for yes 0 for no(0): >", 0
                )
            )

    def setup(self):
        self.flower = flower.Flower(
            self.WIDTH // 2,
            self.HEIGHT // 2,
            angle=self.FLOWER_ANGLE,
            spread=self.FLOWER_SPREAD,
            num=self.FLOWER_NUMBER,
        )

    def update(self):
        if self.FLOWER_SINGLE:
            self.flower.draw_step(self.WIN, (255, 0, 255), (255, 255, 255))
        else:
            self.flower = flower.Flower(
                self.WIDTH // 2,
                self.HEIGHT // 2,
                angle=self.FLOWER_ANGLE,
                spread=self.FLOWER_SPREAD,
                num=self.FLOWER_NUMBER,
            )
            self.WIN.fill((0, 0, 0))
            self.flower.draw_full(self.WIN, (255, 0, 255))
            if self.FLOWER_MOVING:
                self.FLOWER_ANGLE += 0.001
                self.flower = flower.Flower(
                    self.WIDTH // 2,
                    self.HEIGHT // 2,
                    angle=self.FLOWER_ANGLE,
                    spread=self.FLOWER_SPREAD,
                    num=self.FLOWER_NUMBER,
                )
            elif self.FLOWER_HILIGHTING:
                self.flower.hilight_nth(
                    self.FLOWER_HILIGHT_NUMBER, self.WIN, (255, 255, 0)
                )
                pygame_tools.debug(self.FLOWER_HILIGHT_NUMBER, 10)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEWHEEL:
                self.FLOWER_HILIGHT_NUMBER += 1
            if pygame.mouse.get_pressed()[0]:
                self.FLOWER_HILIGHT_NUMBER = 1

    def run(self):
        self.setup()
        while self.running:
            self.events()

            self.update()

            self.CLOCK.tick(self.FPS)
            pygame.display.set_caption(str(self.CLOCK.get_fps()))
            pygame.display.flip()


app = App(setting.window["width"], setting.window["height"], setting.window["fps"])
app.run()
