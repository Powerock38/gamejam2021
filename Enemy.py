import pygame


class Enemy:
    def __init__(self, sprite, hp = 100, speed = 0.5, pos = [0, 0]):
        """
        Constructor of the Enemy class\n
        Parameters:\n
        \tsprite : sprite of the Tower (path png)
        \thp : health point of the enemy (int) (default 100)
        \tspeed : the speed of the enemy (int) (default 0.5)
        \tpos : position of the enemy (int) (default (0,0))
        """
        self.__sprite = sprite
        self.__hp = hp
        self.__speed = speed
        self.pos = pos
        self.pos_in_tile = [0, 0]

    def attack(self, damage = 1):
        """
        Hurt the enemy\n
        Parameters :\n
        \tdamage : the damage to hurt the enemy (int) (default 1)\n
        Return :\n
        None
        """
        self.__hp -= damage

    def draw(self, screen):
        """
        The draw funtion\n
        Parameters :\n
        \tscreen :  the screen that draw the enemy
        """
        screen.blit(self.__sprite, (32 * self.pos[0] + self.pos_in_tile[0], 32 * self.pos[1] + self.pos_in_tile[1]))

    def move(self, direction):
        if direction == 0:
            self.pos_in_tile[1] -= self.__speed
            if self.pos_in_tile[1] <= -32:
                self.pos[1] -= 1
                self.pos_in_tile = [0, 0]
        
        elif direction == 1:
            self.pos_in_tile[0] += self.__speed
            if self.pos_in_tile[0] >= 32:
                self.pos[0] += 1
                self.pos_in_tile = [0, 0]
        
        elif direction == 2:
            self.pos_in_tile[1] += self.__speed
            if self.pos_in_tile[1] >= 32:
                self.pos[1] += 1
                self.pos_in_tile = [0, 0]
        
        elif direction == 3:
            self.pos_in_tile[0] -= self.__speed
            if self.pos_in_tile[0] <= -32:
                self.pos[0] -= 1
                self.pos_in_tile = [0, 0]
