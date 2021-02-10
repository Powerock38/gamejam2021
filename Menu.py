import pygame

pygame.mixer.init()
pygame.font.init()

class Menu:

    def __init__(self):
        
        self.page = "Menu"

        self.__menu = pygame.Surface((1024, 768))
        self.__rules = pygame.Surface((1024, 768))
        self.__credits = pygame.Surface((1024, 768))
        self.__buttons = [pygame.image.load("assets/play.png"),
                          pygame.image.load("assets/rules.png"),
                          pygame.image.load("assets/credits.png"),
                          pygame.image.load("assets/back.png"),
                          pygame.image.load("assets/play_hover.png"),
                          pygame.image.load("assets/rules_hover.png"),
                          pygame.image.load("assets/credits_hover.png"),
                          pygame.image.load("assets/back_hover.png")]

        #Initilalisation of the music
        musicLoad = pygame.mixer.Sound("assets/musics/tmp_menu.ogg")
        pygame.mixer.Channel(0).play(musicLoad, -1)
        pygame.mixer.Channel(0).set_volume(0.1)

        self.__menu.blit(pygame.image.load("assets/menu.png"), (0, 0))
        self.__rules.blit(pygame.image.load("assets/rules_page.png"), (0, 0))
        self.__credits.blit(pygame.image.load("assets/credits_page.png"), (0, 0))

        self.__scoreboard = pygame.Surface((200, 260))
        self.__scoreboard.set_alpha(0)
        
        font = pygame.font.Font('assets/font/comic_book.otf', 20)
        text = font.render('Towers', False, (255, 255, 255))
        self.__scoreboard.blit(text, (0, 0))

        self.__menu.blit(self.__scoreboard, (52, 433))
        
    def draw(self, screen):
        m_pos = pygame.mouse.get_pos()
        if self.page == "Menu":
            if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 350 and m_pos[1] <= 472:
                self.__menu.blit(self.__buttons[4], (295, 350))
                self.__menu.blit(self.__buttons[1], (341, 492))
                self.__menu.blit(self.__buttons[2], (341, 608))
            elif m_pos[0] >= 341 and m_pos[0] <= 683 and m_pos[1] >= 492 and m_pos[1] <= 588:
                self.__menu.blit(self.__buttons[0], (295, 350))
                self.__menu.blit(self.__buttons[5], (341, 492))
                self.__menu.blit(self.__buttons[2], (341, 608))
            elif m_pos[0] >= 341 and m_pos[0] <= 683 and m_pos[1] >= 608 and m_pos[1] <= 704:
                self.__menu.blit(self.__buttons[0], (295, 350))
                self.__menu.blit(self.__buttons[1], (341, 492))
                self.__menu.blit(self.__buttons[6], (341, 608))
            else:
                self.__menu.blit(self.__buttons[0], (295, 350))
                self.__menu.blit(self.__buttons[1], (341, 492))
                self.__menu.blit(self.__buttons[2], (341, 608))
                        
            screen.blit(self.__menu, (0, 0))
                
            
        elif self.page == "Rules":
            if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 608 and m_pos[1] <= 730:
                self.__rules.blit(self.__buttons[3], (341, 640))
            else:
                self.__rules.blit(self.__buttons[7], (341, 640))
                
            screen.blit(self.__rules, (0, 0))
            
        elif self.page == "Credits":
            if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 608 and m_pos[1] <= 730:
                self.__credits.blit(self.__buttons[3], (341, 640))
            else:
                self.__credits.blit(self.__buttons[7], (341, 640))
                
            screen.blit(self.__credits, (0, 0))
