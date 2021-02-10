import pygame

class Menu:
    pygame.mixer.init()

    def __init__(self):
        
        self.page = "Menu"

        self.__menu = pygame.Surface((1024, 768))
        self.__rules = pygame.Surface((1024, 768))
        self.__credits = pygame.Surface((1024, 768))

        background = pygame.image.load("assets/menu.png")
        play_button = pygame.image.load("assets/play.png")

        #Initilalisation of the music
        pygame.mixer.music.load("assets/musics/tmp_menu.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        self.__menu.blit(background, (0, 0))
        self.__menu.blit(play_button, (295, 350))
        self.__menu.blit(pygame.image.load("assets/rules.png"), (341, 492))
        self.__menu.blit(pygame.image.load("assets/credits.png"), (341, 608))
        self.__menu.blit(pygame.image.load("assets/farmer.png"), (900, 550))
        
        self.__rules.blit(background, (0, 0))
        self.__rules.blit(play_button, (295, 608))
        
        self.__credits.blit(background, (0, 0))
        self.__credits.blit(play_button, (295, 608))
        
    def draw(self, screen):
        if self.page == "Menu":
            screen.blit(self.__menu, (0, 0))
        elif self.page == "Rules":
            screen.blit(self.__rules, (0, 0))
        elif self.page == "Credits":
            screen.blit(self.__credits, (0, 0))
