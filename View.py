import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import copy
import pygame
import traceback
import math as m
from Pip import Pip
from Tower import Tower
import time

#Set the default position of the pygame window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

class View:
    __clock = None
    __screen = None
    __crashed = False

    __hover = False
    
    __graphic_elements = []

    def __init__(self, graphic_elements, update):
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(size = (1024, 768))
        self.__graphic_elements = graphic_elements

        try:
            while not self.__crashed:
                t1 = time.time()
                self.__clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__crashed = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and not self.__hover:
                        self.__graphic_elements.append(Tower(
                            pygame.image.load("assets/fruits-veggies/Acorn.png"),
                            "hover",
                            1,
                            1,
                            (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                             pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32)
                        ))
                        self.__hover = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and self.__hover:
                        for g in graphic_elements:
                            if isinstance(g, Pip) and g.get_name() == "hover":
                                graphic_elements.remove(g)
                                del g
                        self.__hover = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.__crashed = True
                        elif event.key == pygame.K_SPACE:
                            self.__graphic_elements.append(Tower(
                                pygame.image.load("assets/fruits-veggies/Acorn.png"),
                                "Acorn",
                                1,
                                1,
                                (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                                 pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32)
                            ))
                        elif event.key == pygame.K_a:
                            for elem in self.__graphic_elements:
                                if isinstance(elem, Tower) and elem.get_name() != "hover":
                                    self.__graphic_elements.append(elem.attack(m.pi/2))

                mouse_pos = pygame.mouse.get_pos()

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
