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
        self.you = None
        self.balls = []
        self.restart()
        return

    def restart(self):
        self.you = Circle(10, WIDTH//2, HEIGHT//2, (255, 0, 0))

        self.balls = [self.you]
        for i in range(BALLCOUNT):
            self.make_ball()

    def make_ball(self):
        radius = random.randint(2, 4)
        x = random.randint(0, WIDTH - radius)
        y = random.randint(0, HEIGHT - radius)
        color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        c = Circle(radius, x, y, color)
        c.dx = random.randint(1, 3) * random.choice([-1, 1])
        c.dy = random.randint(1, 3) * random.choice([-1, 1])
        self.balls.append(c)
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if not self.you in self.balls:
            print('You lost!')
            if pygame.K_r in newkeys:
                self.restart()
            return

        if self.you in self.balls and len(self.balls) == 1:
            print('You won!')
            if pygame.K_r in newkeys:
                self.restart()
            return




        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_UP in keys:
            self.you.dy -= 2

        if pygame.K_DOWN in keys:
            self.you.dy += 2

        if pygame.K_LEFT in keys:
            self.you.dx -= 2

        if pygame.K_RIGHT in keys:
            self.you.dx += 2

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")

        for ball in self.balls:
            ball.move()
            for other in self.balls:
                if ball != other:
                    if ball.hits(other):
                        if random.randint(0, 1) == 1:
                            self.make_ball()

                        if ball > other:
                            ball += other
                            i = self.balls.index(other)
                            self.balls.pop(i)

                        else:
                            other += ball
                            i = self.balls.index(ball)
                            self.balls.pop(i)
                            break
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

