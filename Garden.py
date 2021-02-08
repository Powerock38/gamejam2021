import pygame

class Garden:

    def __init__(self, life = 10, water = 0):
        self.__life = life
        self.__water = water
        #self.__sun = 0
        self.__tiles = []

    def get_life(self):
        return self.__life

    def get_water(self):
        return self.__water

    def draw(self, screen):
        image_path = "assets\Strawberries.png"

        image = pygame.image.load(image_path)

        for i in range(32):
            for j in range(24):
                screen.blit(image, (32 * i, 32 * j))
