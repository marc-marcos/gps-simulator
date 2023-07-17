import random

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    
    def move(self, direction):
        if direction == "W":
            self.y -= self.speed
        elif direction == "S":
            self.y += self.speed 
        elif direction == "A":
            self.x -= self.speed 
        elif direction == "D":
            self.x += self.speed