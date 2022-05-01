#!/usr/bin/env python

import pygame
import sys

class MAIN:
    def __init__(self, width:int, height:int, cell_size:int):
        self.cell_size=cell_size
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size
        self.reset_game()

    def reset_game(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill((20,20,20))
        self.clock = pygame.time.Clock()
        
    def loop(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return False
        self.clock.tick(60)
        pygame.display.update()
        return True


    def end(self):
        pygame.quit()
 
def main():
    game = MAIN(30, 20, 40)

    while True:
        if not game.loop():
            break

    game.end()
    sys.exit()

if __name__ == '__main__':
    main()