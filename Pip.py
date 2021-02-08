import pygame
import math

class Pip:
    """
    Class Pip :\n
    Attibuts :\n
    \tcoordinates : the coordinates of the pip (int) (default (10,10))
    \tsize : size of the pip (int) (default 1)
    \tdamage : damage of the pip (int) (default 1)
    """

    def __init__(self, coordinates = (20,20), direction = 0, size = 1, damage = 1):
        """
        Constructor of the pips\n
        Arguments :\n
        \tcoordinates : the coordinates of the pip (int) (default (10,10))
        \tsize : size of the pip (int) (default 1)
        \tdamage : damage of the pip (int) (default 1)\n
        Return :\n
        None
        """
        self.__coordinates = coordinates
        self.__direction = direction
        self.__size = size
        self.__damage = damage
    
    def __move(self):
        return (
            self.__coordinates[0] + self.__coordinates[0] * math.cos(self.__direction),
            self.__coordinates[1] + self.__coordinates[1] * math.sin(self.__direction)
            )
    
    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """
        image = pygame.image.load('assets/tilesets/bullet.png')
        tile = image.subsurface(((0, 0), (32, 32)))

        screen.blit(tile,self.__coordinates)
        self.__coordinates = self.__move()
