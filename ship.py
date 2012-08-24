from global_stuff import *

class Ship():
    
    def __init__(self):
        self.xPos = SCREEN_WIDTH/2
        self.xSpeed = 0
        
    def tick(self):
        self.xPos = (self.xPos + self.xSpeed)%SCREEN_WIDTH
        
    def rightKeyPressed(self):
        self.xSpeed = 3
    
    def leftKeyPressed(self):
        self.xSpeed = -3
    
    def keyUp(self):
        self.xSpeed = 0
        
    def fireKeyPressed(self):
        pass