import pygame

class Enemy:
    def __init__(self, sprite, hp = 100, speed = 0.5, pos = [0, 0]):
        """
        Constructor of the Enemy class\n
        Parameters :\n
        \tsprite : sprite of the Tower (path png)
        \thp : health point of the enemy (int) (default 100)
        \tspeed : the speed of the enemy (int) (default 0.5)
        \tpos : position of the enemy (int) (default (0,0))
        """
        self.__sprite = sprite
        self.hp = hp
        self.__hpMax = hp
        self.__speed = speed
        self.pos = pos
        self.pos_in_tile = [0, 0]

    def draw(self, screen):
        """
        The draw funtion\n
        Parameters :\n
        \tscreen : the screen that draw the enemy
        """
        x, y = (32 * self.pos[0] + self.pos_in_tile[0], 32 * self.pos[1] + self.pos_in_tile[1])
        screen.blit(self.__sprite, (x, y))
        if self.hp != self.__hpMax:
            width = max(1, int((self.hp / self.__hpMax) * 32))
            pygame.draw.rect(screen, (20,10,10), (x - 1, y - 9, 32, 6))
            pygame.draw.rect(screen, (237,28,36), (x, y - 8, width, 2))
            pygame.draw.rect(screen, (200,20,25), (x, y - 6, width, 2))

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
