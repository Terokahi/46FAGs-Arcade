import random as rng

class pc:
    def __init__(self):
        self.x = rng.randint(0, 44)
        self.y = rng.randint(0, 234)
        self.char = '@'

    def __str__ (self):
        return self.char
    
    def reset(self):
        self.x = rng.randint(0, 43)
        self.y = rng.randint(0, 234)
    
    def move(self, x, y):
        
        self.x += x
        self.y += y
