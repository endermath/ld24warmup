import pygame, sys
from pygame.locals import *
from chicken import *
from ship import *

# pygame init
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("ld24 warmup!")
windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mixer.init()

# load resources
chickenLeftSurface = pygame.transform.scale2x(pygame.image.load("chicken.png"))
chickenRightSurface = pygame.transform.flip(chickenLeftSurface,True,False)

shipSurface = pygame.transform.scale2x(pygame.image.load("ship.png"))

laserSound = pygame.mixer.Sound("Laser_Squeak.wav")
deathSound = pygame.mixer.Sound("Retro_Death.wav")

# Create chickens
chickList = []
for i in range(100):
    chickList.append(Chicken())
    print chickList[-1].xPos

# Create ship
myShip = Ship()

# Clear screen with fixed color
windowSurface.fill((17,134,17))

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
    
    windowSurface.blit(shipSurface, (myShip.xPos, SCREEN_HEIGHT-64),None,BLEND_SUB)
    myShip.tick()
    windowSurface.blit(shipSurface, (myShip.xPos, SCREEN_HEIGHT-64))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                myShip.rightKeyPressed()
            elif event.key == K_LEFT:
                myShip.leftKeyPressed()
            elif event.key == K_SPACE:
                myShip.fireKeyPressed()
                laserSound.play()
        elif event.type == KEYUP:
            myShip.keyUp()
                
            
    pygame.display.update()
    fpsClock.tick(40)

