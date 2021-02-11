import pygame

class Enemy:
    dirToSpriteLine = (3, 2, 0, 1)

    def __init__(self, enemy, pos):
        """
        Constructor of the Enemy class\n
        Parameters :\n
        \tsprite : sprite of the Tower (path png)
        \thp : health point of the enemy (int) (default 100)
        \tspeed : the speed of the enemy (int) (default 0.5)
        \tpos : position of the enemy (int) (default (0,0))
        """
        self.__sprites = enemy['sprites']
        self.hp = enemy['hp']
        self.__hpMax = self.hp
        self.__speed = enemy['speed']
        self.water = enemy['water']
        self.pos = pos
        self.pos_in_tile = [0, 0]
        self.__direction = 2
        self.__animTick = 0
        self.fly = enemy['fly']

    def draw(self, screen):
        """
        The draw funtion\n
        Parameters :\n
        \tscreen : the screen that draw the enemy
        """
        x, y = (32 * self.pos[0] + self.pos_in_tile[0], 32 * self.pos[1] + self.pos_in_tile[1])
        
        if self.__animTick >= 30:
            self.__animTick = 0
        
        screen.blit(self.__sprites[Enemy.dirToSpriteLine[self.__direction]][self.__animTick // 10], (x, y))
        
        self.__animTick += 1

        if self.hp != self.__hpMax:
            width = max(1, int((self.hp / self.__hpMax) * 28))
            pygame.draw.rect(screen, (20,10,10), (x + 1, y - 9, 32, 6))
            pygame.draw.rect(screen, (237,28,36), (x + 2, y - 8, width, 2))
            pygame.draw.rect(screen, (200,20,25), (x + 2, y - 6, width, 2))

    def move(self, direction):
        self.__direction = direction

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
