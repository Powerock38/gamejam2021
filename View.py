import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import copy
import pygame

#Set the default position of the pygame window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

class View:
    _clock = None
    _screen = None
    _crashed = False
    
    _args = []
    _graphic_elements = []

    def __init__(self, args, graphic_elements, calculations, update):
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(size = (1024, 768))
        self._args = args
        self._graphic_elements = graphic_elements

        try:
            while not self._crashed:
                self._clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._crashed = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self._crashed = True

                mouse_pos = pygame.mouse.get_pos()
                
                self._args = copy.deepcopy(calculations(self._args))

                self._args, self._graphic_elements = update(self._args, self._graphic_elements)
                
                self._screen.fill((0, 0, 0))
                
                for element in self._graphic_elements:
                    element.draw(self._screen)

                pygame.display.update()

            pygame.quit()
        except:
            print(sys.exc_info()[0], sys.exc_info()[1])
            pygame.quit()
