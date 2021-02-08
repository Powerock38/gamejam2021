import pygame
from Pip import Pip

class Tower:
    """
    Tower :\n
    Attibuts :\n
    \tsprite : sprite of the Tower (pygame image)
    \tname : name of the fruit or vegetable (not given in the constructor)  (string)
    \trate : fire rate of the tower (int)
    \tdamage : level of damage of the tower (int)
    \tenergy : level of energy of the tower (int)
    \tcoordinates : the coordinates of the tower (tupple of int) (default (0,0))
    \ttowerRange : the range of fire of the fower (int) (default 5)
    """

    def __init__(self, sprite, name, rate, damage, coordinates = (10,10), towerRange = 5 ):
        """
        Tower : constructor of a Tower\n
        Arguments :\n
        \tsprite : sprite of the Tower (path png)
        \tname : name of the fruit or vegetable (not given in the constructor)  (string)
        \tcoordinates : coordinates of the tower (tupple of int)
        \trate : fire rate of the tower (int)
        \tdamage : the level of damage of the tower (int)
        \tcoordinates : the coordinates of the tower (tupple of int) (default (0,0))
        \ttowerRange : the range of fire of the fower (int) (default 5)\n
        Return :\n
        None
        """
        self.__sprite = sprite
        self.name = name
        self.rate = rate
        self.__damage = damage
        self.__coordinates = coordinates
        self.__towerRange = towerRange
        self.__energy = 1 #100%
        self.tick = 0
    
    def attack(self, direction):
        """
        Attack a position\n
        Parameters :\n
        \tdirection : the direction to attack in radian (int)\n
        Return :\n
        The new pip that attack
        """
        return Pip((self.__coordinates[0], self.__coordinates[1]), direction)

    def get_coordinates(self):
        """
        Return the coordinates of the tower
        """
        return self.__coordinates

    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """
        tile = self.__sprite.subsurface(((0, 0), (32, 32)))

        screen.blit(tile,self.get_coordinates())
