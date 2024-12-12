import pygame
import math
from objects.paddle import Paddle
from objects.blocks import Blocks



class Ball(pygame.Rect):
    """
    A class to represent a ball that moves on the screen, inheriting from pygame.Rect.
    The ball is defined by its position, velocity, speed, radius, and color.

    Attributes:
    radius (int): The radius of the ball.
    speed (int): The speed at which the ball moves.
    color (str): The color of the ball (in a format pygame understands).
    diameter (int): The diameter of the ball (calculated from the radius).
    x (int): The x-coordinate of the ball's center.
    y (int): The y-coordinate of the ball's center.
    dx (float): The x-component of the direction vector (movement direction).
    dy (float): The y-component of the direction vector (movement direction).
    """

    def __init__(self, x, y, radius=15, dx=0, dy=1, speed=5, color='white', colliding_paddle = False, colliding_block = False):
        """
        Initialize a new ball object with position, velocity, speed, and color.

        Parameters:
        x (int): The initial x-coordinate of the ball's center.
        y (int): The initial y-coordinate of the ball's center.
        radius (int, optional): The radius of the ball. Default is 15.
        dx (float, optional): The x-component of the direction vector. Default is 0.
        dy (float, optional): The y-component of the direction vector. Default is 1.
        speed (int, optional): The speed at which the ball moves. Default is 5.
        color (str, optional): The color of the ball. Default is 'white'.
        """
        
        self.radius = int(radius)
        self.speed = speed
        self.color = color
        self.diameter = int(self.radius * 2)
        self.x = int(x)
        self.y = int(y)
        self.dx = dx
        self.dy = dy
        self.colliding_paddle = colliding_paddle
        self.colliding_block = colliding_block 
        # rectangles in pygame are defined by the top-left corner and dimensions
        super().__init__(self.x - self.radius, 
                         self.y - self.radius, 
                         self.diameter, 
                         self.diameter)

    def draw(self, screen, show_box=True):
        """
        Draw the ball on the provided screen at its current position.

        Parameters:
        screen (pygame.Surface): The surface to draw the ball on.
        show_box (bool, optional): Whether to show the bounding box of the ball for debugging. Default is False.
        """
        pygame.draw.circle(screen, 
                           pygame.Color(self.color),
                           self.center, 
                           self.radius)
        
        if show_box:  # For collision debugging, show the bounding box
            pygame.draw.rect(screen, 
                             pygame.Color('white'), 
                             self,
                             1)  # last number is the box width

    def move(self):
        """
        Move the ball in the direction defined by the direction vector (dx, dy) at the specified speed.

        The direction vector (dx, dy) is normalized to ensure consistent movement speed, 
        and the ball's position is updated accordingly.
        """
        # Normalize the direction vector so that the movement per frame is given by self.speed
        num = math.sqrt(self.dx * self.dx + self.dy * self.dy)
        self.dx = self.dx / num
        self.dy = self.dy / num
        
        step_x = self.speed * self.dx
        step_y = self.speed * self.dy

        self.x += step_x
        self.y += step_y

    def __str__(self):
        """
        Returns a string representation of the ball's current state, including position and velocity.

        Returns:
        str: A string describing the ball's current position (x, y), direction (dx, dy), and speed.
        """
        return "ball: x={}, y={}, dx={}, dy={}, speed={}".format(self.x, self.y, self.dx, self.dy, self.speed)
    
    def paddle_collition(self, paddle):
         """
         Makes the ball colide with the paddle         
         """

         if self.colliding_paddle == False:
            if (self.x +2* self.radius) > paddle.x and (self.x) < (paddle.x + paddle.width): #x component
                if self.y+2*self.radius > paddle.y and self.y < paddle.y + paddle.height: #y component
                   self.dy = - self.dy
                   self.colliding_paddle = True
         if self.colliding_paddle == True:
            if not ((self.x +2* self.radius) > paddle.x and (self.x) < (paddle.x + paddle.width)): 
                if not (self.y+2*self.radius > paddle.y and self.y < paddle.y + paddle.height):
                    self.colliding_paddle = False                  
            
     

    def walls_collition(self):
        """
        Makes the ball colide with the top as well as the side walls.
        """
        DISPLAY_WIDTH = 600       
        
        if self.x+2*self.radius >= DISPLAY_WIDTH or (self.x) <= 0: #makes the ball bounce with the side walls
            self.dx = - self.dx

        if self.y <= 0: #makes the ball bounce with the top wall
            self.dy = -self.dy    
    def blocks_collition(self, block):
        """
        Mackes the ball colition with the blocks, subtract 1 to blocks health
        """
        #to be fixed (more or less 
        # works)
        if self.colliding_block == False:
            if (self.x +2* self.radius) > block.x and (self.x) < (block.x + block.width): 
                if self.y+2*self.radius > block.y and self.y < block.y + block.height:
                   self.dy = - self.dy
                   self.colliding_block = True
                   Blocks.damage(block)
                                     
            if self.y+2*self.radius > block.y and self.y < block.y + block.height: 
                if (self.x +2* self.radius) > block.x and (self.x) < (block.x + block.width):
                   self.dx = - self.dx  
                   self.colliding_block = True 
                   Blocks.damage(block)
                    
        if self.colliding_block == True: 
            if not ((self.x +2* self.radius) > block.x and (self.x) < (block.x + block.width)): 
                if not (self.y+2*self.radius > block.y and self.y < block.y + block.height):
                   
                   self.colliding_block = False
            elif not(self.y+2*self.radius > block.y and self.y < block.y + block.height): 
                if not((self.x +2* self.radius) > block.x and (self.x) < (block.x + block.width)):
                   
                   self.colliding_block = False

    
                                      
    
        
  





    


