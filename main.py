from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD
import pygame

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()
        
        elif isinstance(g, Pip):
            if g.move()[0] > 0 and g.move()[0] < 1024 and g.move()[1] > 0 and g.move()[1] < 768:
                g.set_coordinates(g.move())
            else :
                graphic_elements.remove(g)
                del g

        elif isinstance(g, Tower):
            if g.get_name() == "hover":
                g.set_coordinates(
                    (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                     pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32))

    return graphic_elements

#Main

garden = Garden()

garden.spawnEnemy()

# Create HUD
hud = HUD(100,10)

view = View([garden,hud], update)
