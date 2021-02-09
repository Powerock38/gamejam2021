import pygame
from Utils import Utils

pygame.font.init()

class HUD:


    def __init__(self, garden, life = 100, water = 1, level = 1):
        """
        Initialise HUD at the right of the screen\n
        Parameters :\n
        \tlife : The life of the player at the start of the game
        \twater : The number of water money given at the start of the game
        \tlevel : The level at the start of the game
        """

        self.GARDEN = garden
        self.__life = life
        self.__water = water
        self.__level = level

        self.__surface = pygame.Surface((128,768))
        self.__surface.fill(Utils.GRAY)
        
        self.__water_image = pygame.image.load("assets/waterdrop.png")

        self.set_water(water)
        self.set_level(level)

        # Create the tower text
        self.__font = self.get_font(25)
        tower_text = self.__font.render('Towers ', False, Utils.WHITE)
        self.__surface.blit(tower_text, (18, 87))

        self.__towers_rect = []

        aGauche = False
        nb = 0
        for id, tower in Utils.TOWERS.items():
            # elem_number = elem + (col*int(len(Utils.TOWERS)/2))
            image = pygame.image.load(tower['path'])
            image_rect = image.get_rect()
            
            # Display item sprite
            x = 20 + (55 if aGauche else 0)
            y = 130 + (85 * (nb//2))
            
            image_rect.x = x
            image_rect.y = y
            self.__surface.blit(image, image_rect)

            # Create tower hover
            hover = pygame.Surface((50,15))
            hover.fill(Utils.RED)
            self.__font = self.get_font(10)
            hover_text = self.__font.render("Id : " + id, False, Utils.BLACK)
            hover.blit(hover_text, (5,5))

            self.__towers_rect.append(
                {
                    "id":id,
                    "rect":image_rect, 
                    "hover":hover
                }
            )

            # Display name
            x = 36 + (55 if aGauche else 0)
            y = 162 + (85 * (nb//2))
            # Get the size wich will be occupated by the text
            self.__font = self.get_font(12)
            dim = self.__font.size(tower["name"])

            item_text = self.__font.render(tower["name"], False, Utils.WHITE)
            self.__surface.blit(item_text, (x-(int(dim[0]/2)), y+5))

            # Display price
            item_text = self.__font.render(str(tower["price"]), False, Utils.WHITE)
            x -= 10
            self.__surface.blit(self.__water_image, (x-dim[0]/2, y+dim[1]))
            self.__surface.blit(item_text, ((x-dim[0]/2) + 32, y+dim[1] + 8))

            nb += 1
            aGauche = not aGauche

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def get_water(self):
        return self.__water

    def set_water(self, water):

        self.__water = water

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)

        x = int(self.get_surface().get_width() / 2)
        y = 25

        box = pygame.Surface((self.__surface.get_width(),30))
        box.fill(Utils.GRAY)
        self.__surface.blit(box, (0,730))

        # Create the text water
        self.__font = self.get_font(20)
        self.__water_text = self.__font.render('Water ' + str(self.get_water()), False, Utils.BLUE)

        dim = self.__font.size("Water : " + str(self.get_water()))
        self.__surface.blit(self.__water_text, (x - (int((dim[0]) / 2)), 730))
        self.__surface.blit(self.__water_image, (dim[0] - 10, 730))

    def get_level(self):
        return self.__level

    def set_level(self, level):

        self.__level = level

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)

        # x, y cords
        x = int(self.get_surface().get_width() / 2)
        y = 25

        box = pygame.Surface((self.__surface.get_width(),30))
        box.fill(Utils.GRAY)
        self.__surface.blit(box, (0,y))

        # Create the level text
        self.__level_text = self.__font.render('Level ' + str(self.get_level()), False, Utils.WHITE)
        dim = self.__font.size("Level " + str(self.get_level()))
        self.__surface.blit(self.__level_text, (x - (int(dim[0] / 2)), y))

    def get_surface(self):
        return self.__surface
    
    def get_towers_rect(self):
        return self.__towers_rect

    def get_font(self, size):
        return pygame.font.Font('assets/font/comic_book.otf', size)

    # Draw the element
    def draw(self, screen):

        screen.blit(self.__surface, (896,0))

    def buy(self, x ,y):
        if True: # self.get_water() >= vegetable['price']:
            # self.set_water(self.get_water() - tower['price'])
            self.GARDEN.hold('apple')