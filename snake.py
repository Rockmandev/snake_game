from typing import Tuple
import pygame
import sys
import random
from p2d import P2D

CELLSIZE = 40
GRIDWIDTH = 30
GRIDHEIGHT = 20

class FRUIT:
    def __init__(self, max_grid_x, max_grid_y):
        self.pos = P2D(
            random.randint(0, max_grid_x-1),
            random.randint(0, max_grid_y-1), CELLSIZE)
        

class MAIN:
    def __init__(self, width:int, height:int, cellsize:int):
        self.screen_width = width * cellsize
        self.screen_height = height * cellsize
        self.cellsize = cellsize
        self.reset_game()

    def reset_game(self):
        pygame.init()
        screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
            )
        self.clock = pygame.time.Clock()
    
    def _pressed_key_evaluator(self, key):
        match key:
            case pygame.K_UP:
                print("Up")
            case pygame.K_DOWN:
                print("Down")
            case pygame.K_RIGHT:
                print("Right")
            case pygame.K_LEFT:
                print("Left")

    def loop(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return False
                case pygame.KEYDOWN:
                    self._pressed_key_evaluator(event.key)
                
        pygame.display.update()
        self.clock.tick(60)
        return True


    def end(self):
        pygame.quit()
 
def main():
    game = MAIN(GRIDWIDTH, GRIDHEIGHT, CELLSIZE)

    while True:
        if not game.loop():
            break

    game.end()
    sys.exit()

if __name__ == '__main__':
    main()