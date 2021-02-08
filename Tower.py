import pygame

class Tower:
    """
    Tower :\n
    \tAttibuts :\n
    - sprite : sprite of the Tower (pygame image)\n
    - name : name of the fruit or vegetable (not given in the constructor)  (string)\n
    - rate : fire rate of the tower (int)\n
    - damage : level of damage of the tower (int)\n
    - coordinates : coordinates of the tower (tupple of int)\n
    - energy : level of energy of the tower (int)\n
    """

    def __init__(self, sprite, name, rate, damage):
        """
        Tower : constructor of a Tower\n
        Arguments :\n
        \tsprite : sprite of the Tower (path png)
        \tname : name of the fruit or vegetable (not given in the constructor)  (string)
        \tcoordinates : coordinates of the tower (tupple of int)
        \trate : fire rate of the tower (int)
        \tdamage : the level of damage of the tower (int)
        """
        self.__sprite = sprite
        self.__name = name
        self.__rate = rate
        self.__damage = damage
        self.__coordinates = (10,10)
        self.__energy = 1 #100%
    
    def attack(self, screen):
        """Pas encore implémenté ..."""
        pass

    def draw(self, screen):
        image = pygame.image.load(self.__sprite)
        tile = image.subsurface(((0, 0), (32, 32)))

        screen.blit(tile,self.__coordinates)
