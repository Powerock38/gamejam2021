import pygame


class Enemy:
    def __init__(self, sprite, hp = 100, speed = 2, pos = [0, 0]):
        self.__sprite = sprite
        self.__hp = hp
        self.__speed = speed
        self.pos = pos
        self.__posInTile = [0, 0]

    def draw(self, screen):
        screen.blit(self.__sprite, (32 * self.pos[0] + self.__posInTile[0], 32 * self.pos[1] + self.__posInTile[1]))

    def move(self, direction):
        if direction == 0:
            self.__posInTile[1] -= self.__speed
            if self.__posInTile[1] <= -32:
                self.pos[1] -= 1
                self.__posInTile = [0, 0]
        
        elif direction == 1:
            self.__posInTile[0] += self.__speed
            if self.__posInTile[0] >= 32:
                self.pos[0] += 1
                self.__posInTile = [0, 0]
        
        elif direction == 2:
            self.__posInTile[1] += self.__speed
            if self.__posInTile[1] >= 32:
                self.pos[1] += 1
                self.__posInTile = [0, 0]
        
        elif direction == 3:
            self.__posInTile[0] -= self.__speed
            if self.__posInTile[0] <= -32:
                self.pos[0] -= 1
                self.__posInTile = [0, 0]
