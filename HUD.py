import pygame

class HUD:

    def __init__(self, water = 0):
        self.__life = life
        self.__water = water

        self.__hud = pygame.surface((128,768))
        self.__hud.fill((89,89,89))

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def get_water(self):
        return self.__water

    def set_water(self, water):
        self.__water = water

    def get_surface(self):
        return self.__hud
    
