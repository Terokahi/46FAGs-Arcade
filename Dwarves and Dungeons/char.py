import random as rng

class pc:
    def __init__(self):
        self.x = rng.randint(0, 44)
        self.y = rng.randint(0, 234)
        self.char = '@'

    
    def reset(self):
        self.x = rng.randint(0, 44)
        self.y = rng.randint(0, 234)
    
    def move(self, x, y):
        
        self.x += x
        self.y += y

def move():
    movement = input()
    x = 0
    y = 0

    if movement == 'w':
        x -= 1
    elif movement == 'a':
        y -= 1
    elif movement == 'x':
        x += 1
    elif movement == 'd':
        y += 1
    elif movement == 'q':
        x -= 1
        y -= 1
    elif movement == 'e':
        x -= 1
        y += 1
    elif movement == 'y':
        x += 1
        y -= 1
    elif movement == 'c':
        x += 1
        y += 1
    return x, y
    