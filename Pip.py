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
    
    def move(self):
        """
        Move the pip with the direction given in the constructor
        """
        return (
            int(self.__coordinates[0] + self.__coordinates[0] * math.cos(self.__direction) / 32),
            int(self.__coordinates[1] + self.__coordinates[1] * math.sin(self.__direction) / 32)
        )

    def get_coordinates(self):
        """
        Return the coordinates of the pip
        """
        return self.__coordinates

    def set_coordinates(self, new_coordinates):
        """
        Set or Update the coordinates of the pip\n
        Parameters :\n
        x and y coordinate
        Return : \n
        None
        """
        self.__coordinates = new_coordinates

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
