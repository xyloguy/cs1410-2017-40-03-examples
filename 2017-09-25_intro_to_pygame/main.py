import pygame
import math
import game_mouse
import rectangle
import random

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):
        game_mouse.Game.__init__(self, "Shapes",
                                 width,
                                 height,
                                 fps)

        self.r = rectangle.Rectangle(200, 100, 0, 0, (255,255,255))
        self.r2 = rectangle.Rectangle(300, 50, 200, 300, (0,255,0))
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")


    
    def paint(self, surface):
        surface.fill((0,0,0))
        self.r.paint(surface)
        self.r2.paint(surface)


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

