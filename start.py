import pygame, sys
from pygame.locals import *
from chicken import *

# pygame init
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("ld24 warmup!")
windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

chickenLeftSurface = pygame.transform.scale2x(pygame.image.load("chicken.png"))
chickenRightSurface = pygame.transform.flip(chickenLeftSurface,True,False)

# chicken init
chickList = []
for i in range(100):
    chickList.append(Chicken())
    print chickList[-1].xPos

# event loop

while True:
    for c in chickList:
        if c.isFacingRight:
            windowSurface.blit(chickenRightSurface, (c.xPos, c.yPos),None,BLEND_SUB)
        else:
            windowSurface.blit(chickenLeftSurface, (c.xPos, c.yPos),None,BLEND_SUB)
        c.tick()
        if c.isFacingRight:
            windowSurface.blit(chickenRightSurface, (c.xPos, c.yPos))
        else:
            windowSurface.blit(chickenLeftSurface, (c.xPos, c.yPos))

    for event in pygame.event.get():
        if event.type == QUIT:
          sys.exit()
    pygame.display.update()
    fpsClock.tick(40)

