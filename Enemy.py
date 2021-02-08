import pygame


class Enemy:
    def __init__(self, sprite, hp, damage, pos = [0, 0]):
        self.__sprite = sprite
        self.__hp = hp
        self.__pos = pos
        self.__posPercent = [0, 0]
        self.__speed = 2

    def draw(self, screen):
        screen.blit(self.__sprite, self.__pos)

    def move(self, direction):
        if direction == 0:
            self.__posPercent[1] += self.__speed
            if self.__posPercent[1] >= 32:
                self.__pos[1] += 1
                self.__posPercent = [0, 0]
        
        elif direction == 1:
            self.__posPercent[0] += self.__speed
            if self.__posPercent[0] >= 32:
                self.__pos[0] += 1
                self.__posPercent = [0, 0]
        
        elif direction == 2:
            self.__posPercent[1] -= self.__speed
            if self.__posPercent[1] <= -32:
                self.__pos[1] -= 1
                self.__posPercent = [0, 0]
        
        elif direction == 3:
            self.__posPercent[0] -= self.__speed
            if self.__posPercent[0] <= -32:
                self.__pos[0] -= 1
                self.__posPercent = [0, 0]
