import random 
from global_stuff import *

DIR_RIGHT=0
DIR_UP=1
DIR_LEFT=2
DIR_DOWN=3
    
class Chicken():
    def __init__(self):
        random.seed()
        self.xPos = random.randint(0,SCREEN_WIDTH-1)
        self.yPos = random.randint(0,SCREEN_HEIGHT-1)
        self.isFacingRight = random.choice([True,False])
        self.xSpeed = 0
        self.ySpeed = 0
        self.isWalking = False
        self.tickCounter = 0
        
    def tick(self):
        self.tickCounter -= 1
            
        if self.isWalking:
            self.xPos = (self.xPos+self.xSpeed)%SCREEN_WIDTH
            self.yPos = (self.yPos+self.ySpeed)%SCREEN_HEIGHT
            
        if self.tickCounter<0:
            self.tickCounter = random.randint(10,100)
            self.xSpeed = random.choice([-2,-1,1,2])
            self.ySpeed = random.choice([-2,-1,1,2])
            if self.xSpeed > 0:
                self.isFacingRight = True
            if self.xSpeed < 0:
                self.isFacingRight = False
            self.isWalking = not self.isWalking
                
    
    