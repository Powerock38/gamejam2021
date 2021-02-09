import pygame

class Menu:

    def __init__(self):

        self.__surface = pygame.Surface((1024, 768))
        self.__surface.blit(pygame.image.load("assets/Main.png"), (0, 0))
        self.__surface.blit(pygame.image.load("assets/button.png"), (261, 500))
        
    def draw(self, screen):
        
        screen.blit(self.__surface, (0, 0))
