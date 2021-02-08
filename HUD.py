import pygame

class HUD:

    __GRAY = (89,89,89)
    __BLACK = (0,0,0)
    __WHITE = (255,255,255)
    __BLUE = (0,120,255)

    __TOWERS = ["apple_red",
                "pear",
                "banana", 
                "tomato",
                "peach",
                "orange",
                "cherry",
                # second col
                "potatoe",
                "pepper_green",
                "lettuce",
                "carrot",
                "squash",
                "aubergine",
                "broccoli"]

    def __init__(self, life = 0, water = 0, level = 1):
        self.__life = life
        self.__water = water
        self.__level = level
        self.initialise_surface()

    def initialise_surface(self):
        self.__surface = pygame.Surface((128,768))
        self.__surface.fill(self.__GRAY)

        pygame.font.init()

        # Initialise font with the default font
        font = pygame.font.Font('assets/font/hey_comic.ttf', 27)

        # Create the text level
        self.__levelText = font.render('Level ' + str(self.__level), True, self.__WHITE)
        # Create the text level
        self.__towerText = font.render('Towers ', True, self.__WHITE)


        # Create the text water
        self.__waterText = font.render('Water ' + str(self.__water), True, self.__BLUE)

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
    
    # Draw the element
    def draw(self, screen):

        # Render text
        self.__surface.blit(self.__levelText, (15, 25))
        self.__surface.blit(self.__towerText, (18, 87))

        self.__surface.blit(self.__waterText, (15, 730))

        # Render towers item
        
        image_path = "assets/fruits-veggies/"

        # Display towers items col by col by taking the first half part of array and the second after
        for y in range(2):
            for elem in range(int(len(self.__TOWERS)/2)):
                image = pygame.image.load(image_path + self.__TOWERS[elem + (y*int(len(self.__TOWERS)/2))] + ".png")
                
                self.__surface.blit(image, (20 + (55*y), 130 + (70*elem)))



        screen.blit(self.__surface, (896,0))
