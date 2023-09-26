# import pygame
# pygame.init()
# window=pygame.display.set_mode((680,480))
# pygame.draw.rect(window,(255,0,0),(100,100,50,50))
# pygame.display.update()

import pygame
import sys
pygame.init()

window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game code goes here...
