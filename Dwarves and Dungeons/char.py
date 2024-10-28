import random as rng

class pc:
    """
    A class representing the player character.
    """

    def __init__(self):
        """
        Initialize the player character.
        """
        self.x = rng.randint(0, 44)
        self.y = rng.randint(0, 234)
        self.char = '@'

        # Position of the player character in the game world.
        # The player character is currently placed at a random position
        # within the game world.

    def reset(self):
        """
        Reset the player character's position to a new random position.
        """
        self.x = rng.randint(0, 44)
        self.y = rng.randint(0, 234)

        # Reset the player character's position to a new random position.
        # This is used to move the player character to a new location.

    def move(self, x, y):
        """
        Move the player character by the specified amount.

        Parameters
        ----------
        x : int
            The amount to move the player character in the x direction.
        y : int
            The amount to move the player character in the y direction.
        """

        self.x += x
        self.y += y

        # Move the player character by the specified amount.
        # This is used to move the player character to a new location.

def move():
    """
    Get the direction of movement from the user and return the amount to move.
    """
    movement = input()
    x = 0
    y = 0

    # Get the direction of movement from the user.

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

    # Convert the direction of movement to an amount to move.

    return x, y

    # Return the amount to move.

