import pygame
from Utils import Utils

class HUD:

    def __init__(self, life = 100, water = 1, level = 1):
        self.__life = life
        self.__water = water
        self.__level = level

        self.__surface = pygame.Surface((128,768))
        self.__surface.fill(Utils.GRAY)
        
        for col in range(2):
            for elem in range(int(len(Utils.TOWERS)/2)):
                elem_number = elem + (col*int(len(Utils.TOWERS)/2))
                image = pygame.image.load(Utils.TOWERS[elem_number]["path"])
                
                x = 20 + (55 * col)
                y = 130 + (85 * elem)
                self.__surface.blit(image, (x, y))

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


        pygame.font.init()

        # Initialise font with the font available in assets/font
        font = self.get_font(25)

        # x, y cords
        x = int(self.get_surface().get_width() / 2)
        y = 25

        # Create the level text
        level_text = font.render('Level ' + str(self.get_level()), False, Utils.WHITE)
        dim = font.size("Level " + str(self.get_level()))
        self.__surface.blit(level_text, (x - (int(dim[0] / 2)), y))

        # Create the tower text
        tower_text = font.render('Towers ', False, Utils.WHITE)
        
        self.__surface.blit(tower_text, (18, 87))

        font = self.get_font(20)
        # Create the text water
        water_text = font.render('Water ' + str(self.get_water()), False, Utils.BLUE)

        dim = font.size("Water : " + str(self.get_water()))
        image = pygame.image.load("assets/waterdrop.png")
        self.__surface.blit(water_text, (x - (int((dim[0]) / 2)), 730))
        self.__surface.blit(image, (dim[0] - 10, 730))


        font = self.get_font(12)

        # Display towers items col by col by taking the first half part of array and the second after
        for col in range(2):
            for elem in range(int(len(Utils.TOWERS)/2)):

                # Display item name

                # Position x at mid of item width and y at the bottom of item
                
                elem_number = elem + (col*int(len(Utils.TOWERS)/2))
                
                x = 36 + (55 * col)
                y = 162 + (85 * elem)

                # Get the size wich will be occupated by the text
                dim = font.size(Utils.TOWERS[elem_number]["name"])

                # Display name
                item_text = font.render(Utils.TOWERS[elem_number]["name"], False, Utils.WHITE)
                self.__surface.blit(item_text, (x-(int(dim[0]/2)), y+5))

                # Display price
                item_text = font.render(str(Utils.TOWERS[elem_number]["price"]), False, Utils.WHITE)
                x -= 10
                self.__surface.blit(image, (x-dim[0]/2, y+dim[1]))
                self.__surface.blit(item_text, ((x-dim[0]/2) + 32, y+dim[1] + 8))



        screen.blit(self.__surface, (896,0))
