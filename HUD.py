import pygame
from Utils import Utils

class HUD:

    def __init__(self, life = 0, water = 0, level = 1):
        self.__life = life
        self.__water = water
        self.__level = level
        self.initialise_surface()

    def initialise_surface(self):
        self.__surface = pygame.Surface((128,768))
        self.__surface.fill(Utils.GRAY)

        pygame.font.init()

        # Initialise font with the font available in assets/font
        font = self.get_font(27)

        # Create the text level
        self.__level_text = font.render('Level ' + str(self.__level), True, Utils.WHITE)
        # Create the text level
        self.__tower_text = font.render('Towers ', True, Utils.WHITE)

        # Create the text water
        self.__water_text = font.render('Water ' + str(self.__water), True, Utils.BLUE)

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def get_water(self):
        return self.__water

    def set_water(self, water):
        self.__water = water

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_surface(self):
        return self.__surface
    
    def get_towers(self):
        return self.__TOWERS

    def get_font(self, size):
        return pygame.font.Font('assets/font/hey_comic.ttf', size)

    # Draw the element
    def draw(self, screen):

        # Render text
        self.__surface.blit(self.__level_text, (15, 25))
        self.__surface.blit(self.__tower_text, (18, 87))

        self.__surface.blit(self.__water_text, (15, 730))

        # Initialise font with the font available in assets/font
        font = self.get_font(12)

        # Display towers items col by col by taking the first half part of array and the second after
        for col in range(2):
            for elem in range(int(len(Utils.TOWERS)/2)):

                # Display item
                elem_number = elem + (col*int(len(Utils.TOWERS)/2))
                print(Utils.TOWERS[elem_number]["path"])
                image = pygame.image.load(Utils.TOWERS[elem_number]["path"])
                
                x = 20 + (55*col)
                y = 130 + (70*elem)
                self.__surface.blit(image, (x, y))

                # Display item name

                # Position x at mid of item width and y at the bottom of item
                x += 16
                y += 32
                # Get the size wich will be occupated by the text
                dim = font.size(Utils.TOWERS[elem_number]["name"])

                # Create text surface
                item_text = font.render(Utils.TOWERS[elem_number]["name"], False, Utils.WHITE)
                # Render text
                self.__surface.blit(item_text, (x-(int(dim[0]/2)), y+5))



        screen.blit(self.__surface, (896,0))
