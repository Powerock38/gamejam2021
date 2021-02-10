import pygame
from Utils import Utils

pygame.font.init()

class HUD:

    def __init__(self, garden, life = 100, water = 1, level = 0):
        """
        Initialise HUD at the right of the screen\n
        Parameters :\n
        \tgarden : The garden associated to this HUD
        \tlife : The life of the player at the start of the game
        \twater : The number of water money given at the start of the game
        \tlevel : The level at the start of the game
        """

        self.GARDEN = garden
        self.__life = life
        self.__water = water
        self.__level = level

        self.__surface = pygame.image.load("assets/ui/hud/hud_background.png")
        
        self.__water_image = pygame.image.load("assets/ui/hud/waterdrop.png")
        self.__heart_image = pygame.image.load("assets/ui/hud/heart.png")

        self.set_level(level)
        self.set_water(water)
        self.set_life(life)

        # Container for tower text + tower sprites
        self.__tower_container = pygame.Surface((self.__surface.get_width(), 80*7+50)) # (128, 80 per sprite + 50 TOWER title)
        self.__tower_container.set_colorkey(Utils.BLACK)
        
        # Surface for TOWER text
        tower_title_surface = pygame.Surface((self.__surface.get_width(), 50))
        tower_title_surface.set_colorkey(Utils.BLACK)

        # Create the tower text
        self.__font = self.get_font(25)
        tower_text = self.__font.render('Towers', False, Utils.WHITE)

        dim = self.__font.size('Towers')
        x = tower_title_surface.get_width() // 2
        y = tower_title_surface.get_height() // 2

        tower_title_surface.blit(tower_text, (x - dim[0] // 2, y - dim[1] // 2))
        self.__tower_container.blit(tower_title_surface, (0, 0))

        self.__towers_rect = []

        aGauche = False
        nb = 0
        for id, tower in Utils.TOWERS.items():

            sprite_surface = pygame.Surface((self.__tower_container.get_width()//2, 80))

            # Display name
            # Get the size wich will be occupated by the text
            self.__font = self.get_font(12)
            dim = self.__font.size(tower["name"])
            item_text = self.__font.render(tower["name"], False, Utils.WHITE)
            sprite_surface.blit(item_text, (32-dim[0]//2, 40))

            # Display price
            y = dim[1]
            price_text = self.__font.render(str(tower["price"]), False, Utils.WHITE)
            dim = self.__font.size(str(tower["price"]))
            
            x = 32-(dim[0]+24)//2 + 5
            sprite_surface.blit(price_text, (x, 40+y))

            dim = self.__font.size(str(tower["price"]))

            little_water = pygame.transform.scale(self.__water_image, (24,24))

            sprite_surface.blit(little_water, (x+dim[0], 40+y-4))

            
            # Display item sprite in sprite surface
            image = pygame.image.load(tower['path'])
            sprite_surface.blit(image, (32 - image.get_width()//2, 0))

            # Get sprite rectangle
            sprite_rect = sprite_surface.get_rect()

            x = 64 if aGauche else 0
            y = 50 + (80 * (nb//2))

            sprite_rect.x = x
            sprite_rect.y = y + 50

            # Create tower hover
            hover = pygame.image.load("assets/ui/hud/hover_board.png")
            self.__font = self.get_font(24)
            
            dim = self.__font.size(tower["name"])
            hover.blit(self.__font.render(tower["name"], False, Utils.WHITE), (150 - dim[0]//2, 55))

            self.__font = self.get_font(14)
            data_text_color = Utils.GREEN
            hover.blit(self.__font.render(str(tower["fire_rate"]) + " shot/s", False, data_text_color), (120, 84))
            hover.blit(self.__font.render(str(tower["damage"]) + "/shot", False, data_text_color), (110, 101))
            hover.blit(self.__font.render(str(tower["range"]) + " px", False, data_text_color), (99, 117))
            hover.blit(self.__font.render(str(tower["max_attack"]) + " enemies/shot", False, data_text_color), (139, 133))
            hover.blit(self.__font.render(str(tower["energy_consumption"]) + "/shot", False, data_text_color), (194, 151))
            hover.blit(self.__font.render(str(tower["sleeping_time"]) + " s", False, data_text_color), (149, 167))


            self.__towers_rect.append(
                {
                    "id":id,
                    "rect":sprite_rect, 
                    "hover":hover
                }
            )

            # Adding sprite surface to tower container
            self.__tower_container.blit(sprite_surface, (x,y))
        

            nb += 1
            aGauche = not aGauche

        self.__surface.blit(self.__tower_container, (0,50))

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)

        life_surface = pygame.image.load("assets/ui/hud/hud_life_background.png")

        # x, y cords
        x = life_surface.get_width() // 2
        y = life_surface.get_height() // 2

        # Create the text water
        self.__font = self.get_font(30)

        life_text = self.__font.render(str(self.get_life()), False, Utils.RED)
        dim = self.__font.size(str(self.get_life()))

        life_surface.blit(life_text, (30, (y - dim[1] // 2)-5))
        life_surface.blit(self.__heart_image, (30 + dim[0] + 5, y - self.__heart_image.get_height() // 2))

        self.__surface.blit(life_surface, (0,714))

    def get_water(self):
        return self.__water

    def set_water(self, water):

        self.__water = water

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)

        water_surface = pygame.image.load("assets/ui/hud/hud_water_background.png")

        # x, y cords
        x = water_surface.get_width() // 2
        y = water_surface.get_height() // 2

        # Create the text water
        self.__font = self.get_font(20)
        dim = self.__font.size(str(self.get_water()))

        if dim[0] + self.__water_image.get_width() > self.__surface.get_width():
            self.__font = self.get_font(18)
            dim = self.__font.size(str(self.get_water()))

        water_text = self.__font.render(str(self.get_water()), False, Utils.BLUE)

        water_surface.blit(water_text, ((x-10) - dim[0] // 2, y - dim[1] // 2))
        water_surface.blit(self.__water_image, ((x-10) - dim[0] // 2 + dim[0], y - dim[1] // 2))

        self.__surface.blit(water_surface, (0,660))

    def get_level(self):
        return self.__level

    def set_level(self, level):

        self.__level = level

        # Initialise font with the font available in assets/font
        self.__font = self.get_font(25)


        level_surface = pygame.image.load("assets/ui/hud/hud_level_background.png")

        # x, y cords
        x = level_surface.get_width() // 2
        y = level_surface.get_height() // 2

        # Create the level text
        level_text = self.__font.render('Wave ' + str(self.get_level() + 1), False, Utils.WHITE)
        dim = self.__font.size("Wave " + str(self.get_level()))
        level_surface.blit(level_text, (x - dim[0] // 2, y - dim[1] // 2))

        self.__surface.blit(level_surface, (0,0))

    def get_surface(self):
        return self.__surface
    
    def get_towers_rect(self):
        return self.__towers_rect

    def get_font(self, size):
        return pygame.font.Font('assets/font/comic_book.otf', size)

    def buy(self, x ,y):

        # Check for evry elem if mouse is in
        for elem in self.__towers_rect:
            rect = elem["rect"]
            if rect.collidepoint(x-896,y):
                tower = Utils.TOWERS[elem["id"]]
                if self.GARDEN.holding == None:
                    if self.get_water() >= tower['price']:
                        self.set_water(self.get_water() - tower['price'])
                        self.GARDEN.hold(elem['id'])
                else:
                    self.refund()

    def refund(self):

        if self.GARDEN.holding != None:
            self.set_water(self.get_water() + Utils.TOWERS[self.GARDEN.holding[0]]['price'])
            self.GARDEN.holding = None

    # Draw the element
    def draw(self, screen):

        screen.blit(self.__surface, (896,0))

        mx, my = pygame.mouse.get_pos()
        if mx >= 896:
            for tower in self.__towers_rect:
                rect = tower["rect"]
                if rect.collidepoint(mx-896,my):

                    display_x = mx-310
                    display_y = my-125 if my-125 >= 0 else 0

                    screen.blit(tower["hover"], (display_x,display_y))