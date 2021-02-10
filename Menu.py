import pygame

pygame.mixer.init()
pygame.font.init()

class Menu:

    musicLoad = pygame.mixer.Sound("assets/musics/menu.ogg")

    def __init__(self):
        
        self.page = "Menu"

        self.__menu = pygame.Surface((1024, 768))
        self.__rules = pygame.Surface((1024, 768))
        self.__credits = pygame.Surface((1024, 768))
        self.__buttons = [pygame.image.load("assets/ui/menu/play.png"),
                          pygame.image.load("assets/ui/menu/rules.png"),
                          pygame.image.load("assets/ui/menu/credits.png"),
                          pygame.image.load("assets/ui/menu/back.png"),
                          pygame.image.load("assets/ui/menu/play_hover.png"),
                          pygame.image.load("assets/ui/menu/rules_hover.png"),
                          pygame.image.load("assets/ui/menu/credits_hover.png"),
                          pygame.image.load("assets/ui/menu/back_hover.png")]

        #Initilalisation of the music
        channel = pygame.mixer.Channel(0)
        channel.play(Menu.musicLoad,-1)
        channel.set_volume(0.25)

        self.__menu.blit(pygame.image.load("assets/ui/menu/menu.png"), (0, 0))
        self.__rules.blit(pygame.image.load("assets/ui/menu/rules_page.png"), (0, 0))
        self.__credits.blit(pygame.image.load("assets/ui/menu/credits_page.png"), (0, 0))

        self.__scoreboard = pygame.Surface((200, 260))
        self.__scoreboard.set_colorkey((0, 0, 0))

        size = 21
        font = pygame.font.Font('assets/font/comic_book.otf', size)

        f = open("scoreboard", "r", encoding = "utf-8")
        scoreboard = f.read().split("\n")
        f.close()

        for i, x in enumerate(scoreboard):
            text = x.split(" : ")
            t1 = font.render(text[0], False, (255, 255, 255))
            t2 = font.render(": " + text[1], False, (255, 255, 255))
            self.__scoreboard.blit(t1, (0, i * (size + 2)))
            self.__scoreboard.blit(t2, (130, i * (size + 2)))

        self.__menu.blit(self.__scoreboard, (50, 433))
        
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
                self.__rules.blit(self.__buttons[7], (341, 640))
            else:
                self.__rules.blit(self.__buttons[3], (341, 640))
                
            screen.blit(self.__rules, (0, 0))
            
        elif self.page == "Credits":
            if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 608 and m_pos[1] <= 730:
                self.__credits.blit(self.__buttons[7], (341, 640))
            else:
                self.__credits.blit(self.__buttons[3], (341, 640))
                
            screen.blit(self.__credits, (0, 0))
