import pygame
import math
import random
from config import *
import game_mouse
from circle import Circle

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Bouncing Balls",
                                 WIDTH,
                                 HEIGHT,
                                 24)
        self.balls = []
        for i in range(BALLCOUNT):
            radius = random.randint(2, 10)
            x = random.randint(0, WIDTH - radius)
            y = random.randint(0, HEIGHT - radius)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            c = Circle(radius, x, y, color)
            c.dx = random.randint(1, 10) * random.choice([-1, 1])
            c.dy = random.randint(1, 10) * random.choice([-1, 1])
            self.balls.append(c)
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")

        for ball in self.balls:
            ball.move()

        return
    
    def paint(self, surface):
        surface.fill((0, 0, 0))

        for ball in self.balls:
            ball.paint(surface)

        return

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 10
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

