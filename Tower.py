import pygame

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
        self.__name = name
        self.__rate = rate
        self.__damage = damage
        self.__coordinates = coordinates
        self.__towerRange = towerRange
        self.__energy = 1 #100%
    
    def attack(self, screen, direction):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen
        \tdirection : the direction to attack\n
        Return :\n
        None
        """
        pass

    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """
        image = pygame.image.load(self.__sprite)
        tile = image.subsurface(((0, 0), (32, 32)))

        screen.blit(tile,self.__coordinates)
