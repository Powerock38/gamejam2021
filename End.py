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

        self.__end.blit(pygame.image.load("assets/ui/end/game_over.png"), (0, 0))

        #Initilalisation of the music
        channel = pygame.mixer.Channel(0)
        channel.play(End.musicLoad)
        channel.set_volume(0.25)

        #Setput the text area of wave that you achive
        self.__textSurface = pygame.Surface((100000,100))
        self.__textSurface.set_colorkey((0, 0, 0))
        self.__fontSize = 40
        self.__font = pygame.font.Font('assets/font/comic_book.otf', self.__fontSize)

#(342,96)
    def draw(self, screen):
        m_pos = pygame.mouse.get_pos()

#coordinates of the text area : (512,460)
        if m_pos[0] >= 120 and m_pos[0] <= 462 and m_pos[1] >= 642 and m_pos[1] <= 738:
            self.__end.blit(self.__buttons[1], (120, 642))

        elif m_pos[0] >= 536 and m_pos[0] <= 878 and m_pos[1] >= 642 and m_pos[1] <= 738:
            self.__end.blit(self.__buttons[3], (536, 642))

        else:
            self.__end.blit(self.__buttons[0], (120, 642))
            self.__end.blit(self.__buttons[2], (536, 642))

        text = self.__font.render(str(self.score), False, (255, 255, 255))
        self.__textSurface.blit(text, (0,0))
        self.__end.blit(self.__textSurface, (499 - len(str(self.score)) * self.__fontSize / 4, 480))

        screen.blit(self.__end, (0, 0))
