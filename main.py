import pygame
import time
import random
pygame.init()
WIDTH,HEIGHT=500,400
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("checkers")


def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break 
    pygame.quit()

if __name__=="__main__":
    main()