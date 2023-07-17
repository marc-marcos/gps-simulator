import random

class Satelite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

        self.speed = 0.1
        self.x_speed = random.randint(-5, 5)
        self.y_speed = random.randint(-5, 5)

    

    def distance(self, player):
        return ((self.x - player.x)**2 + (self.y - player.y)**2)**0.5
    
    def move(self, window_width, window_height):
        self.x += self.x_speed * self.speed / ((self.x_speed**2 + self.y_speed**2)**0.5)
        self.y += self.y_speed * self.speed / ((self.x_speed**2 + self.y_speed**2)**0.5)

        if self.x < 0 or self.x > window_width:
            self.x_speed *= -1
        
        if self.y < 0 or self.y > window_height:
            self.y_speed *= -1
    
    def change_speed(self, increment):
        if increment == 1: self.speed *= 2
        elif increment == -1: self.speed /= 2
