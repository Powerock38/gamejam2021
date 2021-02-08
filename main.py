from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD
from Enemy import Enemy
import math
import pygame

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()
        
        elif isinstance(g, Pip):
            if g.move()[0] > 0 and g.move()[0] < 896 and g.move()[1] > 0 and g.move()[1] < 768:
                g.coordinates = g.move()
            else :
                graphic_elements.remove(g)
                del g
        elif isinstance(g, Tower):
            for enemy in graphic_elements[0].get_ennemies():
                pos1 = g.get_coordinates()
                pos2 = (enemy.pos[0] * 32 + enemy.pos_in_tile[0], enemy.pos[1] * 32 + enemy.pos_in_tile[1])
                delta1 = pos1[0] - pos2[0]
                delta2 = pos1[1] - pos2[1]
                distance = math.sqrt((delta1)**2 + (delta2)**2)
                angle = math.atan2(-delta2, -delta1)
                if distance < 100:
                    if g.tick == g.rate:
                        graphic_elements.append(g.attack(angle))
                        g.tick = 0
                    else:
                        g.tick += 1
            if g.name == "hover":
                g.set_coordinates(
                    (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                     pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32))
    return graphic_elements

#Main

garden = Garden()

# Create HUD
hud = HUD(100,10)

view = View([garden,hud], update)
