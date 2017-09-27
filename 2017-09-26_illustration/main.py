import pygame
import math
import game_mouse
import rectangle
import random
import triangle
import circle

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):
        game_mouse.Game.__init__(self, "Shapes",
                                 width,
                                 height,
                                 fps)

        self.sun = circle.Circle(0, 0, 150, (255,255,0))
        self.sky = rectangle.Rectangle(600, 400, 0, 0, (20, 160, 255))
        self.houseBody = rectangle.Rectangle(400, 250, 100, 200, (247,210,45))
        self.door = rectangle.Rectangle(70, 150, 265, 300, (64, 52, 12))
        self.roof = triangle.Triangle([(300, 50), (550, 200), (50, 200)], (117,8,8))
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")


    
    def paint(self, surface):
        # order does matter. (layers)
        surface.fill((6,148,8))
        self.sky.paint(surface)
        self.sun.paint(surface)
        self.houseBody.paint(surface)
        self.door.paint(surface)
        self.roof.paint(surface)

        return

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 20
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

