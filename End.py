import pygame

pygame.mixer.init()
pygame.font.init()

class End:

    musicLoad = pygame.mixer.Sound("assets/musics/end.ogg")

    def __init__(self):
        self.__menu = pygame.Surface((1024, 768))
        self.__rules = pygame.Surface((1024, 768))
        self.__credits = pygame.Surface((1024, 768))
        self.__buttons = [pygame.image.load("assets/ui/end/play_again.png"),
                          pygame.image.load("assets/ui/end/play_again_hover.png"),
                          pygame.image.load("assets/ui/end/quit.png"),
                          pygame.image.load("assets/ui/end/quit_hover.png"),
                          pygame.image.load("assets/ui/end/game_over.png")]

        #Initilalisation of the music
        channel = pygame.mixer.Channel(0)
        channel.play(End.musicLoad, -1)
        channel.set_volume(0.5)

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
