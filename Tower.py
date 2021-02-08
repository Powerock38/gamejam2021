import pygame

class Tower:
    """
    Tower :\n
    \tAttibuts :\n
    - sprite : sprite of the Tower (pygame image)\n
    - name : name of the fruit or vegetable (not given in the constructor)  (string)\n
    - coordinates : coordinates of the tower (tupple of int)\
    - rate : fire rate of the tower (int)\n
    - damage : level of damage of the tower (int)\n
    - energy : level of energy of the tower (int)\n
    """

    def __init__(self, sprite, name, coordinates, rate, damage):
        """
        Tower : constructor of a Tower\n
        Arguments :\n
        \tsprite : sprite of the Tower (pygame image)
        \tname : name of the fruit or vegetable (not given in the constructor)  (string)
        \tcoordinates : coordinates of the tower (tupple of int)
        \trate : fire rate of the tower (int)
        \tdamage : the level of damage of the tower (int)
        """
        self.__sprite = sprite
        self.__name = name
        self.__coordinates = (0,0)
        self.__rate = rate
        self.__damage = damage
        self.__energy = 1 #100%
    
    def draw(self, screen):
        image = pygame.image.load(self.__sprite)
        tile = image.subsurface(((32, 0), (32, 32)))

        for i in range(32):
            for j in range(24):
                screen.blit(tile, (32 * i, 32 * j))
