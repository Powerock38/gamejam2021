import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import traceback
import time

#Set the default position of the pygame window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

class View:
    __clock = None
    __screen = None
    __crashed = False

    __graphic_elements = []

    def __init__(self, graphic_elements, update, eventListener):
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(size = (1024, 768))
        self.__graphic_elements = graphic_elements

        try:
            while not self.__crashed:
                t1 = time.time()
                self.__clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        self.__crashed = True
                    else:
                        # self.__graphic_elements = eventListener(event, self.__graphic_elements)
                        eventListener(event, self.__graphic_elements)

                self.__graphic_elements = update(self.__graphic_elements)
                
                self.__screen.fill((0, 0, 0))
                
                for element in self.__graphic_elements:
                    element.draw(self.__screen)
                pygame.display.update()

                #print(1/(time.time() - t1))

            pygame.quit()
        except:
            print(traceback.print_exc())
            pygame.quit()
