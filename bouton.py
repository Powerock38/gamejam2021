#Imports
from pygame import draw
from pygame import Rect
from pygame import font
from Utils import Utils

font.init()

class Bouton:
    """Classe permettant de créer des boutons et de les afficher avec pygame"""
    

    def __init__(self, rect_infos, data):
        """Constructeur de la classe"""

        self.__rect_infos = rect_infos
        self.__rect = Rect(rect_infos)

        self.__default_color = (100, 100, 100)
        self.__pressed_color = (50, 50, 50)
        self.__hover_color = (150, 150, 150)

        self.__changed = True
        self.__hover = False
        self.__pressed = False

        self.__data = data

        self.__hover_surface = pygame.Surface((300,150))
        self.__hover_surface.fill((255,0,0))

    def get_hover_surface(self):
            return self.__hover_surface

    def get_rectangle(self):
        """Retourne le rectangle du bouton"""
        
        return self.__rect

    def get_rectangle_infos(self):
        
        return self.__rect_infos

    def draw(self, surface, update_list):
        """Dessine le bouton"""

        if self.__changed:
            w = self.__rect_infos[1][0]
            h = self.__rect_infos[1][1]
            x = self.__rect_infos[0][0]
            y = self.__rect_infos[0][1]

            if self.__hover:
                c = self.__hover_color
            elif self.__pressed:
                c = self.__pressed_color
            else:
                c = self.__default_color
            
            draw.rect(surface, c, ((x, y), (w, h)))
            surface.blit(self.__hover_surface, (200, 50))
            
            self.__changed = False

            update_list.append(self.__rect_infos)
            

        return update_list


    def react(self, mouse_coordinates, mouse_pressed):
        """Fait réagir le bouton en fonction de la situation"""
        
        if self.__rect.collidepoint(mouse_coordinates):
            if mouse_pressed:
                if not self.__pressed:
                    self.__pressed = True
                    self.__hover = False
                    self.__changed = True
            else:
                if not self.__hover:
                    self.__pressed = False
                    self.__hover = True
                    self.__changed = True
        else:
            if self.__hover or self.__pressed:
                self.__pressed = False
                self.__hover = False
                self.__changed = True
        
        state = "none"
        if self.__pressed:
            if self.__changed:
                state = "pressed"
            else:
                state = "pressing"
        elif self.__hover:
            state = "hover"
        
        return state
            

if __name__ == "__main__":
    
    import pygame
    screen = pygame.display.set_mode(size = (600, 600))
    crashed = False

    pomme = {"id":"apple",
                "path":"assets/fruits-veggies/apple_red.png",
                "name":"Apple",
                "price":5,
                "description":"blablabla",
                "fire_rate":1,
                "damage":1,
                "range":5,
                "energy_consomation":1,
                "sleeping_time": 2}

    b = Bouton(((300, 300), (50, 50)), pomme)

    object_list = [b]

    while not crashed:
        
        update_list = []
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        mouse_pressed_left = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        for index, obj in enumerate(object_list):
            etat = obj.react(mouse_pos, mouse_pressed_left)
            
            update_list = obj.draw(screen, update_list)
        
        pygame.display.update(update_list)
    
    pygame.quit()
        
