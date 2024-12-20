import math, pygame
from utility import tools


class Flower:
    def __init__(self, x, y, angle, spread, num) -> None:
        self.angle = angle * (3.14159 / 180)
        self.spread = spread
        self.num = num
        self.current = 0
        self.centerX = x
        self.centerY = y
        self.points = []
        self.circleSize = 6

    def draw_step(self, win, color, color2=None):
        if self.current >= self.num:
            return
        distFromCenter = self.spread * math.sqrt(self.current)
        theda = self.current * self.angle
        x = distFromCenter * math.cos(theda) + self.centerX
        y = distFromCenter * math.sin(theda) + self.centerY

        if color2 != None:
            R = tools.remap(self.current, 0, self.num, color[0], color2[0])
            G = tools.remap(self.current, 0, self.num, color[1], color2[1])
            B = tools.remap(self.current, 0, self.num, color[2], color2[2])
            col = (R, G, B)
        else:
            col = color

        pygame.draw.circle(win, col, (x, y), 5)
        self.current += 1

    def draw_full(self, win, color, color2=None):
        while self.current < self.num:
            distFromCenter = self.spread * math.sqrt(self.current)
            theda = self.current * self.angle
            x = distFromCenter * math.cos(theda) + self.centerX
            y = distFromCenter * math.sin(theda) + self.centerY

            if color2 != None:
                R = tools.remap(self.current, 0, self.num, color[0], color2[0])
                G = tools.remap(self.current, 0, self.num, color[1], color2[1])
                B = tools.remap(self.current, 0, self.num, color[2], color2[2])
                col = (R, G, B)
            else:
                col = color

            pygame.draw.circle(win, col, (x, y), self.circleSize)
            self.points.append((x, y))
            self.current += 1

    def hilight_nth(self, n, win, color):
        i = 0
        while i < len(self.points):
            pygame.draw.circle(win, color, self.points[i], self.circleSize)
            i += n
