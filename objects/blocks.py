import pygame

class Blocks(pygame.Rect):

    """
    A class to represent the blocks to be destructed

    Attributes:
    x (int): The x-coordinate of the block's top-left corner.
    y (int): The y-coordinate of the block's top-left corner.
    width (int): The width of the block.
    height (int): The height of the block.
    color (str): The color of the paddle (in a format pygame understands).
    health (int): The amount of hits nedded to be destructed.
    
    powerup (int, optional): The power up of the block, in case there is one #to be impliemented later
    """
    
    def __init__(self, x, y, width=50, height=20, color='yellow', health = 3):
        self._x = x
        self._y = y
        super().__init__(x, y, width, height)
        self.color = color  
        self.health = health
        

    def draw(self, screen):
        """
        Draw the Block on the provided screen at its current position.

        Parameters:
        screen (pygame.Surface): The surface to draw the paddle on.
        """
        pygame.draw.rect(screen, 
                         pygame.Color(self.color), 
                         self)        
   
    def __str__(self):
        """
        Return a string representation of the block's current state, including position and health.

        Returns:
        str: A string describing the block current position (x, y) and health.
        """
        return "block: x={}, y={}, health={}".format(self.x, self.y, self.health)
    
    def damage(self):
        """
        Destruction of a block
        """
        self.health -= 1
        print(f" Block hit: Remaining helf: {self.health}")
        if self.health <= 0:
            print("blocks death")
            del(self)
import pygame

class Blocks(pygame.Rect):

    """
    A class to represent the blocks to be destructed

    Attributes:
    x (int): The x-coordinate of the block's top-left corner.
    y (int): The y-coordinate of the block's top-left corner.
    width (int): The width of the block.
    height (int): The height of the block.
    color (str): The color of the paddle (in a format pygame understands).
    health (int): The amount of hits nedded to be destructed.
    
    powerup (int, optional): The power up of the block, in case there is one #to be impliemented later
    """
    
    def __init__(self, x, y, width=50, height=20, color='yellow', health = 3):
        self._x = x
        self._y = y
        super().__init__(x, y, width, height)
        self.color = color  
        self.health = health
        

    def draw(self, screen):
        """
        Draw the Block on the provided screen at its current position.

        Parameters:
        screen (pygame.Surface): The surface to draw the paddle on.
        """
        pygame.draw.rect(screen, 
                         pygame.Color(self.color), 
                         self)        
   
    def __str__(self):
        """
        Return a string representation of the block's current state, including position and health.

        Returns:
        str: A string describing the block current position (x, y) and health.
        """
        return "block: x={}, y={}, health={}".format(self.x, self.y, self.health)
    
    def damage(self):
        """
        Destruction of a block
        """
        self.health -= 1
        print(f" Block hit: Remaining helf: {self.health}")
        if self.health <= 0:
            print("blocks death")
            del(self)

