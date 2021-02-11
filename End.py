import pygame

pygame.mixer.init()
pygame.font.init()

class End:

    musicLoad = pygame.mixer.Sound("assets/musics/end.ogg")

    def __init__(self):
        self.score = 0
        self.__end = pygame.Surface((1024, 768))
        self.__buttons = [pygame.image.load("assets/ui/end/play_again.png"),
                          pygame.image.load("assets/ui/end/play_again_hover.png"),
                          pygame.image.load("assets/ui/end/quit.png"),
                          pygame.image.load("assets/ui/end/quit_hover.png")]

        self.__background = pygame.image.load("assets/ui/end/game_over.png")

        #Initilalisation of the music
        self.channel = pygame.mixer.Channel(0)
        self.channel.play(End.musicLoad,-1)
        self.channel.set_volume(0.25)

        #Setput the text area of wave that you achive
        self.__text_surface = pygame.Surface((200, 50))
        self.__text_surface.set_colorkey((0, 0, 0))
        self.__font_size = 40
        self.__font = pygame.font.Font('assets/font/comic_book.otf', self.__font_size)
        self.pseudo = ""
        self.__pseudo_surface = pygame.Surface((250, 50))
        self.__pseudo_surface.set_colorkey((0, 0, 0))

    def draw(self, screen):
        m_pos = pygame.mouse.get_pos()

        self.__end.blit(self.__background, (0, 0))
        
        if m_pos[0] >= 120 and m_pos[0] <= 462 and m_pos[1] >= 642 and m_pos[1] <= 738:
            self.__end.blit(self.__buttons[1], (120, 642))
            self.__end.blit(self.__buttons[2], (536, 642))

        elif m_pos[0] >= 536 and m_pos[0] <= 878 and m_pos[1] >= 642 and m_pos[1] <= 738:
            self.__end.blit(self.__buttons[0], (120, 642))
            self.__end.blit(self.__buttons[3], (536, 642))

        else:
            self.__end.blit(self.__buttons[0], (120, 642))
            self.__end.blit(self.__buttons[2], (536, 642))

        text = self.__font.render(str(self.score), False, (255, 255, 255))
        text2 = self.__font.render(self.pseudo, False, (255, 255, 255))
        self.__text_surface.blit(text, (0, 0))
        self.__pseudo_surface.fill((0, 0, 0))
        self.__pseudo_surface.blit(text2, (0, 0))
        self.__end.blit(self.__text_surface, (499 - len(str(self.score)) * self.__font_size / 4, 440))
        self.__end.blit(self.__pseudo_surface, (499 - len(self.pseudo) * self.__font_size / 4, 530))

        screen.blit(self.__end, (0, 0))
