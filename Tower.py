import pygame
from Pip import Pip
import math

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

    def __init__(self, sprite, name, rate, damage, coordinates = (10,10), towerRange = 5, max_attack = 1):
        """
        Tower : constructor of a Tower\n
        Arguments :\n
        \tsprite : sprite of the Tower (path png)
        \tname : name of the fruit or vegetable (not given in the constructor)  (string)
        \trate : fire rate of the tower (int)
        \tdamage : the level of damage of the tower (int)
        \tcoordinates : the coordinates of the tower (tupple of int) (default (10,10))
        \ttowerRange : the range of fire of the fower (int) (default 5)\n
        Return :\n
        None
        """
        self.__sprite = sprite
        self.name = name
        self.rate = rate
        self.__damage = damage
        self.coordinates = coordinates
        self.__towerRange = towerRange
        self.__energy = 1 #100%
        self.tick = 0
        self.max_attack = max_attack
    
    def attack(self, enemy):
        """
        Attack a position\n
        Parameters :\n
        \tdirection : the direction to attack in radian (int)\n
        Return :\n
        The new pip that attack
        """
        pip = None
        pos1 = self.coordinates
        pos2 = (enemy.pos[0] * 32 + enemy.pos_in_tile[0], enemy.pos[1] * 32 + enemy.pos_in_tile[1])
        distance = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
        if distance < 100:
            pip = Pip(self.coordinates, enemy)
            
        return pip

    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """
        tile = self.__sprite.subsurface(((0, 0), (32, 32)))

        screen.blit(tile,self.coordinates)
