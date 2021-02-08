import pygame

class Garden:

    def __init__(self, tiles):
        self.__tiles = tiles

    def draw(self, screen):
        image_path = "assets/tilesets/plowed_soil.png"

        image = pygame.image.load(image_path)
        tile = image.subsurface(((32, 0), (32, 32)))

        for i in range(32):
            for j in range(24):
                screen.blit(tile, (32 * i, 32 * j))
