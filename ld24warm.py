import pygame, sys, os
from pygame.locals import *
from chicken import *
from ship import *

if getattr(sys, 'frozen', None):
     basedir = sys._MEIPASS
else:
     basedir = os.path.dirname(__file__)
     
# pygame init
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("ld24 warmup!")
windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mixer.init()

# load resources
chickenLeftSurface = pygame.transform.scale2x(pygame.image.load(os.path.join(basedir,"chicken.png")))
chickenRightSurface = pygame.transform.flip(chickenLeftSurface,True,False)

shipSurface = pygame.transform.scale2x(pygame.image.load(os.path.join(basedir,"ship.png")))

laserSound = pygame.mixer.Sound(os.path.join(basedir,"Laser_Squeak.wav"))
deathSound = pygame.mixer.Sound(os.path.join(basedir,"Retro_Death.wav"))

pygame.mixer.music.load(os.path.join(basedir,"bu-woeful-matrices.it"))
pygame.mixer.music.play()


# Create chickens
chickList = []
for i in range(100):
    chickList.append(Chicken())

# Create ship
myShip = Ship()

# Clear screen with fixed color
grassColor = pygame.Color('0x118611')
windowSurface.fill(grassColor)

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

