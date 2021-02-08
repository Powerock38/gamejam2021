import pygame
from Utils import Utils

class HUD:

    def __init__(self, life = 100, water = 1, level = 1):
        self.__life = life
        self.__water = water
        self.__level = level

        self.__surface = pygame.Surface((128,768))
        self.__surface.fill(Utils.GRAY)

        pygame.font.init()

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)

        # Create the text level
        self.__level_text = self.__font.render('Level ' + str(self.get_level()), False, Utils.WHITE)
        # Create the text level
        self.__tower_text = self.__font.render('Towers ', True, Utils.WHITE)

        font = self.get_font(15)
        # Create the text water
        self.__water_text = font.render('Water ' + str(self.get_water()), False, Utils.BLUE)

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
        return pygame.font.Font('assets/font/comic_book.otf', size)

    # Draw the element
    def draw(self, screen):

        # Render top text
        self.__surface.blit(self.__level_text, (15, 25))
        self.__surface.blit(self.__tower_text, (18, 87))

        # Render Water text
        self.__surface.blit(self.__water_text, (10, 730))


        # Display waterdrop
        dim = self.__font.size("Water : " + str(self.get_water()))
        image = pygame.image.load("assets/waterdrop.png")
        self.__surface.blit(image, (dim[0]-5, 730))


        # Initialise font with the font available in assets/font
        self.__font = self.get_font(12)

        # Display towers items col by col by taking the first half part of array and the second after
        for col in range(2):
            for elem in range(int(len(Utils.TOWERS)/2)):

                # Display item
                elem_number = elem + (col*int(len(Utils.TOWERS)/2))
                image = pygame.image.load(Utils.TOWERS[elem_number]["path"]) # à opti
                
                x = 20 + (55*col)
                y = 130 + (80*elem)
                self.__surface.blit(image, (x, y))

                # Display item name

                # Position x at mid of item width and y at the bottom of item
                x += 16
                y += 32

                # Get the size wich will be occupated by the text
                dim = self.__font.size(Utils.TOWERS[elem_number]["name"])

                # Display name
                item_text = self.__font.render(Utils.TOWERS[elem_number]["name"], False, Utils.WHITE)
                self.__surface.blit(item_text, (x-(int(dim[0]/2)), y+5))

                # # Display price
                # dim = font.size("Price : " + str(Utils.TOWERS[elem_number]["name"]))

                # item_text = font.render("Price : " + str(Utils.TOWERS[elem_number]["price"]), False, Utils.WHITE)
                # self.__surface.blit(item_text, (x-(int(dim[0]/2)), (y+5+(int(dim[1]/2)))))



        screen.blit(self.__surface, (896,0))
