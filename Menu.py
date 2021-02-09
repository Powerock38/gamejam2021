import pygame

class Menu:

    def __init__(self):

        self.__surface = pygame.Surface((1024, 768))
        self.__surface.blit(pygame.image.load("assets/main.png"), (0, 0))
        self.__surface.blit(pygame.image.load("assets/play.png"), (295, 350))
        self.__surface.blit(pygame.image.load("assets/rules.png"), (341, 492))
        self.__surface.blit(pygame.image.load("assets/credits.png"), (341, 608))
        
    def draw(self, screen):
        screen.blit(self.__surface, (0, 0))
