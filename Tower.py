import pygame
import math
from Pip import Pip
from Utils import Utils

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

    sleepingFrames = [pygame.image.load('assets/zzz.png').subsurface([i*32,0,32,32]) for i in range(3)]

    def __init__(self, tower, coordinates):
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

        self.coordinates = coordinates
        self.__energy = 100
        self.__energyMax = self.__energy
        self.tick = 0
        self.animTick = 0

        self.__sprite = pygame.image.load(tower['path'])
        self.name = tower['name']
        self.rate = tower['fire_rate']
        self.damage = tower['damage']
        self.__towerRange = tower['range']
        self.__energy_consumption = tower['energy_consumption']
        self.max_attack = tower['max_attack']
        self.sleeping_time = tower['sleeping_time']
        self.price = tower['price']

    def draw(self, screen):
        """
        Draw the tower\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """            

        # sprite
        screen.blit(self.__sprite, self.coordinates)

        # sleeping
        x,y = self.coordinates
        if self.__energy <= 0:
            if self.animTick >= 120:
                self.animTick = 0
                
            screen.blit(Tower.sleepingFrames[self.animTick // 40], (x, y - 10))
            self.animTick += 1

        else: # energy bars
            for n in range(1, max(2, int((self.__energy/self.__energyMax) * 7))):
                w = 4
                pygame.draw.rect(screen, Utils.BLUE, (x + (n - 1)*(w + 1), y + 30, w, 4))

    def update(self, enemies):
        if self.__energy > 0:
            self.tick += 1
            if self.tick >= self.rate:
                self.tick = 0
                attack = 0
                for enemy in enemies:
                    if self.__energy > 0 and attack < self.max_attack:
                        pos1 = (self.coordinates[0] + 16, self.coordinates[1] + 16)
                        pos2 = (enemy.pos[0] * 32 + enemy.pos_in_tile[0] + 16, enemy.pos[1] * 32 + enemy.pos_in_tile[1] + 16)
                        distance = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

                        if distance < self.__towerRange:
                            pip = Pip(self.coordinates, enemy)
                            self.__energy -= self.__energy_consumption
                            attack += 1
                            return pip
        else:
            if self.tick >= 60 * self.sleeping_time:
                self.tick = 0
                self.__energy = self.__energyMax

            self.tick += 1