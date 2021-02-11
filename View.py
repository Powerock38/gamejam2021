import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import traceback

#Set the default position of the pygame window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

class View:
    __clock = None
    __screen = None
    crashed = False

    __graphic_elements = []

    def __init__(self, graphic_elements, update, eventListener):
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(size = (1024, 768))
        self.__graphic_elements = graphic_elements
        pygame.display.set_icon(pygame.image.load('assets/fruits-veggies/apple_red.png'))
        pygame.display.set_caption('Garden Defense')

        try:
            while not self.crashed:
                self.__clock.tick(60)
                #print(self.__clock.get_fps())

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        self.crashed = True
                    else:
                        self.__graphic_elements = eventListener(event, self.__graphic_elements)

                self.__graphic_elements = update(self.__graphic_elements)
                
                self.__screen.fill((0, 0, 0))
                
                for element in self.__graphic_elements:
                    element.draw(self.__screen)
                pygame.display.update()

            pygame.quit()
        except:
            print(traceback.print_exc())
            pygame.quit()
